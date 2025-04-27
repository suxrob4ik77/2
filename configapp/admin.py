
from django.contrib import admin
from .models import *
from .models.davomat_model import Davomat

# Register your models here.
admin.site.register([Teacher,Departments,Course,User,Student,GroupStudent,Table,Rooms,TableType,Davomat,Homework,HomeworkReview,HomeworkSubmission,PaymentType,Parents,Month])