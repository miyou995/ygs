from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'about.html')


def services(request):
    return render(request,'about.html')

def hiring(request):
    return render(request,'about.html')