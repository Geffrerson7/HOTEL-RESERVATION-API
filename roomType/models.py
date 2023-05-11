from django.db import models

# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Room_Type"
