from django.urls import path
from . import views
​
urlpatterns = [
    path('', views.index),
    path('mamago/', views.mamago),
    path('translated/', views.translated),
]