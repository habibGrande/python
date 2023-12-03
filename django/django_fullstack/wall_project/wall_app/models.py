from django.db import models
import re
# Create your models here.
class Users_validation(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "user first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "user last name should be at least 2 characters"
        if len(postData['password']) <  8:
            errors['password']   = 'Password shpuld be at least 8 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
             errors['email'] = "Invalid email address!"
        if postData['conf-pass'] != postData['password']:
            errors['conf-pass']= 'password is not the same'
        return errors
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email-login']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['password-login']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        return errors
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    passowrd = models.CharField(max_length=45)
    confirm_passowrd = models.CharField(max_length=45)
    objects = Users_validation()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    masssege = models.TextField(null=True)
    user = models.ForeignKey(Users,related_name="messages",on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Users,related_name="comments",on_delete=models.CASCADE,null=True )
    messages = models.ForeignKey(Messages,related_name='comment',on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
