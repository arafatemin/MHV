# Generated by Django 5.0.7 on 2024-08-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0011_alter_subjectcontact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
