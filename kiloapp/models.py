from django.db import models


food_choice=[
    ('Biriyani','Biriyani'),
    ('Curries','Curries'),
    ('Garlic Rice','Garlic Rice'),
    ('Juice Bar','Juice Bar'),
    ('Kilo koththu','Kilo koththu')]

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200,default="n/a")
    cover = models.ImageField(upload_to='images/',default='kiloapp/images/logo.jpeg')
    food= models.CharField(max_length=15,choices=food_choice,default='Juice Bar')
    offer=models.IntegerField(default=0)
    spacial=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name