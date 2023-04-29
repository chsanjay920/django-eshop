from django.contrib import admin
from django.urls import path
from prateekstore.views.about import About
from prateekstore.views.account import Account
from prateekstore.views.forgetpassword import Forgetpassword
from prateekstore.views.success import Success

from .views.contact import Contact
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.products import ProductsList, store2
from .views.productdetailes import productdetailes

from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),

    path('store2', store2, name="store2"),
    path('products', ProductsList.as_view(), name='products'),
    
    path('productdetailes', productdetailes, name='productdetailes'),
    path('about', About.as_view(), name='about'),
     path('success', Success.as_view(), name='success'),
    path('support', Contact.as_view(), name='support'),
    path('account', Account.as_view(), name='account'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('forgetpassword', Forgetpassword.as_view(), name='forgetpassword'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
