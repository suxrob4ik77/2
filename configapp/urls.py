from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
from .views.davomat_view import *
from .views.group_view import *

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentApi, basename='student')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'davomat', DavomatViewSet,basename='davomat')
router.register(r'parents', ParentViewSet, basename='parent')
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'table', TableViewSet, basename='table')
router.register(r'table_type', TableTypeViewSet, basename='tabletype')
router.register(r'rooms', RoomsViewSet, basename='rooms')


urlpatterns = [
    path('post_send_otp/', PhoneSendOTP.as_view()),
    path('post_v_otp/', VerifySMS.as_view()),
    path('register/', RegisterUserApi.as_view()),
    # path('student/', StudentApi.as_view()),
    path('token/', LoginApi.as_view(), name='token'),
    # path('teacher/create/', TeacherCreateApi.as_view(), name='teacher-create'),
    path('', include(router.urls)),
]

