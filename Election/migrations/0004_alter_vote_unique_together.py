# Generated by Django 4.2.1 on 2023-06-16 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0003_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
    ]
