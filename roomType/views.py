from rest_framework import viewsets
from .models import RoomType
from .serializer import RoomTypeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .pagination import StandardResultsSetPagination


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all().order_by("id")
    serializer_class = RoomTypeSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]