# Generated by Django 4.0.6 on 2023-03-12 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_students_nfcid'),
    ]

    operations = [
        migrations.CreateModel(
            name='NfcCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(max_length=100, verbose_name='Bergan odam nomi')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('book_name', models.CharField(max_length=50, verbose_name='Kitob nomi')),
                ('author', models.CharField(max_length=100, verbose_name='Муаллифи')),
                ('key', models.CharField(max_length=25)),
                ('respite', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('checker', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nfc_check', to='accounts.students')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
