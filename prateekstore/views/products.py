from django.shortcuts import render , redirect , HttpResponseRedirect
from prateekstore.models.product import Products
from prateekstore.models.category import Category
from django.views import View


# Create your views here.
class ProductsList(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('cart')

    def get(self , request):
        return HttpResponseRedirect(f'/store2')

def store2(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None 
    products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = ""
    return render(request, 'products.html', data)


