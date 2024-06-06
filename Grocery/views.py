# from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


    
def home(request):
    print('user', request.user.username)
    grocery_category = Category.objects.get(slug='Grocery Items')
    grocery_category = grocery_category.product_set.all()
    context = {
        'grocery_category': grocery_category
    }
    return render(request, 'Grocery/homePage.html', context)


def collections(request):
    category = Category.objects.filter(status=0)        #from models.py using Category class, status = 0 means product is visible if 1 then product is not visible
    context = {'category' : category}
    return render(request, 'Grocery/collections.html', context)

def collectionsview(request, slug):
    category = Category.objects.filter(slug=slug, status=0).first()
    if category:
        products = Product.objects.filter(category__slug=slug)
        context = {'products': products, 'category': category}  # Pass category to the context
        return render(request, 'Grocery/items.html', context)
    else:
        messages.warning(request, 'No such category found')
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):   #checking if the product is found or not
            products = Product.objects.filter(slug=prod_slug, status=0).first  #fetching the data in products varable, it will store the product data in the products variable 
            context = {'products': products}     # adding data in the context
        else:
            messages.error(request, 'No such category')
            return redirect('collections')  
    else:
        messages.error(request, 'No such category')
        return redirect('collections')                
    
    return render(request, "Grocery/proddetails.html", context)    
