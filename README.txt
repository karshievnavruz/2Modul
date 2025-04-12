OLCHA.UZ USLUBIDAGI MINI MAHSULOT SAYTI

1. Django project oching va 'shop' appini qo'shing:
    django-admin startproject olcha_clone
    cd olcha_clone
    python manage.py startapp shop

2. settings.py:
    - 'shop' ni INSTALLED_APPS ga qo'shing
    - MEDIA_URL = '/media/'
      MEDIA_ROOT = BASE_DIR / 'media'

3. urls.py (project darajasida):
    from django.conf import settings
    from django.conf.urls.static import static
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('shop.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

4. Admin paneldan mahsulotlar kiriting, va ularni ko'rish uchun localhost:8000 ga kiring.

Tayyor!
