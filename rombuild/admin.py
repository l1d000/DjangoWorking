from django.contrib import admin
from rombuild.models import BuildProject
from django.forms import Textarea, TextInput
from django.db import models

class BuildProjectAdmin(admin.ModelAdmin):
    list_display = ('Project_Name', 'build_path')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':100})},
    }

admin.site.site_header = 'Working'
admin.site.site_title = 'Working' 

# Register your models here.
admin.site.register(BuildProject, BuildProjectAdmin)
