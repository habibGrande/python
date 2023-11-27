from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=45)
    Network = models.CharField(max_length=45)
    Release_Date = models.CharField(max_length=45)
    description = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)