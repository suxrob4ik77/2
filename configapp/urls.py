from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import *
from .views.davomat_view import *
from .views.group_view import *

router = DefaultRouter()
# Teacher
router.register(r'teacher', TeacherViewSet, basename='teacher')
#Student
router.register(r'student', StudentApi, basename='student')
#Group
router.register(r'group', GroupViewSet, basename='group')
# Davomat
router.register(r'davomat', DavomatViewSet,basename='davomat')
# Parents
router.register(r'parents', ParentViewSet, basename='parent')
#Department
router.register(r'department', DepartmentViewSet, basename='department')
# Course
router.register(r'course', CourseViewSet, basename='course')
router.register(r'table', TableViewSet, basename='table')
router.register(r'table_type', TableTypeViewSet, basename='tabletype')
router.register(r'rooms', RoomsViewSet, basename='rooms')
router.register(r'homeworks',HomeworkViewSet,basename='homework')
router.register(r'homework-submissions',HomeworkSubmissionViewSet,basename='homework-submission')
router.register(r'homework-reviews',HomeworkReviewViewSet,basename='homework-review')
router.register(r'months',MonthViewSet,basename='month')
router.register(r'payment-type',PaymentTypeViewSet,basename='payment-type')
router.register(r'payment',PaymentViewSet,basename='payment')

urlpatterns = [
    path('post_send_otp/', PhoneSendOTP.as_view()),
    path('post_v_otp/', VerifySMS.as_view()),
    path('register/', RegisterUserApi.as_view()),
    # Token
    path('token/', LoginApi.as_view(), name='token'),
    path('tokenref', TokenRefreshView.as_view(), name='token'),
    path('tokenac', TokenBlacklistView.as_view(), name='token'),
    path('', include(router.urls)),
    path('users/create/', RegisterUserApi.as_view()),
    path('users/detail/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    #Static
    path('students-statistic/', StudentFilterView.as_view(), name='recent-students'),
    path('teachers-statistic/', TeacherFilterView.as_view(), name='teachers-statistic'),
    path('courses-statistics', CourseFilterView.as_view(), name='courses-statistics'),
    path('davomat-statistics', DavomatFilterView.as_view(), name='davomat-statistics'),
    path('payments-statistics', PaymentFilterView.as_view(), name='payments-statistics'),
]

