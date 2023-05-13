from rest_framework import viewsets
from .models import Room
from .serializer import RoomSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
