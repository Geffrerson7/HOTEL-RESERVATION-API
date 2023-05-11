from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    @property
    def username(self):
        return self.user.username

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dni

    class Meta:
        db_table = "Client"
