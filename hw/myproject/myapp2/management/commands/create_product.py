from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        bottle_of_water = Product(product_name='bottle_of_water',
                                  price=2.5,
                                  description="bottle_of_water",
                                  image=None)
        bottle_of_water.save()
        self.stdout.write(f'{bottle_of_water}')
