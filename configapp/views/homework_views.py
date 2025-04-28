from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from ..models import *
from ..permissions import *
from ..pagination import *
from ..serializers import *
class HomeworkViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        homeworks = Homework.objects.all()
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        homework = get_object_or_404(Homework, pk=pk)
        serializer = HomeworkSerializer(homework)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create')
    @swagger_auto_schema(request_body=HomeworkSerializer)
    def create_homework(self, request):
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update')
    @swagger_auto_schema(request_body=HomeworkSerializer)
    def update_homework(self, request, pk=None):
        homework = get_object_or_404(Homework, pk=pk)
        serializer = HomeworkSerializer(homework, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_homework(self, request, pk=None):
        homework = get_object_or_404(Homework, pk=pk)
        homework.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class HomeworkViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#
#     def list(self, request):
#         homeworks = Homework.objects.all()
#         serializer = HomeworkSerializer(homeworks, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         homework = get_object_or_404(Homework, pk=pk)
#         serializer = HomeworkSerializer(homework)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['post'], url_path='create')
#     @swagger_auto_schema(request_body=HomeworkSerializer)
#     def create_homework(self, request):
#         serializer = HomeworkSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 teacher = Teacher.objects.get(user=request.user)
#                 serializer.validated_data['teacher'] = teacher
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except Teacher.DoesNotExist:
#                 return Response(
#                     {"error": "Sizga bog'langan o'qituvchi topilmadi. Faqat o'qituvchilar uy vazifasi yaratishi mumkin."},
#                     status=status.HTTP_403_FORBIDDEN
#                 )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     @action(detail=True, methods=['put'], url_path='update')
#     @swagger_auto_schema(request_body=HomeworkSerializer)
#     def update_homework(self, request, pk=None):
#         homework = get_object_or_404(Homework, pk=pk)
#         try:
#             teacher = Teacher.objects.get(user=request.user)
#             if homework.teacher != teacher and not request.user.is_admin and not request.user.is_superuser:
#                 return Response(
#                     {"error": "Siz faqat o'zingiz yaratgan uy vazifalarini tahrirlashingiz mumkin."},
#                     status=status.HTTP_403_FORBIDDEN
#                 )
#             serializer = HomeworkSerializer(homework, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Teacher.DoesNotExist:
#             return Response(
#                 {"error": "Sizga bog'langan o'qituvchi topilmadi."},
#                 status=status.HTTP_403_FORBIDDEN
#             )
#
#     @action(detail=True, methods=['delete'], url_path='delete')
#     def delete_homework(self, request, pk=None):
#         homework = get_object_or_404(Homework, pk=pk)
#         try:
#             teacher = Teacher.objects.get(user=request.user)
#             if homework.teacher != teacher and not request.user.is_admin and not request.user.is_superuser:
#                 return Response(
#                     {"error": "Siz faqat o'zingiz yaratgan uy vazifalarini o'chirishingiz mumkin."},
#                     status=status.HTTP_403_FORBIDDEN
#                 )
#             homework.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Teacher.DoesNotExist:
#             return Response(
#                 {"error": "Sizga bog'langan o'qituvchi topilmadi."},
#                 status=status.HTTP_403_FORBIDDEN
#             )
#
#

class HomeworkReviewViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        homework = HomeworkReview.objects.all()
        serializer = HomeworkReviewSerializer(homework, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        homework = get_object_or_404(HomeworkReview, pk=pk)
        serializer = HomeworkReviewSerializer(homework)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/review')
    @swagger_auto_schema(request_body=HomeworkReviewSerializer)
    def create_homework_review(self, request):
        serializer = HomeworkReviewSerializer(data=request.data)
        if serializer.is_valid():
            try:
                teacher = Teacher.objects.get(user=request.user)
                serializer.validated_data['teacher'] = teacher
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Teacher.DoesNotExist:
                return Response(
                    {"error": "Sizga bog'langan o'qituvchi topilmadi. Faqat o'qituvchilar baho qo'yishi mumkin."},
                    status=status.HTTP_403_FORBIDDEN
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/review')
    @swagger_auto_schema(request_body=HomeworkReviewSerializer)
    def update_homework_review(self, request, pk=None):
        homework = get_object_or_404(HomeworkReview, pk=pk)
        try:
            teacher = Teacher.objects.get(user=request.user)
            if homework.teacher != teacher and not request.user.is_admin and not request.user.is_superuser:
                return Response(
                    {"error": "Siz faqat o'zingiz yaratgan baholarni tahrirlashingiz mumkin."},
                    status=status.HTTP_403_FORBIDDEN
                )
            serializer = HomeworkReviewSerializer(homework, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response(
                {"error": "Sizga bog'langan o'qituvchi topilmadi."},
                status=status.HTTP_403_FORBIDDEN
            )

    @action(detail=True, methods=['delete'], url_path='delete/review')
    def delete_homework_review(self, request, pk=None):
        homework = get_object_or_404(HomeworkReview, pk=pk)
        try:
            teacher = Teacher.objects.get(user=request.user)
            if homework.teacher != teacher and not request.user.is_admin and not request.user.is_superuser:
                return Response(
                    {"error": "Siz faqat o'zingiz yaratgan baholarni o'chirishingiz mumkin."},
                    status=status.HTTP_403_FORBIDDEN
                )
            homework.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response(
                {"error": "Sizga bog'langan o'qituvchi topilmadi."},
                status=status.HTTP_403_FORBIDDEN
            )



class HomeworkSubmissionViewSet(viewsets.ViewSet):
    # permission_classes = [AdminOrStudent]

    def list(self, request):
        homework = HomeworkSubmission.objects.all()
        serializer = HomeworkSubmissionSerializer(homework, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        homework = get_object_or_404(HomeworkSubmission, pk=pk)
        serializer = HomeworkSubmissionSerializer(homework)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/submission')
    @swagger_auto_schema(request_body=HomeworkSubmissionSerializer)
    def create_homework_submission(self, request):
        serializer = HomeworkSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['student'] = request.user.student
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/submission')
    @swagger_auto_schema(request_body=HomeworkSubmissionSerializer)
    def update_homework_submission(self, request, pk=None):
        homework = get_object_or_404(HomeworkSubmission, pk=pk)
        serializer = HomeworkSubmissionSerializer(homework, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/submission')
    def delete_homework_submission(self, request, pk=None):
        homework = get_object_or_404(HomeworkSubmission, pk=pk)
        homework.delete()
        return Response({'status':True,'detail': 'HomeworkSubmission muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

