from django.db import models

class Election(models.Model):
    election_name = models.CharField(max_length=100, primary_key=True)
    election_description = models.TextField()
    participant_due_date = models.DateField()
    election_start_date = models.DateTimeField()
    election_end_date = models.DateTimeField()
    election_result_date = models.DateField()
    result = models.JSONField()
    registration_close = models.BooleanField(default=False)
    area = models.ManyToManyField('Area')

    def __str__(self):
        return self.election_name


class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
