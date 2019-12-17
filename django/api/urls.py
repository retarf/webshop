from django.urls import path

from api import api

namespace = 'api'

urlpatterns = [
        path('products', api.ProductList.as_view()),
        ]

