# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.db.models import Q
# from ..models.davomat_model import Davomat
# from ..models.model_teacher import Teacher
# from ..serializers.davomat_serializer import DavomatSerializer, DavomatCreateSerializer
# from configapp.permissions import IsTeacherOnly, IsAdminOrTeacher
#
#
# class DavomatViewSet(viewsets.ModelViewSet):
#     serializer_class = DavomatSerializer
#     permission_classes = [IsAdminOrTeacher]
#
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_admin or user.is_superuser:
#             return Davomat.objects.all()
#
#         # For teachers, only show attendance records they created
#         teacher = Teacher.objects.get(user=user)
#         return Davomat.objects.filter(teacher=teacher)
#
#     def get_serializer_class(self):
#         if self.action == 'create':
#             return DavomatCreateSerializer
#         return DavomatSerializer
#
#     @action(detail=False, methods=['get'])
#     def by_group(self, request):
#         group_id = request.query_params.get('group_id')
#         if not group_id:
#             return Response({"error": "group_id is required"}, status=status.HTTP_400_BAD_REQUEST)
#
#         queryset = self.get_queryset().filter(group_id=group_id)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['get'])
#     def by_student(self, request):
#         student_id = request.query_params.get('student_id')
#         if not student_id:
#             return Response({"error": "student_id is required"}, status=status.HTTP_400_BAD_REQUEST)
#
#         queryset = self.get_queryset().filter(student_id=student_id)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['get'])
#     def by_date(self, request):
#         date = request.query_params.get('date')
#         if not date:
#             return Response({"error": "date is required"}, status=status.HTTP_400_BAD_REQUEST)
#
#         queryset = self.get_queryset().filter(date=date)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models.davomat_model import Davomat
from ..models.model_teacher import Teacher
from ..serializers.davomat_serializer import DavomatSerializer, DavomatCreateSerializer
from ..permissions import *
from rest_framework.exceptions import PermissionDenied
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DavomatViewSet(viewsets.ModelViewSet):
    serializer_class = DavomatSerializer
    # permission_classes = [IsAdminOrTeacher]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or getattr(user, 'is_admin', False):
            return Davomat.objects.all()
        return Davomat.objects.none()  # Non-admin users can't see any records

    def get_serializer_class(self):
        if self.action == 'create':
            return DavomatCreateSerializer
        return DavomatSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def create(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied("Avval tizimga kirishingiz kerak.")

        if not (user.is_superuser or getattr(user, 'is_admin', False)):
            raise PermissionDenied("Faqat admin foydalanuvchilari davomat qo'shishi mumkin.")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied("Avval tizimga kirishingiz kerak.")

        if not (user.is_superuser or getattr(user, 'is_admin', False)):
            raise PermissionDenied("Faqat admin foydalanuvchilari davomatni tahrirlashi mumkin.")

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied("Avval tizimga kirishingiz kerak.")

        if not (user.is_superuser or getattr(user, 'is_admin', False)):
            raise PermissionDenied("Faqat admin foydalanuvchilari davomatni o'chirishi mumkin.")

        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'group_id',
                openapi.IN_QUERY,
                description="Guruh ID si",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
            openapi.Parameter(
                'page',
                openapi.IN_QUERY,
                description="Sahifa raqami",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ]
    )
    @action(detail=False, methods=['get'])
    def by_group(self, request):
        user = request.user
        if not (user.is_superuser or getattr(user, 'is_admin', False)):
            raise PermissionDenied("Faqat admin foydalanuvchilari bu ma'lumotlarni ko'rishi mumkin.")

        group_id = request.query_params.get('group_id')
        if not group_id:
            return Response({
                "error": "group_id parametri talab qilinadi",
                "example": "/api/davomat/by_group/?group_id=1&page=1"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            group_id = int(group_id)
        except ValueError:
            return Response({
                "error": "group_id raqam bo'lishi kerak",
                "example": "/api/davomat/by_group/?group_id=1&page=1"
            }, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(group_id=group_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'student_id',
                openapi.IN_QUERY,
                description="Talaba ID si",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
            openapi.Parameter(
                'page',
                openapi.IN_QUERY,
                description="Sahifa raqami",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ]
    )
    @action(detail=False, methods=['get'])
    def by_student(self, request):
        user = request.user
        if not (user.is_superuser or getattr(user, 'is_admin', False)):
            raise PermissionDenied("Faqat admin foydalanuvchilari bu ma'lumotlarni ko'rishi mumkin.")

        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({
                "error": "student_id parametri talab qilinadi",
                "example": "/api/davomat/by_student/?student_id=1&page=1"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            student_id = int(student_id)
        except ValueError:
            return Response({
                "error": "student_id raqam bo'lishi kerak",
                "example": "/api/davomat/by_student/?student_id=1&page=1"
            }, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(student_id=student_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'date',
                openapi.IN_QUERY,
                description="Sana (YYYY-MM-DD formatida)",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'page',
                openapi.IN_QUERY,
                description="Sahifa raqami",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ]
    )
    @action(detail=False, methods=['get'])
    def by_date(self, request):
        user = request.user
        if not (user.is_superuser or getattr(user, 'is_admin', False)):
            raise PermissionDenied("Faqat admin foydalanuvchilari bu ma'lumotlarni ko'rishi mumkin.")

        date = request.query_params.get('date')
        if not date:
            return Response({
                "error": "date parametri talab qilinadi",
                "example": "/api/davomat/by_date/?date=2024-04-27&page=1"
            }, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(date=date)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
