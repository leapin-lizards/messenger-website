# Generated by Django 5.1.2 on 2024-11-03 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='title',
            new_name='name',
        ),
    ]
