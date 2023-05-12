from django.db import models
from django.contrib.auth.models import User
from room.models import Room

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('PAID', 'PAID'),
        ('CANCELED', 'CANCELED'),
    ]

    @property
    def room_status(self):
        return self.room.is_reserved
    
    @property
    def room_type(self):
        return self.room.room_type.name
    
    @property
    def client_first_name(self):
        return self.user.client.first_name
    
    @property
    def client_last_name(self):
        return self.user.client.last_name
    
    @property
    def client_dni(self):
        return self.user.client.dni
    
    date_in = models.DateField()
    date_out = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation room: {self.room.number}"

    class Meta:
        db_table = "Reservation"
