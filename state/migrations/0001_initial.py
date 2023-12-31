# Generated by Django 4.2.2 on 2023-06-12 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('nom', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(50)])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(99)])),
                ('genre', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], max_length=5)),
                ('image', models.ImageField(default='img/avatar-default.png', upload_to='img/', validators=[django.core.validators.FileExtensionValidator(['JPEG', 'JPG', 'PNG', 'WEBP'])])),
                ('pays', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='state.state')),
            ],
        ),
    ]
