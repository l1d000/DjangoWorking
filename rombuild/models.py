from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html

# Create your models here.
class BuildProject(models.Model):
    project_name   = models.CharField(max_length=100)
    build_path   = models.CharField(max_length=100)
    sync_command = models.CharField(max_length=100)
    export_variables   = models.TextField()
    build_command   = models.TextField()
    color_code = models.CharField(max_length=6)
    def Project_Name(self):
        return format_html('<span style="color: #{0};">{1}</span>',
                           self.color_code,self.project_name)
    Project_Name.allow_tags = True

