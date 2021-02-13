from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField(default=1)
    address=models.CharField(default="na",max_length=500)
    phone1 = PhoneField(blank=True, help_text='Contact phone number')


    def __str__(self):
        return f'{self.user.username} Profile'
    
