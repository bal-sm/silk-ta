# Generated by Django 4.0.4 on 2022-05-28 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkoperasi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='koperasi',
            old_name='koperasi',
            new_name='name',
        ),
    ]
