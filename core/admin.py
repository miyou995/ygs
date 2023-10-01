from django.contrib import admin
from core.models import  Service
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationAdmin



Service._meta.verbose_name = "content"



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    prepopulated_fields = {"slug": ("name",)}
    # exclude= ('name_fr','about_high_fr', 'about_low_fr')
    list_display_links = ('id','name')
    list_per_page = 40


