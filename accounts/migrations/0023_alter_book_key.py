# Generated by Django 3.2.12 on 2022-06-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20220604_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='key',
            field=models.CharField(default=1, max_length=25, verbose_name='Инвентар рақами'),
            preserve_default=False,
        ),
    ]