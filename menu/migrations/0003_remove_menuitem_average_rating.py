# Generated by Django 3.2.19 on 2023-06-25 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menuitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='average_rating',
        ),
    ]
