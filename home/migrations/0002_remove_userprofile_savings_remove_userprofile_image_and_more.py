# Generated by Django 4.0 on 2022-02-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Savings',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='income',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profession',
        ),
    ]
