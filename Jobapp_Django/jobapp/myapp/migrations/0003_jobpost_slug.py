# Generated by Django 4.1.4 on 2023-01-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_jobpost_date_jobpost_description_jobpost_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
