# Generated by Django 3.2.12 on 2022-06-06 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_book_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return_book',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.students'),
        ),
    ]
