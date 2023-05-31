# Generated by Django 4.2.1 on 2023-05-31 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_remove_accept_book_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept_book',
            name='key',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='key',
            field=models.CharField(max_length=25, unique=True, verbose_name='Инвентар рақами'),
        ),
        migrations.AlterField(
            model_name='check',
            name='key',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='nfccheck',
            name='key',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='return_book',
            name='key',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]