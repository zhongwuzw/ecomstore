from django.views.generic import TemplateView
from django.shortcuts import render

class FileNotFound404(TemplateView):
    def get(self,request,*args,**kwargs):
        page_title = 'Page Not Found'
        return render(request,'404.html',locals())