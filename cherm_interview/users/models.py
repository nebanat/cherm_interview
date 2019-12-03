from django.db import models
from django.db.utils import IntegrityError
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


USER_TYPE = [
    'interviewer',
    'candidate'
]


class CustomUser(AbstractUser):
    """
        base user class
        to be used for authentication
    """
    USER_TYPE = [
        ('interviewer', 'interviewer'),
        ('candidate', 'candidate')
    ]

    user_type = models.CharField(max_length=30, choices=USER_TYPE, default=USER_TYPE[1][0])

    def __str__(self):
        return "%s %s" % (self.user_type, self.email)


class Interviewer(models.Model):
    """
        models for interviewers
    """
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Candidate(models.Model):
    """
        models for candidates
    """
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance,  **kwargs):
    try:
        if instance.user_type == 'interviewer':
            Interviewer.objects.create(user=instance)
        elif instance.user_type == 'candidate':
            Candidate.objects.create(user=instance)
    except IntegrityError:
        pass  # use logging here
