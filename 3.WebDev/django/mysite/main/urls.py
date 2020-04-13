from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='index'),
    path('master/',views.master,name='master'),
    path('carpool/',views.carpool,name='carpool'),
    path('test/',views.test,name='test')
]