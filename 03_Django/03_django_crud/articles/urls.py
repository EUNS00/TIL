from django.urls import path
from . import views

#6.
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]