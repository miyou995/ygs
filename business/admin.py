from django.contrib import admin
from business.models import Business, Contact, Quote, Hiring, Slide, About, Service
from django.utils.html import format_html

from modeltranslation.admin import TranslationAdmin



Business._meta.verbose_name = "Informations "


@admin.register(Business)
class BusinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')

    def has_add_permission(self, request):
        business = Business.objects.all()
        if business.count() > 1:
            return False
        else: 
            return True
        
        
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    prepopulated_fields = {"slug": ("name",)}
    # exclude= ('name_fr','about_high_fr', 'about_low_fr')
    list_display_links = ('id','name')
    list_per_page = 40
admin.site.register(Service, ServiceAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude= ('name_fr','about_high_fr', 'about_low_fr', 'title_fr')
    list_display_links = ('id','name')
    list_per_page = 40
admin.site.register(About, AboutAdmin)


admin.site.register(Contact) 
admin.site.register(Quote) 
admin.site.register(Hiring) 
admin.site.register(Slide) 