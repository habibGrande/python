from django.db import models
from django.utils import timezone
# Create your models here.

class ShowsManager(models.Manager):
    def shows_validator(self,postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
   
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=45)
    Network = models.CharField(max_length=45)
    Release_Date = models.CharField(max_length=45)
    description = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
