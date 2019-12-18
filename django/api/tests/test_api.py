from django.test import TestCase, Client
from rest_framework import status

from shop.models import Product
from api.serializers import ProductSerializer

class GetAllProductsTest(TestCase):

    def setUp(self):
        Product.objects.create(
                name='TestProduct01',
                description='TestProduct01'
                )
        Product.objects.create(
                name='TestProduct02',
                description='TestProduct02'
                )

    def test_get_all_products(self):
        response = Client().get('/api/shop/products/')

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
