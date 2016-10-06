from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_bio = models.CharField(max_length=1000)

    def __str(self):
        return self.person_name + "\n bio: " + self.person_bio
