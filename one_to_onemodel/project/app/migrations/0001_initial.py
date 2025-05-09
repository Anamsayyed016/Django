# Generated by Django 5.2 on 2025-04-29 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.ImageField(unique=True, upload_to='')),
                ('create_date', models.DateField()),
                ('created_by', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_contant', models.IntegerField()),
                ('aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.aadhar')),
            ],
        ),
    ]
