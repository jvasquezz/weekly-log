from __future__ import unicode_literals

from django.db import models

# Create your models here.
class updateHours(models.Model):
    hours = models.TimeField()
    
    def __str__(self):
        self.hours


