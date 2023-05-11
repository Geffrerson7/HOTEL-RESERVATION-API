from rest_framework import viewsets
from .models import RoomType
from .serializer import RoomTypeSerializer
from rest_framework.permissions import IsAuthenticated


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAuthenticated]