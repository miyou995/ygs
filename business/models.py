from django.db import models
from tinymce import models as tinymce_models
from django.utils.html import format_html
from django.core.exceptions import ValidationError
# Create your models here.
from django.db.models.signals import pre_init
from django.db.models import F
from django.urls import reverse
from django.utils.translation import gettext as _
from modeltranslation.translator import translator, TranslationOptions


CHOICES = (
    ('S1' ,'Cycle Moyen'),
    ('S2' ,'Niveau Secondaire'),
    ('S3' ,'Niveau Terminal'),
    ('S4' ,'Formation Professionnelle '),
    ('S5' ,'Baccalauréat'),
    ('S6' ,'Niveau Universitaire'),
)




class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(actif=True)


class Business(models.Model):
    name                = models.CharField(verbose_name="Nom de l'entreprise", max_length=100)
    logo                = models.ImageField(upload_to='images/logos', verbose_name='Logo', null=True, blank=True)
    logo_negatif        = models.ImageField(upload_to='images/slides', verbose_name="Logo négatif", null=True, blank=True)
    favicon             = models.ImageField(upload_to='images/logos', verbose_name='Favicon', null=True, blank=True)
    title               = models.CharField(verbose_name="Titre", max_length=50, blank=True)
    address             = models.CharField(verbose_name="Adresse", max_length=50, blank=True)
    address_link        = models.CharField(verbose_name="Lien maps ", max_length=50, blank=True)
    email               = models.EmailField(verbose_name="email de l'entreprise", max_length=50, blank=True)
    email2              = models.EmailField(verbose_name="2eme email de l'entreprise", max_length=50, blank=True)
    phone               = models.CharField(verbose_name="numéro de téléphone de l'entreprise", max_length=50, blank=True)
    phone2              = models.CharField(verbose_name="2eme numéro de téléphone de l'entreprise", max_length=50, blank=True)
    phone3               = models.CharField(verbose_name="3eme numéro de téléphone de l'entreprise", max_length=50, blank=True)
    work_start          = models.TimeField(verbose_name="heure de debut ")
    work_end            = models.TimeField(verbose_name="heure de fin ")
    about               = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    conditions          = tinymce_models.HTMLField(verbose_name='Conditions d utilisations', blank=True, null=True)
    mini_about          = models.TextField(verbose_name="Petit texte a propos de l'entreprise ( bas de page)", blank=True, null=True)
    facebook            = models.URLField(verbose_name="Lien page Facebook", max_length=300, blank=True, null=True)
    instagram           = models.URLField(verbose_name="Lien page Instagram", max_length=300, blank=True, null=True)
    tiktok              = models.URLField(verbose_name="Lien page Tiktok", max_length=300, blank=True, null=True)
    twitter             = models.URLField(verbose_name="Lien Compte Twitter (X)", max_length=300, blank=True, null=True)
    linkedin            = models.URLField(verbose_name="Lien Compte linkedin", max_length=300, blank=True, null=True)
    youtube             = models.URLField(verbose_name="Lien Chaine Youtube", max_length=300, blank=True, null=True)
    chat_code           = models.TextField(verbose_name="Script messagerie instantané", blank=True, null=True)
    pixel               = models.TextField(verbose_name="Script Facebook pixel", blank=True, null=True)
    analytics           = models.TextField(verbose_name="Script Analytics", blank=True, null=True)
    meta_title          = models.CharField(max_length=70, verbose_name="SEO title", blank=True, null=True)
    meta_description    = models.TextField(verbose_name="SEO description ", blank=True, null=True)
    meta_keyword        = models.CharField(max_length=150, verbose_name="SEO keywords", blank=True, null=True)  
    contact_message     = models.TextField(verbose_name="Contact message", blank=True, null=True)
    google_maps         = models.TextField(verbose_name="iframe google maps", blank=True, null=True)
    # actif  = models.BooleanField(verbose_name='Active', default=False)
    # is_big  = models.BooleanField(verbose_name='Grande photo (1920 x 570)', default=False)
    # is_small  = models.BooleanField(verbose_name='Medium photo (720 x 540)', default=False)

    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.logo.url))
    image_tag.allow_tags = True
    class Meta:
        verbose_name = '1- Infomation'
        verbose_name_plural = '1- Infomations'

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter une autre entreprise")

