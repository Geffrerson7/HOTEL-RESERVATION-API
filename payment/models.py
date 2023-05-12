from django.db import models
from reservation.models import Reservation

class Payment(models.Model):
    @property
    def reservation_price(self):
        return self.reservation.amount
    
    @property
    def room_status(self):
        return self.reservation.room_status
            
    PAYMENT_METHOD_CHOICES = (
        ('bank transfer', 'Wire Transfer'),
        ('credit card', 'Credit Card'),
    )

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateField(auto_now_add=True)
    hotel_name = models.CharField(max_length=100, default="Hotel 5 stars")
    hotel_address = models.CharField(max_length=100, default="Lima")
    hotel_ruc = models.CharField(max_length=11, default="12345678910")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservation")
    
    class Meta:
        db_table = "Payment"