# Generated by Django 4.2.1 on 2023-06-17 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0007_remove_vote_election_name'),
        ('Candidate_Login', '0003_participant_is_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='election_name',
            field=models.ManyToManyField(to='Election.election'),
        ),
    ]
