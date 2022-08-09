# Generated by Django 3.2.15 on 2022-08-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_num', models.IntegerField()),
                ('english', models.CharField(blank=True, default='', max_length=100)),
                ('maths', models.CharField(blank=True, default='', max_length=100)),
                ('physics', models.CharField(blank=True, default='', max_length=100)),
                ('cs', models.CharField(blank=True, default='', max_length=100)),
                ('chemistry', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
