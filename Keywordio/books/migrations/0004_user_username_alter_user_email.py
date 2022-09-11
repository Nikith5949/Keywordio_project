# Generated by Django 4.1.1 on 2022-09-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]