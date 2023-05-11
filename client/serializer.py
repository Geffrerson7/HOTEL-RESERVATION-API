from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "first_name",
            "last_name",
            "dni",
            "age",
            "gender",
            "contact_number",
            "address",
            "username",
        )
        read_only_fields = ("username",)
        