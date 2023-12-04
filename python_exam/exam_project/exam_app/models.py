from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if(len(postData['first_name']) < 2):
            errors['first_name'] = "First Name should be 2 characters!"
        if(len(postData['last_name']) < 2):
            errors['last_name'] = "Last Name should be 2 characters!"
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confrim_password']:
            errors['con-password'] = "Passwords should be matched"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):        
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        return errors
    
    def report_validator(self, postData):
        errors = {}
        if(len(postData['location']) <= 0):
            errors['location'] = "Location is Required"
        if(len(postData['SightDate']) <= 0):
            errors['date'] = "Date is Required and should be in the past"
        if(len(postData['numberSas']) < 1):
            errors['numberSas'] = "Number of sasquatches should be at least 1"
        if(len(postData['desc']) >= 50):
            errors['desc'] = "What happened now should be less than 50 characters"
        return errors


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Report(models.Model):
    location = models.CharField(max_length=45)
    date = models.DateField()
    numberOfSasq = models.IntegerField()
    desc = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="reports", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()