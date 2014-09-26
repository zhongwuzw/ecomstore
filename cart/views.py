from django.shortcuts import render
from django.views.generic import TemplateView
from cart.cartbase import get_cart_items,cart_distinct_item_count,remove_from_cart,get_cart_subtotal,update_cart
from django.contrib.auth.views import login

class ShowCart(TemplateView):
    template_name = 'cart/cart.html'
    
    def get(self,request,*args,**kwargs):
        cart_items = get_cart_items(request)
        cart_item_count = cart_distinct_item_count(request)
        page_title = 'Shopping Cart'
        return render(request,self.template_name,locals())
    
    def post(self,request,*args,**kwargs):
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            remove_from_cart(request)
        if postdata['submit'] == 'Update':
            update_cart(request)
        cart_items = get_cart_items(request)
        page_title = 'Shopping Cart'
        cart_subtotal = get_cart_subtotal(request)
        return render(request,self.template_name,locals())

