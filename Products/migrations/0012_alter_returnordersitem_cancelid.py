# Generated by Django 3.2.6 on 2022-07-29 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_auto_20220729_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returnordersitem',
            name='cancelid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.returnallorders'),
        ),
    ]
