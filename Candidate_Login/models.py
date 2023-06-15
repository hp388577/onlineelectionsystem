from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    area_name = models.CharField(max_length=100)
    documents_image = models.ImageField(upload_to='documents/')
    token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_registered=models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    area_name = models.CharField(max_length=100)
    documents_image = models.ImageField(upload_to='documents/')
    symbol=models.ImageField(upload_to='documents/')
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
