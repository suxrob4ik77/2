from django.contrib.auth.hashers import make_password
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from ..models import Student, User, Parents
from ..serializers import StudentSerializer, StudentUserSerializer, StudentPostSerializer, ParentsSerializer
from ..pagination import StudentPagination
from rest_framework.generics import get_object_or_404
from ..permissions import IsAdminOrReadPatchOnly


class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return StudentPostSerializer
        return StudentSerializer

    @swagger_auto_schema(request_body=StudentPostSerializer)
    def create(self, request, *args, **kwargs):
        user_data = request.data.get('user')
        student_data = request.data.get('student')

        serializer_user = StudentUserSerializer(data=user_data)
        serializer_user.is_valid(raise_exception=True)
        validated_user = serializer_user.validated_data
        validated_user['password'] = make_password(validated_user['password'])
        validated_user['is_student'] = True
        validated_user['is_active'] = True

        user = User.objects.create(**validated_user)

        student_serializer = StudentSerializer(data=student_data)
        student_serializer.is_valid(raise_exception=True)
        student = student_serializer.save(user=user)

        if 'departments' in student_data:
            student.departments.set(student_data['departments'])

        if 'course' in student_data:
            student.course.set(student_data['course'])

        response_data = {
            'user': StudentUserSerializer(user).data,
            'student': StudentSerializer(student).data,
            'success': True
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination


class ParentViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminOrReadPatchOnly]
    pagination_class = StudentPagination

    def list(self, request):
        parents = Parents.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(parents, request)
        serializer = ParentsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        parent = get_object_or_404(Parents, pk=pk)
        serializer = ParentsSerializer(parent)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/parent')
    @swagger_auto_schema(request_body=ParentsSerializer)
    def create_parent(self, request):
        serializer = ParentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/parent')
    @swagger_auto_schema(request_body=ParentsSerializer)
    def update_parent(self, request, pk=None):
        parent = get_object_or_404(Parents, pk=pk)
        serializer = ParentsSerializer(parent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/parent')
    def delete_parent(self, request, pk=None):
        parent = get_object_or_404(Parents, pk=pk)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



















#
# class StudentApi(APIView):
#     @swagger_auto_schema(request_body=StudentPostSerializer)
#     def post(self, request):
#         data = {"success": True}
#         user_data = request.data['user']
#         student_data = request.data['student']
#
#         user_serializer = StudentUserSerializer(data=user_data)
#         user_serializer.is_valid(raise_exception=True)
#
#         validated_user = user_serializer.validated_data
#         validated_user['password'] = make_password(validated_user['password'])
#         validated_user['is_student'] = True
#         validated_user['is_active'] = True
#
#         user = User.objects.create(**validated_user)
#
#         student_serializer = StudentSerializer(data=student_data)
#         student_serializer.is_valid(raise_exception=True)
#
#         student = student_serializer.save(user=user)
#
#         if 'departments' in student_data:
#             student.departments.set(student_data['departments'])
#         if 'course' in student_data:
#             student.course.set(student_data['course'])
#
#         data['user'] = StudentUserSerializer(user).data
#         data['student'] = StudentSerializer(student).data
#         return Response(data)


