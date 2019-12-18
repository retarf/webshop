from django.urls import path
from rest_framework.routers import DefaultRouter
from api.api import ProductList

from api import api

namespace = 'api'

urlpatterns = []

product_router = DefaultRouter()
product_router.register('products', ProductList, basename='product')
urlpatterns += product_router.urls


