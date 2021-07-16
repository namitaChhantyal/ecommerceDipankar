from django.contrib import admin
from . import models
from .models import Product
from .models import Menu
from .models import Category
from .models import Order



# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['name','price']

admin.site.register(Product,AdminProduct)

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Category,AdminCategory)

class AdminMenu(admin.ModelAdmin):
    list_display=['name','price','description','category']

admin.site.register(Menu,AdminMenu)


class AdminOrder(admin.ModelAdmin):
    list_display=['username','productnameee','note','quantity','address','fullname','number','altnum','date','time']
admin.site.register(Order,AdminOrder)


