from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView
from catalog.models import Category,Product
from django.template.context import RequestContext
from catalog.forms import ProductAddToCartForm
from cart.cartbase import add_to_cart 
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect

class Index(TemplateView):
    template_name = 'index.html'
    
    def get(self,request,*args,**kwargs):
        page_title = 'Musical Instruments and Sheet Music for Musicians'
        print request
        return render(request,self.template_name,locals())
    
class ShowCategory(TemplateView):
    template_name = 'category.html'
    
    def get(self,request,*args,**kwargs):
        c = get_object_or_404(Category,slug = kwargs['category_slug'])
        products = c.product_set.filter(is_active = True)
        page_title = c.name
        meta_keywords = c.meta_keywords
        meta_description = c.meta_description
        return render(request,self.template_name,locals())
    
class ShowProduct(TemplateView):
    template_name = 'product.html'
    
    def get(self,request,*args,**kwargs):
        p = get_object_or_404(Product,slug = kwargs['product_slug'])
        categories = p.categories.filter(is_active = True)
        page_title = p.name
        meta_keywords = p.meta_keywords
        meta_description = p.meta_description
        form = ProductAddToCartForm(request,label_suffix = ':')
        form.fields['product_slug'].widget.attrs['value'] = kwargs['product_slug']
        request.session.set_test_cookie()
        return render(request,self.template_name,locals())
    
    def post(self,request,*args,**kwargs):
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request,postdata)
        if form.is_valid():
            add_to_cart(request)
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(reverse('show_cart'))
        form.fields['product_slug'].widget.attrs['value'] = kwargs['product_slug']
        request.session.set_test_cookie()
        return render(request,self.template_name,locals())