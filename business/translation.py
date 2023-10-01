from modeltranslation.translator import register, TranslationOptions

from .models import Business



@register(Business)
class BusinessTranslationOptions(TranslationOptions):
     fields =('name', 'title', 'address', 'about', 'meta_title', 'meta_description'  )

# translator.register(Business,BusinessTranslationOptions)




