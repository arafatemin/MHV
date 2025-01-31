# Generated by Django 5.0.7 on 2024-08-15 16:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('comment', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('sub_message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('sub_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
