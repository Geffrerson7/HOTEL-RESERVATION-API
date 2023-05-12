from .models import Room
from rest_framework import serializers
from roomType.models import RoomType

class RoomSerializer(serializers.ModelSerializer):
    room_type = serializers.SlugRelatedField(
        queryset=RoomType.objects.all(), slug_field="name"
    )
    class Meta:
        model = Room
        fields = 'id', 'number', 'floor', 'is_reserved', 'room_price', 'room_type'
        read_only_fields = 'room_price', 