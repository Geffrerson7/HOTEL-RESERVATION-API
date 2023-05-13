from rest_framework import viewsets
from .models import Reservation
from .serializer import ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        room_price = serializer.validated_data["room"].room_price
        serializer.save(user=self.request.user, amount=room_price)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get('status') == 'CANCELED':
            instance.room.is_reserved = False
            instance.room.save()

        self.perform_update(serializer)
        return Response(serializer.data)

