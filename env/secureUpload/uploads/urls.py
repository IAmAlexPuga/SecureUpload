from django.urls import path
from .views import FileListView, FileDetailView, FileCreateView
from . import views

urlpatterns = [
    path('', FileListView.as_view(), name='uploads-home'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='uploads-detail'),
    path('file/new/', FileCreateView.as_view(), name='uploads-new'),
    #path('upload/', views.upload, name='uploads-upload'),
]


#path('upload/', views.upload, name='uploads-upload'),