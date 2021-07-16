from django.db import models
import datetime

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/menu/')

    @staticmethod
    def get_all_menus():
        return Menu.objects.all()

    def get_all_menus_by_categoryid(category_id):
        if category_id:
            return Menu.objects.filter(category=category_id)
        else:
            return Menu.get_all_menus()


class Order(models.Model):
    username=models.CharField(max_length=50, null=True, blank=True)
    productnameee = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(max_length=100, default='')
    QUANTITY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    quantity = models.CharField(
        max_length=5, choices=QUANTITY_CHOICES, default='1')
    address = models.CharField(max_length=50, default='')
    fullname = models.CharField(max_length=40, default='')
    detailaddress = models.TextField(max_length=100, default='')
    number = models.CharField(max_length=10, default='')
    altnum = models.CharField(max_length=10, default='')
    date = models.DateField(
        default=datetime.datetime.today, null=True, blank=True)
    time = models.TimeField(
        default=datetime.datetime.today, null=True, blank=True)

    def register(self):
        self.save()


