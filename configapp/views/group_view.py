
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import GroupStudent,Table,TableType,Rooms
from ..serializers import GroupStudentSerializer,TableSerializer,TableTypeSerializer,RoomsSerializer
from ..permissions import IsAdminOrReadPatchOnly


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]

class TableTypeViewSet(viewsets.ModelViewSet):
    queryset = TableType.objects.all()
    serializer_class = TableTypeSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]