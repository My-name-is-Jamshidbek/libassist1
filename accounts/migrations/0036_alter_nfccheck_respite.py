# Generated by Django 4.0.6 on 2023-03-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_nfccheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfccheck',
            name='respite',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]