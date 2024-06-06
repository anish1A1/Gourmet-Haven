from django.urls import path

from Grocery import cart
from . import views 
from Grocery import checkout



urlpatterns = [
    path('', views.home, name='Grocery-Home' ),
    path('collections/', views.collections, name='collections'),
    path ('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),
    
    path('add-to-cart/', cart.addtocart, name='addtocart'),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart/', cart.updatecart, name="updatecart"),
    path('delete-cart-item/', cart.deletecartitem, name="deletecartitem"),
    path('checkout', checkout.index, name = 'checkout'),
                                                                                                                           
]
