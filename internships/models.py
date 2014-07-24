from django.contrib.auth.models import User, Group
from django.db import models

class Applicant(models.Model):
    user = models.OneToOneField(User)

    email = models.EmailField(unique = True)
    groups = models.ManyToManyField(Group)


