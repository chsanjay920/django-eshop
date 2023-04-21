from django.shortcuts import render , redirect , HttpResponseRedirect
from prateekstore.models.product import Products
from prateekstore.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

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
        return redirect('products')



    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    OtherProducts = None
    PopularProducts = None
    OtherProducts = Products.get_other_Products();
    PopularProducts = Products.get_Popular_Products();

    data = {}
    data['OtherProducts'] = OtherProducts
    data['PopularProducts'] = PopularProducts

    return render(request, 'index.html', data)


