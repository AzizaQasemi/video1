# import random
# from decimal import Decimal

# from django.core.management.base import BaseCommand
# # from django.contrib.auth.models import User
# from django.utils import lorem_ipsum
# from api.models import User, Product,Order, OrderItem

# class Command(BaseCommand):
#     help = "Creates application data"
    
#     def handle(self, *args, **kwargs):
#         user = User.objects.filter(username = 'admin').first()
#         if not user:
#             user = User.objects.create_superuser(username='admin')
            
#         products = [
#             Product(name='A Scanner Darkly', description=)
#             Product(name='A Scanner Darkly', description=)
#             Product(name='A Scanner Darkly', description=)
#             Product(name='A Scanner Darkly', description=)
#             Product(name='A Scanner Darkly', description=)
#             Product(name='A Scanner Darkly', description=)
#         ]
        
#         Product.objects.bulk_create(products)
#         products = Product.objects.all()
        
#         for _ in range(3):
#             order = Order.objects.create(user=user)
#             for product in random.sample(list(products), 2):
#                 OrderItem.objects.create(
#                     order=order, product=product, quantity=random
#                 )




import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from api.models import User, Product, Order, OrderItem


class Command(BaseCommand):
    help = "Creates application data"

    def handle(self, *args, **kwargs):
        user = User.objects.filter(username="admin").first()

        if not user:
            user = User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin12345",
            )

        product_data = [
            ("A Scanner Darkly", Decimal("19.99")),
            ("The Great Gatsby", Decimal("14.50")),
            ("1984", Decimal("12.99")),
            ("Pride and Prejudice", Decimal("16.75")),
            ("To Kill a Mockingbird", Decimal("18.25")),
            ("The Hobbit", Decimal("21.00")),
        ]

        for name, price in product_data:
            Product.objects.get_or_create(
                name=name,
                defaults={
                    "description": lorem_ipsum.paragraph(),
                    "price": price,
                    "stock": random.randint(1, 20),
                },
            )

        products = list(Product.objects.all())

        if len(products) < 2:
            self.stdout.write(
                self.style.ERROR("En az iki ürün gerekli.")
            )
            return

        for _ in range(3):
            order = Order.objects.create(user=user)

            for product in random.sample(products, 2):
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=random.randint(1, 5),
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Örnek ürünler ve siparişler başarıyla oluşturuldu."
            )
        )
