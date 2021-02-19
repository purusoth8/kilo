from django.urls import path
#from .views import PostListView,PostDetailView
from . import views

urlpatterns = [
    path('',views.view,name='cart'),
    path('mail/',views.email_one,name='email_one'),
    path('mailth/',views.mailth,name='mainth'),
#   
#   path('<int:pk>/',views.update_cart,name='update_cart'),
 #  path('post/<int:pk>/', PostDetailView.as_view(),name='food-detail'),
    path('<int:id>/', views.update_cart, name='update_cart'),
     


    
]