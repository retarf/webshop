from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.api import ProductList

from api import api

namespace = 'api'

product_router = DefaultRouter()
product_router.register('products', ProductList, basename='product')

urlpatterns = [
        path('shop/', include(product_router.urls), name='products'),
        ]
