import random

from django.db import transaction
from django.core.management.base import BaseCommand

from supershop.models import Product, Order, OrderProduct
from supershop.factories import (
    ProductFactory,
    OrderFactory,
    OrderProductFactory
)

NUM_PRODUCTS = 1000
NUM_ORDERS = 1000
NUM_ORDER_PRODUCT = 5000
MAX_QTY = 32

class Command(BaseCommand):
    help = "Создаем тестовые данные"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляем старые данные...")
        models = [OrderProduct, Order, Product]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Создаем данные...")

        products = []
        for _ in range(NUM_PRODUCTS):
            product = ProductFactory()
            products.append(product)

        orders = []
        for _ in range(NUM_ORDERS):
            order = OrderFactory()
            # TODO add at least 1 product
            orders.append(order)

        for _ in range(NUM_ORDER_PRODUCT):
            order = random.choice(orders)
            product = random.choice(products)

            # TODO quantities should have normal distribution, not linear
            quantity = random.randint(0, MAX_QTY)
            order_product = OrderProductFactory(order=order, 
                                                product=product,
                                                quantity=quantity)
