from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    passowrd = models.CharField(max_length=45)
    confirm_passowrd = models.CharField(max_length=45)
    