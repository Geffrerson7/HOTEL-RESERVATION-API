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
        room_price = serializer.validated_data['room'].room_price
        serializer.save(user=self.request.user, amount=room_price)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)
