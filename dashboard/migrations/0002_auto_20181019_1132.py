# Generated by Django 2.1.2 on 2018-10-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='adresse',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='adresse',
            field=models.CharField(max_length=50),
        ),
    ]