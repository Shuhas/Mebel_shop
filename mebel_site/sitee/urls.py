from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog'),
    path('product/', product, name='product'),
]