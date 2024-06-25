import logging
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageForm
from myapp2.models import Product

logger = logging.getLogger(__name__)


# def add_image(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         message = 'Ошибка данных'
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             address = form.cleaned_data['address']
#             image_user = form.cleaned_data['image_user']
#             user = User(name=name, email=email, phone=phone, address=address, image_user=image_user)
#             user.save()
#             message = 'Пользователь сохранен'
#             # Делаем что-то с данными
#             logger.info(f'Получили {name=}, {email=}, {phone=}, {phone=}, {address=}')
#     else:
#         form = UserForm()
#         message = 'Заполните форму'
#     return render(request, 'myapp4/user_form.html', {'form': form})


def all_product(request):
    products = Product.objects.all()
    return render(request, 'myapp4/products.html', {"products": products})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/new_product.html', {'form': form})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                product_name=form.cleaned_data["product_name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                count_product=form.cleaned_data["count_product"],
                image_product=form.cleaned_data["image_product"],
            )
            fs = FileSystemStorage()
            fs.save(product.image_product.name, product.image_product)
            product.save()
            return render(request, 'myapp4/new_product.html', {'form': form}) 
    else:
        form = ProductForm()
    context = {"title": "Добавить товар", "form": form}
    return render(request, "myapp4/new_product.html", context)
