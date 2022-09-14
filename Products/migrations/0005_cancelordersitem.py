# Generated by Django 3.2.6 on 2022-07-29 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_cancelallorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='cancelordersItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('producttotal', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='orderitem/')),
                ('size', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('cancelid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.cancelallorders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.addproduct')),
            ],
        ),
    ]
