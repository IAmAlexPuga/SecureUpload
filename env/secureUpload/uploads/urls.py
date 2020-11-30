from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='uploads-home'),
    path('upload/', views.upload, name='uploads-upload'),
]