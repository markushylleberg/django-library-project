from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_material, name='add_material'),
]