class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)

class Slide(models.Model):
    photo      = models.ImageField(verbose_name="Slide haut de page", upload_to='slides/' )
    actif  = models.BooleanField(verbose_name='actif', default=True)
    objects = ActiveManager()

    class Meta:
        verbose_name = 'slide'
        verbose_name_plural = 'slides'
    
  
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'autres Slides")


class About(models.Model):
    name            = models.CharField(verbose_name="Nom de l'entreprise", max_length=100,  blank=True, null=True)
    image_high      = models.ImageField(upload_to='images/', verbose_name='image_1', blank=True, null=True)
    image_low       = models.ImageField(upload_to='images/', verbose_name="image_2", blank=True, null=True)
    title           = models.CharField(verbose_name="Titre", max_length=50, blank=True) 
    about_high      = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    about_low       = tinymce_models.HTMLField(verbose_name='Page a propos 2', blank=True, null=True)
 
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


class Service(models.Model):
    name            = models.CharField(verbose_name="service", max_length=100,  blank=True, null=True)
    slug = models.SlugField()
    image           = models.ImageField(upload_to='images/', verbose_name='image du service', blank=True, null=True)
    image_high      = models.ImageField(upload_to='images/', verbose_name='image_detail_1', blank=True, null=True)
    image_low       = models.ImageField(upload_to='images/', verbose_name="image_detail_2", blank=True, null=True)
    about_high      = tinymce_models.HTMLField(verbose_name='Text service', blank=True, null=True)
    about_low       = tinymce_models.HTMLField(verbose_name='Page service ', blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def get_absolute_url(self):
        return reverse("core:service_detail", kwargs={"slug": self.slug})
    


class Contact(models.Model):
    name            = models.CharField(max_length=150, verbose_name='Nom', null=True, blank=True)
    entreprise      = models.CharField(max_length=150, verbose_name="Nom de l'entreprise", null=True, blank=True)
    email           = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    phone           = models.CharField(verbose_name="Téléphone" , max_length=25, null=True, blank=True)
    service         = models.ForeignKey(Service, verbose_name='service', null=True, blank=True, on_delete=models.CASCADE)
    subject         = models.CharField(max_length=150, verbose_name='sujet', null=True, blank=True)
    message         = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:contact", kwargs={"pk": self.pk})

   
class Hiring(models.Model):
    name        = models.CharField(max_length=150, verbose_name='Nom')
    email       = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25, null=True, blank=True)
    niveau      = models.CharField(choices=CHOICES,verbose_name="niveau d'étude", max_length=2, null=True, blank=True)
    birth_date  = models.DateField(null=True, blank=True) 
    birth_place = models.CharField(max_length=150, verbose_name='lieu de naissance', null=True, blank=True)
    permis      = models.BooleanField(verbose_name='Permis de Conduire ', default=False)
    passeport   = models.BooleanField(verbose_name='Passeport valide', default=False)
    army        = models.BooleanField(verbose_name='Service militaire', default=False)
    message     = models.TextField(verbose_name='Experience', null=True, blank=True)
    cv_file     = models.FileField(upload_to='media', verbose_name='CV', null=True, blank=True)

    class Meta:
        verbose_name = _("hiring")
        verbose_name_plural = _("hirings")
    
    def __str__(self):
        return str(self.email)
  

    def get_absolute_url(self):
        return reverse("core:hiring", kwargs={"pk": self.pk})



   
    
class Quote(models.Model):
    email       = models.EmailField(verbose_name="E-mail")
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25) 
    entreprise      = models.CharField(max_length=150, verbose_name="Nom de l'entreprise", null=True, blank=True)
    service         = models.ForeignKey(Service, verbose_name='service', null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("quote")
        verbose_name_plural = _("quotes")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("business:quote", kwargs={"pk": self.pk})
    
    def get_total_cost(self):
        return self.surface.price +  self.bien.price + self.formule.price