from django.urls import path
from products import views

urlpatterns = [
    path('catalog/', views.catalog),
    path('catalog/<int:id>/', views.retrieve),
]