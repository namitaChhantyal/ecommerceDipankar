from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),

    path('signup/',views.signup,name='signup'),
    path('location/',views.location,name='location'),
    path('menu/',views.menulistt,name='menulistt'),
    path('order/',views.order,name='order'),
    # path('chartdata/',views.chartdata,name='chartdata'),

   

]