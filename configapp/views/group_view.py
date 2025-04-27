
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import GroupStudent
from ..serializers import GroupStudentSerializer
from ..permissions import IsAdminOrReadPatchOnly


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]