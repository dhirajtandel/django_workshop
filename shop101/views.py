from django.shortcuts import render, HttpResponse
from shop101.models import Product

# Create your views here.

def test(request):
    return HttpResponse ('Hello world')

def product(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products_list.html',
                  context={'product_list': products})

def show_product(request,id):
    p_id = id
    product= Product.objects.get(id=p_id)
    return render (request, 'products_show.html', context={'product' : product})