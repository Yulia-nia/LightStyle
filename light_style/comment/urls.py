from django.urls import path
from comment import views


urlpatterns = [
    path('create_comment/', views.create_comment),
]