from django.urls import path
from comment import views


urlpatterns = [
    path('', views.all),
    path('create/', views.create),
    path('<int:id>/delete/', views.delete),
    path('<int:id>/', views.retrieve),
    path('<int:id>/edit/', views.edit),
]
