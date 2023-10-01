from modeltranslation.translator import translator, TranslationOptions
from .models import Service
from .models import Hiring
from .models import Contact





class ServiceTranslationOptions(TranslationOptions):
     fields =('name','about_high')

translator.register(Service,ServiceTranslationOptions)



