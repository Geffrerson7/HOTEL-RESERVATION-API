from rest_framework import viewsets
from .models import Reservation
from .serializer import ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)
