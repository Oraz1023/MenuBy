from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='menu'),
    path('/<int:pk>/', menuby, name='menuby')
]
