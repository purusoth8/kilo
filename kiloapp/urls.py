from django.urls import path
from .views import PostListView,PostDetailView
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('menu/',views.menu,name='menu'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('catering/',views.res,name='catering'),
    
    path('post/<int:pk>/', PostDetailView.as_view(),name='food-detail'),

    
]