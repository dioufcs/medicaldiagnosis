# Generated by Django 2.1.2 on 2018-11-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maladie',
            name='nomMaladie',
            field=models.CharField(max_length=254, verbose_name='Nom'),
        ),
    ]