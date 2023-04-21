from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from prateekstore.models.customer import Customer
from django.views import View
from prateekstore.models.product import Products
from prateekstore.models.orders import Order
from prateekstore.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
