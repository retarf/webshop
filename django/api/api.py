from rest_framework import generics, viewsets
from api.serializers import ProductSerializer
from shop.models import Product

class ProductList(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
