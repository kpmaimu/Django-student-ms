# Generated by Django 3.2.15 on 2022-08-09 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_marks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marks',
            new_name='Mark',
        ),
    ]
