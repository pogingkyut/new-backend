from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('lists/', views.listview),
    path('lists/add/', views.listadd),
    path('lists/<str:id>/', views.listdetail),
    path('lists/update/<str:id>/', views.listupdate),
    path('lists/delete/<str:id>/', views.listdelete),
]