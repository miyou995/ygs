
from django.urls import path, re_path
from .views import IndexView, AboutView, RecruitingView, ContactView, QuoteoView,  ServiceView, ServiceDetail

app_name = 'core'


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('services', ServiceView.as_view(), name='services'),
    path('about', AboutView.as_view(), name='about'),
    path('service_detail/<slug:slug>/', ServiceDetail.as_view(), name='service_detail'),
    path('hiring', RecruitingView.as_view(), name='hiring'),
    path('contact', ContactView.as_view(), name='contact'),
    path('quote', QuoteoView.as_view(), name='quote'),
]
