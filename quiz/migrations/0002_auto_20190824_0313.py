# Generated by Django 2.2.4 on 2019-08-24 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='questions',
            new_name='author',
        ),
    ]
