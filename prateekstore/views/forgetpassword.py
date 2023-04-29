from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from prateekstore.models.customer import Customer
from django.views import View

from django.contrib.auth.hashers import make_password


class Forgetpassword(View):
    return_url = None

    def get(self, request):
        Forgetpassword.return_url = request.GET.get('return_url')
        return render (request, 'changepassword.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        confirmpassword = request.POST.get('confirmpassword')
        print(email,make_password(password))
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if(password != confirmpassword):
            error_message = 'passwords should match !!'
            return render (request, 'changepassword.html', {'error': error_message})
        if customer:
            customer.change_password(email=email,password=make_password(password))
            return redirect ('homepage')
        else:
            error_message = 'Invalid Email !!'

        return render (request, 'changepassword.html', {'error': error_message})