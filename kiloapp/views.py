from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView



import requests
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
      

class PostDetailView(DetailView):
        model=Post



def menu(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'kiloapp/menu.html',context)

def contact(request):
    return render(request,'kiloapp/contact.html')

def blog(request):
    return render(request,'kiloapp/some.html')
