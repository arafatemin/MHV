# Generated by Django 5.1 on 2024-08-24 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0026_honoursawards_description_ar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='books',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='books',
            name='image3',
        ),
    ]