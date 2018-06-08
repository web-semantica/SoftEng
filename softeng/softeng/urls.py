"""
softeng URL Configuration
The 'urlpatterns' list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("query.urls")),
]
