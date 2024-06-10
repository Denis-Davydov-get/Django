import logging

from django.urls import path
from . import views

logger = logging.getLogger(__name__)

urlpatterns =[
    path('', views.home, name= 'home'),
    path('coin/', views.coin, name='coin'),
    path('random_roll', views.random_roll, name='random_roll'),
    path('random_number', views.random_number, name=' random_number'),
]
