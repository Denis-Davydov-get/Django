from django.urls import path
from .views import hello, my_view, orders, index, orders_user


urlpatterns = [
    path('', my_view, name='index'),
    path('hello/', hello, name='hello'),  # вызов функции
    path('index/', index, name='index'),  # вызов функции
    path('orders/', orders, name='orders'),  # вызов функции
    path('orders/<int:user_id>', orders_user, name='orders_user'),  # вызов функции
    # path('hello2/', HelloView.as_view(), name='hello2'),  # вызов класса
    # path('/<int:year>/', year_post, name='year_post'),

]
