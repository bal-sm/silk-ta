# Generated by Django 4.0.4 on 2022-06-10 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkoperasi', '0004_koperasiuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='koperasiuser',
            old_name='Koperasi',
            new_name='koperasi',
        ),
        migrations.RenameField(
            model_name='koperasiuser',
            old_name='user1',
            new_name='user',
        ),
    ]
