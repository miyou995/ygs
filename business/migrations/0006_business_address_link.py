# Generated by Django 4.2.5 on 2023-09-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_rename_insta_business_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='address_link',
            field=models.CharField(blank=True, max_length=50, verbose_name='Lien maps '),
        ),
    ]
