# olcha_clone/urls.py
from django.contrib import admin
from django.urls import path, include  # include ni import qildik

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('shop.urls')),  # shop app uchun URL-larni qo'shamiz
]
