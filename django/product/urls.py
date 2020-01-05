from django.urls import path

from . import views

namespace = 'product'

urlpatterns = [
        path('', views.ProductListView.as_view(), name='products'),
        path('<int:pk>/', views.ProductDetailView.as_view(), name='product'),
        ]
