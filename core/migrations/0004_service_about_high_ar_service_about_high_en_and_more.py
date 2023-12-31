# Generated by Django 4.2.5 on 2023-10-01 11:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_hiring_service_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='about_high_ar',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text service'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_high_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text service'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_high_fr',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text service'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_ar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='service'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='service'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_fr',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='service'),
        ),
    ]
