from django.urls import path

from . import views

namespace = 'shop'

urlpatterns = [
        path('products/', views.ProductListView.as_view(), name='products'),
        path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
        ]
