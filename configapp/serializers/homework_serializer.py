from rest_framework import serializers
from ..models import *
from ..serializers import *

from rest_framework import serializers
from ..models import Homework, HomeworkSubmission, HomeworkReview


class HomeworkSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=True)
    # group = serializers.IntegerField(required=True)
    group = serializers.PrimaryKeyRelatedField(queryset=GroupStudent.objects.all())
    class Meta:
        model = Homework
        fields = ['id', 'title', 'description', 'group', 'teacher', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {
                'required': True,
                'min_length': 1,
                'max_length': 255,
                'help_text': 'Homework title'
            },
            'description': {
                'required': True,
                'help_text': 'Homework description'
            },
            'group': {
                'required': True,
                'help_text': 'Group ID'
            },
            'teacher': {
                'required': True,
                'help_text': 'Teacher ID (Teacher who created the homework)'
            }
        }

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or contain only whitespace")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be empty or contain only whitespace")
        return value

    def validate_group(self, value):
        if not value:
            raise serializers.ValidationError("Group is required")
        return value


class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=True)  # student ID
    homework = serializers.PrimaryKeyRelatedField(queryset=Homework.objects.all(), required=True)

    class Meta:
        model = HomeworkSubmission
        fields = ['id', 'homework', 'student', 'link', 'is_checked', 'created_at', 'updated_at']
        read_only_fields = ['id', 'student', 'is_checked', 'created_at', 'updated_at']
        extra_kwargs = {
            'homework': {'required': True},
            'link': {
                'required': True,
                'max_length': 255,
                'help_text': 'Link to the homework submission'
            }
        }

    def validate_link(self, value):
        if not value.strip():
            raise serializers.ValidationError("Link cannot be empty or contain only whitespace")
        return value


class HomeworkReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkReview
        fields = ['id', 'submission', 'teacher', 'comment', 'ball', 'created_at', 'updated_at']
        read_only_fields = ['id', 'teacher', 'created_at', 'updated_at']
        extra_kwargs = {
            'submission': {'required': True},
            'comment': {
                'required': False,
                'allow_null': True,
                'help_text': 'Review comment'
            },
            'ball': {
                'required': False,
                'allow_null': True,
                'min_value': 0,
                'max_value': 100,
                'help_text': 'Grade from 0 to 100'
            }
        }