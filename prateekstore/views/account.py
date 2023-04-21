from django.shortcuts import render
from django.views import View

from prateekstore.models.customer import Customer


class Account(View):
    def get(self, request):
        useremail = request.session['user']
        customer = Customer.get_customer_by_email (useremail)
        print(customer.email)
        data = {
            "email":customer.email,
            "firstname":customer.first_name,
            "lastname":customer.last_name,
            "phonenumber":customer.phone,
        }
        return render (request, 'account.html',data)