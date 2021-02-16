from django.urls import path
#from .views import PostListView,PostDetailView
from . import views

urlpatterns = [
    path('',views.view,name='cart'),
    path('mail/',views.mail,name='mail'),
#   path('<int:pk>/',views.update_cart,name='update_cart'),
 #  path('post/<int:pk>/', PostDetailView.as_view(),name='food-detail'),
    path('<int:id>/', views.update_cart, name='update_cart'),
     


    
]