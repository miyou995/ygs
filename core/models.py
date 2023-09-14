from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name  = models.CharField('Name', max_length=100)
    phone = models.CharField('Name', max_length=100)