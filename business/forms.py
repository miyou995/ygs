from django import forms
from .models import Store


class MagasinModalForm(forms.ModelForm):
    class Meta:
        model = Store
        fields= ('name', 'address', 'is_default', 'phone')