from django.urls import path
from shop import views

urlpatterns = [
    path('catalog/', views.catalog),
    path('catalog/<int:id>/', views.retrieve),
]