
from django.urls import path, re_path
from .views import index_view, about_view, contact_view, services_view, hiring_view
app_name = 'core'
urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about_view'),
    path('contact', contact_view, name='contact_view'),
    path('services', services_view, name='services_view'),
    path('hiring', hiring_view, name='hiring_view'),

]
