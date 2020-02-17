"""
Definition of urls for GISearch.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.Search, name='search'),
    path('admin/', admin.site.urls),
]
