from django.core.management.base import BaseCommand
from myapp2.models import Order


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        order = Order(customer='', products='', total_price=None)
        order.save()
        self.stdout.write(f'{order}')
