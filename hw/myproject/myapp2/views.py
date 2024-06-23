from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myapp2.models import Order, User


def hello(request):
    return HttpResponse("Hello World from function!")


# def year_month_date_post(request, year, month, date):
#     text = ""
#     pass  # формируем статьи за год, месяц, день
#     return HttpResponse(f"Posts from {year}/{month}/{date}<br>{text}")


def my_view(request):
    context = {"name": "Denis"}
    return render(request, "myapp2/base.html", context)


def index(request):
    return render(request, "myapp2/index.html")


def orders(request):
    orders = Order.objects.all()
    return render(request, "myapp2/orders.html", {'orders': orders})


def orders_user(request, user_id):
    orders = get_object_or_404(Order, pk=user_id)
    user = User.objects.filter(user=user_id).order_by('-date_ordered')
    return render(request, 'myapp2/orders.html',
                  {'author': user, 'orders': orders})
