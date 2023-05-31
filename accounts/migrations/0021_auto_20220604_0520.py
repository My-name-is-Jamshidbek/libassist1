# Generated by Django 3.2.12 on 2022-06-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_students_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='adadi',
            field=models.CharField(default=12, max_length=50, verbose_name='Адади'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='beti',
            field=models.CharField(default=1, max_length=50, verbose_name='Бети'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='city',
            field=models.CharField(default=1, max_length=50, verbose_name='Шахар номи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=1, max_length=50, verbose_name='ISBN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='money',
            field=models.CharField(default=1, max_length=25, verbose_name='Сумма'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='nameda',
            field=models.CharField(default=1, max_length=50, verbose_name='Номда'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='numberda',
            field=models.CharField(default=1, max_length=50, verbose_name='Сонда'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='organization',
            field=models.CharField(default=1, max_length=200, verbose_name='Тавсия қилган ташкилот'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publishing',
            field=models.CharField(default=1, max_length=100, verbose_name='Нашриёт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='section',
            field=models.CharField(default=1, max_length=50, verbose_name='Бўлими'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(default=1, max_length=50, verbose_name='Йили'),
            preserve_default=False,
        ),
    ]
