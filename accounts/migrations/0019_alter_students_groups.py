# Generated by Django 3.2.12 on 2022-06-04 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_students_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.group'),
        ),
    ]
