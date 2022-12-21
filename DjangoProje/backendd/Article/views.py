from django.shortcuts import render,get_object_or_404
from .models import Product,Category 
# Create your views here.


def index(request):
   return render(request,"index.html")


def shopcart(request):
    return render(request,"shopcart.html")

def categories(request):
    return {
        'categories' : Category.objects.all()
    }
   
def products(request):
    return {
        'products' : Product.objects.all()
    }
    
def product_details(request, slug):
    product = get_object_or_404(Product ,slug = slug, in_stock = True)
    return render(request, 'user/details.html', {'products' : product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug =  category_slug)
    products = Product.objects.filter( category = category)
    return render(request, 'product/category.html', context = {'category':category, 'products' : products})