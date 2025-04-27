# from pickletools import string4
# from tkinter.constants import CASCADE
#
# from django.template.defaultfilters import time
#
# from .auth_users import *
# from .model_teacher import *
#
#
# class Rooms(BaseModel):
#     title = models.CharField(max_length=50)
#     descriptions = models.CharField(max_length=500,blank=True,null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class TableType(BaseModel):
#     title = models.CharField(max_length=50)
#     descriptions = models.CharField(max_length=500,blank=True,null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Table(BaseModel):
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     room = models.ForeignKey(Rooms, on_delete=models.RESTRICT)
#     type = models.ForeignKey(TableType, on_delete=models.RESTRICT)
#     descriptions = models.CharField(max_length=500, blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.start_time} - {self.end_time}"
#
#
#
#
# class GroupStudent(BaseModel):
#     title = models.CharField(max_length=40, unique=True)
#     course = models.ForeignKey(Course, on_delete=models.RESTRICT,related_name='course')
#     teacher = models.ManyToManyField(Teacher, related_name='teacher_get')
#     table = models.ForeignKey(Table,on_delete=models.CASCADE)
#     start_time = models.DateField()
#     end_time = models.DateField()
#     descriptions = models.CharField(max_length=500,blank=True,null=True)
#
#     def __str__(self):
#         return self.title
#

from django.db import models
from .auth_users import *
from .model_teacher import *


class Rooms(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class TableType(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class Table(BaseModel):
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(Rooms, on_delete=models.RESTRICT)
    type = models.ForeignKey(TableType, on_delete=models.RESTRICT)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.start_time.__str__()+" "+self.end_time.__str__()


class GroupStudent(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    teacher = models.ManyToManyField(Teacher, related_name='get_teacher')
    table = models.ForeignKey(Table, on_delete=models.RESTRICT)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
