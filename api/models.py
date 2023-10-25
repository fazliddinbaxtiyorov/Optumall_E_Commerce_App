from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.first_name
