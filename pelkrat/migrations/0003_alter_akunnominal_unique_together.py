# Generated by Django 4.0.4 on 2022-05-28 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dakun', '0001_initial'),
        ('dkoperasi', '0003_alter_koperasi_options_alter_type_options'),
        ('pelkrat', '0002_alter_akunnominal_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='akunnominal',
            unique_together={('koperasi', 'akun')},
        ),
    ]