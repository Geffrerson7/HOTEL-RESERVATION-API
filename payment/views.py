from .models import Payment
from .serializer import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from reservation.models import Reservation
from room.models import Room
from django_filters import rest_framework as filters
from .filters import PaymentFilter
from .pagination import StandardResultsSetPagination


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all().order_by("id")
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PaymentFilter
    filter_class =PaymentFilter
    pagination_class = StandardResultsSetPagination

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
    
    def get_queryset(self):
        queryset = Payment.objects.all()
        user_id = self.request.user.id
        queryset = queryset.filter(reservation__user__id=user_id)
        return self.filter_class(self.request.GET, queryset=queryset, request=self.request).qs
