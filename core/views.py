from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')

# Create your views here.
def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'about.html')


def services_view(request):
    return render(request,'about.html')

def hiring_view(request):
    return render(request,'about.html')