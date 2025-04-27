
from rest_framework import serializers
from ..models import model_group, model_teacher, GroupStudent
from .teacher_serializer import *


class GroupStudentSerializer(serializers.ModelSerializer):

      teacher = TeacherSerializer(read_only=Teacher,many=True)

      class Meta:
          model = GroupStudent
          fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'start_time', 'end_time', 'room', 'type', 'descriptions']

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = ['id', 'title', 'descriptions']

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'title', 'descriptions']



