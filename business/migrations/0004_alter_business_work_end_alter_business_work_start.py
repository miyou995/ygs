# Generated by Django 4.2.5 on 2023-09-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_business_meta_description_business_meta_keyword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='work_end',
            field=models.TimeField(verbose_name='heure de fin '),
        ),
        migrations.AlterField(
            model_name='business',
            name='work_start',
            field=models.TimeField(verbose_name='heure de debut '),
        ),
    ]
