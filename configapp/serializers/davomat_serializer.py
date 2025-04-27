# from rest_framework import serializers
# from ..models.davomat_model import Davomat
# from ..models.model_student import Student
# from ..models.model_group import GroupStudent
# from ..models.model_teacher import Teacher
#
#
# class DavomatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Davomat
#         fields = ['id', 'student', 'group', 'teacher', 'date', 'is_present', 'notes']
#         read_only_fields = ['teacher']
#
#     def validate(self, data):
#         # Ensure the student belongs to the group
#         if not data['student'].group.filter(id=data['group'].id).exists():
#             raise serializers.ValidationError("Student does not belong to this group")
#         return data
#
#
# class DavomatCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Davomat
#         fields = ['id', 'student', 'group', 'date', 'is_present', 'notes']
#         read_only_fields = ['teacher']
#
#     def validate(self, data):
#         # Ensure the student belongs to the group
#         if not data['student'].group.filter(id=data['group'].id).exists():
#             raise serializers.ValidationError("Student does not belong to this group")
#         return data
#
#     def create(self, validated_data):
#         # Automatically set the teacher from the request user
#         teacher = Teacher.objects.get(user=self.context['request'].user)
#         validated_data['teacher'] = teacher
#         return super().create(validated_data)


from rest_framework import serializers
from ..models.davomat_model import Davomat
from ..models.model_student import Student
from ..models.model_group import GroupStudent
from ..models.model_teacher import Teacher


class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = ['id', 'student', 'group', 'teacher', 'date', 'is_present', 'notes']
        read_only_fields = ['teacher']

    def validate(self, data):
        # Talaba guruhga tegishlimi - tekshir
        if not data['student'].group.filter(id=data['group'].id).exists():
            raise serializers.ValidationError("Ushbu talaba bu guruhga tegishli emas.")
        return data


class DavomatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = ['id', 'student', 'group', 'date', 'is_present', 'notes']
        read_only_fields = ['teacher']

    def validate(self, data):
        # Talaba guruhga tegishlimi - tekshir
        if not data['student'].group.filter(id=data['group'].id).exists():
            raise serializers.ValidationError("Ushbu talaba bu guruhga tegishli emas.")
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        try:
            teacher = Teacher.objects.get(user=user)
        except Teacher.DoesNotExist:
            raise serializers.ValidationError("Ushbu foydalanuvchi bilan bog‘liq o‘qituvchi (Teacher) topilmadi.")

        validated_data['teacher'] = teacher
        return super().create(validated_data)
