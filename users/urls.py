from django.urls import path, include
from . import views


urlpatterns = [
    path('users', views.userCreate.as_view(), name='create'),
]