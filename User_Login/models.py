from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    area = models.CharField(max_length=100)
    eligible_to_vote = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
