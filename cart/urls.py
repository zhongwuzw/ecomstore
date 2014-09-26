from django.conf.urls import patterns, include, url
from django.contrib import admin
from cart.views import ShowCart
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',ShowCart.as_view(),name = 'show_cart'),
)
