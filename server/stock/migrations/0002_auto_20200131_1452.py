# Generated by Django 3.0.2 on 2020-01-31 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='qauntity',
            new_name='quantity',
        ),
    ]
