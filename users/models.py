from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone1=models.IntegerField(default=0)
    address=models.CharField(default="",max_length=500)


    def __str__(self):
        return f'{self.user.username} Profile'
    
