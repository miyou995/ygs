
from django.urls import path, re_path
from .views import index_view, about, contact, services, hiring
app_name = 'core'



urlpatterns = [
    path('', index_view, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
    path('hiring', hiring, name='hiring'),
]
