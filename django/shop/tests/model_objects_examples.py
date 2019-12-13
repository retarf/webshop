from shop.models import Product

n = 20


def add_products(n):
    for i in range(n):
        name = 'product{0}'.format(str(i))
        Product.objects.create(
                name=name,
                description=name
                )
