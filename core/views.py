from django.shortcuts import render
from django.utils.translation import *


def index_view(request):
    template_name =  'rtl/index.html' if request.LANGUAGE_CODE == 'ar' else 'index.html'
    return render(request,template_name)


def about(request):
    template_name =  'rtl/about.html' if request.LANGUAGE_CODE == 'ar' else 'about.html'
    return render(request,template_name)

def contact(request):
    template_name =  'rtl/contact.html' if request.LANGUAGE_CODE == 'ar' else 'contact.html'
    return render(request,template_name)

def services(request):
    template_name =  'rtl/services.html' if request.LANGUAGE_CODE == 'ar' else 'services.html'
    return render(request,template_name)

def hiring(request):
    template_name =  'rtl/hiring.html' if request.LANGUAGE_CODE == 'ar' else 'hiring.html'
    return render(request,template_name)

