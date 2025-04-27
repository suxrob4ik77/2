from django.db import models
from .model_student import Student
from .model_group import GroupStudent
from .model_teacher import Teacher
from .auth_users import BaseModel


class Davomat(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records',default='test')
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, related_name='group_attendance',default='Kamron')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_attendance',default='+998992223344')
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True,default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.date} - {'Present' if self.is_present else 'Absent'}"

    class Meta:
        ordering = ['-date', '-created_at']  # Order by date and created_at in descending order