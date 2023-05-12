from django.db import models
from roomType.models import RoomType


class Room(models.Model):

    @property
    def room_price(self):
        return self.room_type.price
    
    number = models.CharField(max_length=100, unique=True)
    floor = models.IntegerField()
    is_reserved = models.BooleanField(default=False)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="room_type")

    def __str__(self):
        return self.number

    class Meta:
        db_table = "Room"