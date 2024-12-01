from django.urls import path, include
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.register, name='reg'),
    ]