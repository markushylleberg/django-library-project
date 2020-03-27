from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('books/', views.books, name='books'),
    path('magazines', views.magazines, name='magazines'),
    path('my_loans/', views.my_loans, name='my_loans'),
    path('expired_loans/', views.expired_loans, name='expired_loans'),
]