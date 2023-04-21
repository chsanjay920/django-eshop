from django.shortcuts import render , redirect , HttpResponseRedirect
from prateekstore.models.product import Products


def productdetailes(request):
    if request.method == 'POST':
        pid = request.POST.get('productid')
        product = Products.get_product_by_id(pid);
        print("product >")
        print(product[0].name);
        return render(request, 'productdetailes.html', {'product':product[0]});
    else:
        return render(request, 'base.html')


