from .models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = 'id','reservation', 'payment_method',"reservation_price", 'room_status',
        read_only_fields = "reservation_price", 'payment_date', 'room_status',
        