# Generated by Django 5.2 on 2025-04-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_stu_dis'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Stu_contact',
            field=models.IntegerField(null=True),
        ),
    ]
