# Generated by Django 4.1.4 on 2022-12-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capital',
            name='id',
        ),
        migrations.AlterField(
            model_name='capital',
            name='country',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
