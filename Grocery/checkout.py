from django.shortcuts import render,redirect


from Grocery.models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity :
            Cart.objects.delete(id=item.id)
            
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty
                    
    context={'cartitems': cartitems, 'total_price': total_price}
    return render(request, "Grocery/checkout.html", context)

