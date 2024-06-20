from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return (f'Username: {self.name}, '
                f'email: {self.email}, '
                f'age:{self.age}')


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return (f'Productname: {self.product_name}, '
                f'price: {self.price}, '
                f'description:{self.description}'
                f'image:{self.image}'
                )


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return (f'Ordercustomer: {self.customer}, '
                f'products: {self.products}, '
                f'date_ordered:{self.date_ordered}'
                f'total_price:{self.total_price}'
                )
