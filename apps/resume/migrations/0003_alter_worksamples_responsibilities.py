# Generated by Django 3.2.4 on 2021-08-19 12:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_resumeuserdetails_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksamples',
            name='responsibilities',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
