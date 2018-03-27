from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AdminConfig(models.Model):
    ConfigName   = models.CharField(max_length=100)
    Parameter  = models.CharField(max_length=100)
