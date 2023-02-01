from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.product_all, name='shop'),
]