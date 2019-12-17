from rest_framework import generics
from api.serializers import ProductSerializer
from shop.models import Product

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
