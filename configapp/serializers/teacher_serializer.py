from rest_framework import serializers

from . import UserSerializer
from ..models import *

class TeacherSerializer(serializers.ModelSerializer):
    # user = models.CharField(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id','user','departments','course','descriptions']



class TeacherUserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)


    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student')



class TeacherPostSerializer(serializers.Serializer):
    user = TeacherUserSerializer()
    teacher = TeacherSerializer()

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'descriptions']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'title', 'is_active', 'descriptions']


# from rest_framework import serializers
# from . import UserSerializer
# from ..models import *
#
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'descriptions']
#
# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departments
#         fields = ['id', 'title', 'is_active', 'search_fields', 'descriptions']
#
# class TeacherSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = Teacher
#         fields = ['id', 'user', 'department', 'course', 'descriptions']
#
#
# class TeacherUserSerializer(serializers.ModelSerializer):
#     is_active = serializers.BooleanField(read_only=True)
#     is_teacher = serializers.BooleanField(read_only=True)
#     is_staff = serializers.BooleanField(read_only=True)
#     is_admin = serializers.BooleanField(read_only=True)
#     is_student = serializers.BooleanField(read_only=True)
#     class Meta:
#         model = User
#         fields = (
#             'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student')
#
# class TeacherPostSerializer(serializers.Serializer):
#     user = TeacherUserSerializer()
#     teacher = TeacherSerializer()