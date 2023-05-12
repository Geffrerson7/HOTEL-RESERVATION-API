from .models import Reservation
from rest_framework import serializers

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "id",
            "date_in",
            "date_out",
            "status",
            "amount",
            "room",
            "room_type",
            "room_status",
            "client_first_name",
            "client_last_name",
            "client_dni",
        )
        read_only_fields = ("client_first_name", "client_last_name", "client_dni", "room_status", "room_type", "amount",)
