# Generated by Django 4.1.1 on 2022-09-10 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_published',
        ),
    ]
