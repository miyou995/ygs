from django.contrib import admin
from .models import Business
from django.utils.html import format_html




Business._meta.verbose_name = "Informations magasin"


@admin.register(Business)
class BusinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    def has_add_permission(self, request):
        business = Business.objects.all()
        if business.count() > 1:
            return False
        else: 
            return True