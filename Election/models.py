from django.db import models
from User_Login.models import UserProfile


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




class Vote(models.Model):
    voter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey('Candidate_Login.Candidate', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('voter', 'election')

    def __str__(self):
        return f"{self.voter} voted for {self.candidate} in {self.election}"