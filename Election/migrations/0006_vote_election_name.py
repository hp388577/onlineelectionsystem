# Generated by Django 4.2.1 on 2023-06-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0005_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='election_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]