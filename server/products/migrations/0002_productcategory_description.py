# Generated by Django 2.2.2 on 2019-06-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание продукта'),
        ),
    ]
