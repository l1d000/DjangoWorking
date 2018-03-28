from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html

# Create your models here.
class BuildProject(models.Model):
    project_Name   = models.CharField(max_length=100)
#    build_Path   = models.CharField(max_length=100)
#    ssh_Name   = models.CharField(max_length=20)
#    ssh_Mirror   = models.CharField(max_length=50)
    sync_Command = models.CharField(max_length=100)
    export_Variables   = models.TextField()
    build_Command   = models.TextField()
    color_Code = models.CharField(max_length=6)
    def Project_Name(self):
        return format_html('<span style="color: #{0};">{1}</span>',
                           self.color_Code,self.project_Name)
    Project_Name.allow_tags = True

