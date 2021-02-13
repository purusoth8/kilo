from django.db import models

from kiloapp.models import Post
from django.contrib.auth.models import User
from django.conf import settings




class CartItem(models.Model):
    cart=models.ForeignKey('Cart',on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Post,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    line_total=models.IntegerField(default=100)
    timestamp=models.DateTimeField( auto_now=False, auto_now_add=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title



# Create your models here.
class Cart(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
        address=models.CharField(max_length=50,null=True)
        phone=models.IntegerField(default=1)
        #items=models.ManyToManyField(CartItem,null=True,blank=True)
        #products=models.ManyToManyField(Post,null=True,blank=True)
        total=models.IntegerField(default=0)
        timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
        active=models.BooleanField(default=True)

        def __str__(self):
            return "Cart id: %s" %(self.id)
    
