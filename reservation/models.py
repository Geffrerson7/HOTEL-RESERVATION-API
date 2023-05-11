from django.db import models
from enumfields import EnumField
from enum import Enum
from client.models import Client
from room.models import Room


class ReservationStatus(Enum):
    PENDING = 'PENDING'
    PAID = 'PAID'
    CANCELED = 'CANCELED'


class Reservation(models.Model):
    
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    status = EnumField(ReservationStatus)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Rerervation"