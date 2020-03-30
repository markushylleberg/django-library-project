from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish_material, name='publish_material'),
    path('register_material/', views.register_material, name='register_material'),
]