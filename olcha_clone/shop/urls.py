# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # mahsulotlar ro'yxati
    path('<int:id>/', views.product_detail, name='product_detail'),  # har bir mahsulotning detali
]
