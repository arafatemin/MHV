# Generated by Django 5.1 on 2024-08-17 12:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0013_alter_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='autism',
            name='description_ar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='description_tr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='finance_ar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='finance_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='finance_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='finance_tr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='title_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='autism',
            name='title_tr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subjectcontact',
            name='subject_ar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subjectcontact',
            name='subject_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subjectcontact',
            name='subject_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subjectcontact',
            name='subject_tr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]