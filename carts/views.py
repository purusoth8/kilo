from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage


# Create your views here.
from kiloapp.models import Post

from .models import Cart,CartItem

def email_one(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id=None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        
        context = {"cart":cart}
    subject = "Order for "+str(cart.author)
    to = [str(request.user.email),'kilobiriyanilk@gmail.com']
    from_email = 'kilobiriyanilk@gmail.com'
    message = get_template('carts/inside.html').render(context)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
    return render(request,'carts/mail.html',context)

@login_required
def mailth(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id=None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart":cart}
    else:
        empty_message="Your cart is empty please keep shopping"
        context= {"empty":True,"empty_message":empty_message}
        
    return render(request,'carts/mail.html',context)



# def mail(request):
#     try:
#         the_id = request.session['cart_id']
#     except:
#         the_id=None
#     if the_id:
#         cart = Cart.objects.get(id=the_id)
        
#         context = {"cart":cart}
#     send_mail(
#     'Order for '+str(cart.author),
#     'Address :'+cart.address+
#     '\n Total '+str(cart.total)+''
#     ,
#     'mammamaathiyosi@gmail.com',
#     ['wecove1584@hrandod.com'],
#     fail_silently=False,)

#     return render(request,'carts/mail.html',context)

@login_required
def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id=None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart":cart}
    else:
        empty_message="Your cart is empty please keep shopping"
        context= {"empty":True,"empty_message":empty_message}
        
    return render(request,'carts/view.html',context)


@login_required
def update_cart(request,id):
    request.session.set_expiry(1500)
    try:
        qty = request.GET.get('qty')
        update_qty = True

    except:
        qty= None
        update_qty = False
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id']=new_cart.id
        the_id=new_cart.id


    cart=Cart.objects.get(id=the_id)
    

    try:
        product=Post.objects.get(id=id)
    except Post.DoesNotExist:
        pass
    except:
        pass


    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)
    if created:
        print("ya")


    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity=qty
            cart_item.save()
    else:
        pass

    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)

    new_total = 0
    for item in cart.cartitem_set.all():
        line_total=(item.product.price) * item.quantity
        new_total +=line_total

    request.session['items_total']=cart.cartitem_set.count()
    #print(cart.products.count())
    user = request.user
    cart.address=request.user.profile.address
    cart.phone=request.user.profile.phone1
    
    cart.author = user
    cart.total=new_total
    cart.save()

    return HttpResponseRedirect(reverse("cart"))


