from django.urls import path
from .views import hello, HelloView

urlpatterns = [
    path('hello/', hello, name='hello'),  # вызов функции
    path('hello2/', HelloView.as_view(), name='hello2'),  # вызов класса
]
