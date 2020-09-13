from django.urls import path, include
from . import views


urlpatterns = [
    path('create', views.userCreate.as_view(), name='create'),
]