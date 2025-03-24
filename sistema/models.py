from django.db import models
from django.utils import timezone

# Create your models here.

# * User class model here. *
class User (models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 11)
    phone_number = models.CharField(max_length = 20)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    register_date = models.DateTimeField(default = timezone.now)
    active = models.BooleanField(default = True)

    # photo =
