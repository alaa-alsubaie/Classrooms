# Generated by Django 2.0.6 on 2018-12-16 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_auto_20181216_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]