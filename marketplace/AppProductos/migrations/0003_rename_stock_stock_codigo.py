# Generated by Django 4.1.3 on 2022-12-13 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProductos', '0002_alter_productos_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='stock',
            new_name='codigo',
        ),
    ]
