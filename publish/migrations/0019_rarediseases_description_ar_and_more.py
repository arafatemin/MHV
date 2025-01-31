# Generated by Django 5.1 on 2024-08-18 19:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0018_rarediseases'),
    ]

    operations = [
        migrations.AddField(
            model_name='rarediseases',
            name='description_ar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='description_tr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='finance_ar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='finance_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='finance_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='finance_tr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='startedDate_ar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='startedDate_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='startedDate_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='startedDate_tr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='title_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rarediseases',
            name='title_tr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
