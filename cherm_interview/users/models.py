from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = [
    'interviewer',
    'candidate'
]


class CustomUser(AbstractUser):
    USER_TYPE = [
        ('interviewer', 'interviewer'),
        ('candidate', 'candidate')
    ]

    user_type = models.CharField(max_length=30, choices=USER_TYPE, default=USER_TYPE[1][0])

    def __str__(self):
        return "%s %s" % (self.user_type, self.email)
