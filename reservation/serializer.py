from .models import Reservation
from rest_framework import serializers


class ReservationStatusSerializer(serializers.Field):
    def to_representation(self, value):
        return value.value

    def to_internal_value(self, data):
        return Reservation.ReservationStatus(data)


class ReservationSerializer(serializers.ModelSerializer):
    status = ReservationStatusSerializer()

    class Meta:
        model = Reservation
        fields = (
            "id",
            "fecha_inicio",
            "fecha_fin",
            "status",
            "amount",
            "room",
            "room_type",
            "room_status",
            "client_first_name",
            "client_last_name",
            "client_dni",
        )
        read_only_fields = ("client_first_name", "client_last_name", "client_dni", "room_status", "room_type")
