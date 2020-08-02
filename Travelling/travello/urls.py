from django.urls import path

from . import views

urlpatterns = [

     path('', views.index, name='home'),
     path('destination/<str:place2>/', views.destination1, name='destination')
     
]
