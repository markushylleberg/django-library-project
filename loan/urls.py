from django.urls import path, include

from . import views

urlpatterns = [
    path('new_loan/', views.new_loan, name='new_loan'),
    path('return_loan/', views.return_loan, name='return_loan'),
]