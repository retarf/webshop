from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):

    def setUp(self):
        Product.objects.create(
                name='TestProduct1',
                description='Description TestProduct1'
                )
        Product.objects.create(
                name='TestProduct2',
                description='Description TestProduct2'
                )

    def test_product_description(self):
        product1 = Product.objects.get(name='TestProduct1')
        product2 = Product.objects.get(name='TestProduct2')
        self.assertEqual(product1.description, 'description TestProduct1')
        self.assertEqual(product2.description, 'description TestProduct2')
                
