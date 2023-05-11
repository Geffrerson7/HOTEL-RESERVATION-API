from .models import Payment
from .serializer import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from reservation.models import Reservation
from room.models import Room

class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def perform_create(self, serializer):
        reservation_id = self.request.data.get('reservation')
        if reservation_id:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.status = "PAID"
            room = Room.objects.get(id=reservation.room.id)
            room.is_reserved= True
            reservation.save()
            room.save()
        serializer.save()
