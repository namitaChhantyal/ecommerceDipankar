from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import Signupform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import models
from .models import Product
from .models import Menu
from .models import Category
from .models import Order

from django.contrib.auth.decorators import login_required


def index(request):
    prds = Product.get_all_products()
    # print(products)
    return render(request, 'index.html', {'products': prds})


def menulistt(request):
    m = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if(categoryID):
        m = Menu.get_all_menus_by_categoryid(categoryID)
    else:
        m = Menu.get_all_menus()
    data = {}
    data['menus'] = m
    data['categories'] = categories
    return render(request, 'menulistt.html', data)


def loginPage(request):
    if request.user.is_authenticated:
        request.session['username'] = user
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # request.session.set_expiry(86400)
                login(request, user)

                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'login.html')

        return render(request, 'login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = Signupform()
        if request.method == 'POST':
            form = Signupform(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def location(request):
    return render(request, 'location.html')

# def chartdata(request):
#     return render(request, 'chartdata.html')


@login_required(login_url='login')
def order(request):
    if request.method == 'POST':
        postDate = request.POST
        username=postDate.get('username')
        productnameee = postDate.get('productnameee')
        note = postDate.get('note')
        quantity = postDate.get('quantity')
        address = postDate.get('address')
        fullname = postDate.get('fullname')
        detailaddress = postDate.get('detailaddress')
        number = postDate.get('number')
        altnum = postDate.get('altnum')
        date = postDate.get('date')
        time = postDate.get('time')

        order_info = Order(username=username,productnameee=productnameee, note=note, address=address,
                           quantity=quantity,
                           fullname=fullname, detailaddress=detailaddress, number=number,
                           altnum=altnum, date=date, time=time)
        order_info.register()
        return render(request, 'thankyou.html')

    else:
        return render(request, 'order.html')
