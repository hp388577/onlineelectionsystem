# Generated by Django 4.2.1 on 2023-06-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate_Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]