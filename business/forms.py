from django import forms
from django.forms import ModelForm
from .models import Contact,  Quote, Hiring
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError



class ContactForm(ModelForm) :
    username = forms.CharField(required=False)

    class Meta: 
        model = Contact 
        fields = '__all__' 
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username:
            raise ValidationError(
                    "BAD BOT"
                )

class QuoteForm(ModelForm) :
    username = forms.CharField(required=False)
    class Meta: 
        model = Quote 
        fields = '__all__' 
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username:
            raise ValidationError(
                    "BAD BOT"
                )

class HiringForm(ModelForm) :
    username = forms.CharField(required=False)
    class Meta: 
        model = Hiring 
        fields = '__all__' 
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username:
            raise ValidationError(
                    "BAD BOT"
                )   
    