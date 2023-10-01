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