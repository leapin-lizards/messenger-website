# Generated by Django 5.1.2 on 2024-11-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('title', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
