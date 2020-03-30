from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('account/', include('account.urls')),
    path('new_material/', include('addmaterial.urls')),
    path('loan/', include('loan.urls')),
]
