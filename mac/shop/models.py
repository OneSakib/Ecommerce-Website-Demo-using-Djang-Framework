from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    product_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)
    c_email = models.CharField(max_length=100, default="name@name.domain")
    c_phone = models.CharField(max_length=50, default='123')
    c_desc = models.CharField(max_length=1000, default="No Description")

    def __str__(self):
        return self.c_name


# crete Database Entry for Orders
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    json_item = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, default="name@name.domain")
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=300)
    phone = models.IntegerField()
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + " ......"
