from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AdminConfig(models.Model):
    buildpath   = models.CharField(max_length=100)
