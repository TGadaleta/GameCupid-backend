# Generated by Django 5.1.5 on 2025-01-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('default', 'default'), ('he/him', 'he/him'), ('she/her', 'she/her'), ('they/them', 'they/them'), ('other', 'other')], default='default', max_length=20),
        ),
    ]
