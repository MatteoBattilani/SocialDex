# Generated by Django 4.0.1 on 2022-01-14 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLoginActivity',
        ),
    ]