# Generated by Django 3.2.6 on 2022-07-27 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allorders',
            name='shipped',
        ),
    ]
