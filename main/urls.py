from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),

    # Users
    path('', include('users.urls')),
    path('chat/', include('chat.urls')),
]
