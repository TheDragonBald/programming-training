from django.urls import path

from . import views

urlpatterns = [
    path('requests/', views.request_list, name='request_list'),
    path('requests/create/', views.request_create, name='request_create'),
]