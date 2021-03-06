"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/<word>/', views.ispal),
    path('isbirth/', views.isbirth),
    path('template_language/', views.template_language),
    path('Circle/<int:r>/', views.Circle),
    path('myself/<name>/<int:age>/', views.myself),
    path('mur/<int:num1>/<int:num2>/', views.mur),
    path('hello/<name>/<int:age>/', views.hello),
    path('img/', views.img),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
