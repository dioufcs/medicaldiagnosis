# Generated by Django 2.1.2 on 2018-12-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20181111_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='situationMatr',
            field=models.CharField(max_length=50, verbose_name='Situation Matrimoniale'),
        ),
    ]
