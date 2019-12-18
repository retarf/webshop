from django.urls import path

from . import views

namespace = 'shop'

urlpatterns = [
        path('products', views.ProductListView.as_view(), name='products'),
        ]
