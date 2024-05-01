# expense/urls.py (project-level)

from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),  # Include URLs from firstapp
]
