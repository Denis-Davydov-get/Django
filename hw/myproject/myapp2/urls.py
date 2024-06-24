from django.urls import path
from .views import index, orders


urlpatterns = [
    path('', index, name='index'),
    path('orders/', orders, name='orders'),
    path('orders/<int:client_id>', orders, name='orders'),

]
