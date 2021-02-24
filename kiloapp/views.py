from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.db.models import Q # new


food_choice=[
    ('Biriyani','Biriyani'),
    ('Curries','Curries'),
    ('Garlic Rice','Garlic Rice'),
    ('Juice Bar','Juice Bar'),
    ('Kilo koththu','Kilo koththu')]

import requests


def about(request):
    return render(request,'kiloapp/about.html')

def res(request):
    #print(request.GET)
    name = request.GET.get('name')
    address1 = request.GET.get('address1')
    address2 = request.GET.get('address2')
    date = request.GET.get('date')
    per = request.GET.get('per')
    time = request.GET.get('time')
    email = request.GET.get('email')
    phone = request.GET.get('phone')

    context={
        'name':name,
        'address1':address1,
        'address2':address2,
        'date':date,
        'per':per,
        'time':time,
        'email':email,
        'phone':phone,
    }

    if request.GET.get('name'):

        subject = "Order for "+str(name)
        to = ['kilobiriyanilk@gmail.com',email]
        from_email = 'kilobiriyanilk@gmail.com'
        message = get_template('carts/inside2.html').render(context)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
    
    else:
        print("non")



    return render(request,'kiloapp/reservation.html')


# Create your views here.
def index(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'kiloapp/index.html',context)

class PostListView(ListView):
        model=Post
        template_name='kiloapp/index.html'
        context_object_name='posts'

class SearchResultsView(ListView):
        model=Post
        template_name='kiloapp/search_results.html'

        def get_queryset(self): # new
            query = self.request.GET.get('q')
            object_list = Post.objects.filter(
                Q(name__icontains=query) | Q(food__icontains=query)
            )
            return object_list

class PostDetailView(DetailView):
        model=Post



def menu(request):
    context={
        'cho':food_choice,
        'posts':Post.objects.all()
    }
    return render(request,'kiloapp/menu.html',context)

def contact(request):
    return render(request,'kiloapp/contact.html')

def blog(request):
    return render(request,'kiloapp/some.html')
