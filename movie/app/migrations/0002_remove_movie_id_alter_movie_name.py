# Generated by Django 5.0 on 2024-02-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
