# Generated by Django 4.2.5 on 2023-09-21 09:06

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_business_address_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Nom de l'entreprise")),
                ('image_high', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_1')),
                ('image_low', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_2')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Titre')),
                ('about_high', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text a propos')),
                ('about_low', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Page a propos 2')),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'abouts',
            },
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Téléphone')),
                ('niveau', models.CharField(blank=True, choices=[('S1', 'Cycle Moyen'), ('S2', 'Niveau Secondaire'), ('S3', 'Niveau Terminal'), ('S4', 'Formation Professionnelle '), ('S5', 'Baccalauréat'), ('S6', 'Niveau Universitaire')], max_length=2, null=True, verbose_name="niveau d'étude")),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=150, null=True, verbose_name='lieu de naissance')),
                ('permis', models.BooleanField(default=False, verbose_name='Permis de Conduire ')),
                ('passeport', models.BooleanField(default=False, verbose_name='Passeport valide')),
                ('army', models.BooleanField(default=False, verbose_name='Service militaire')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Experience')),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='media', verbose_name='CV')),
            ],
            options={
                'verbose_name': 'hiring',
                'verbose_name_plural': 'hirings',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='service')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image du service')),
                ('image_high', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_detail_1')),
                ('image_low', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_detail_2')),
                ('about_high', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text service')),
                ('about_low', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Page service ')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='Slide haut de page')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': 'slide',
                'verbose_name_plural': 'slides',
            },
        ),
        migrations.AddField(
            model_name='business',
            name='phone3',
            field=models.CharField(blank=True, max_length=50, verbose_name="3eme numéro de téléphone de l'entreprise"),
        ),
        migrations.AlterField(
            model_name='business',
            name='conditions',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Conditions d utilisations'),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('entreprise', models.CharField(blank=True, max_length=150, null=True, verbose_name="Nom de l'entreprise")),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.service', verbose_name='service')),
            ],
            options={
                'verbose_name': 'quote',
                'verbose_name_plural': 'quotes',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nom')),
                ('entreprise', models.CharField(blank=True, max_length=150, null=True, verbose_name="Nom de l'entreprise")),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Téléphone')),
                ('subject', models.CharField(blank=True, max_length=150, null=True, verbose_name='sujet')),
                ('message', models.TextField(blank=True, null=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.service', verbose_name='service')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
