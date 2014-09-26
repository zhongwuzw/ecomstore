from django.conf.urls import patterns, include, url
from catalog.views import Index,ShowCategory,ShowProduct
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',Index.as_view(),name = 'catalog_home'),
    url(r'^category/(?P<category_slug>[-\w]+)/$',ShowCategory.as_view(),name = 'catalog_category'),
    url(r'product/(?P<product_slug>[-\w]+)/$',ShowProduct.as_view(),name = 'catalog_product'),
)
