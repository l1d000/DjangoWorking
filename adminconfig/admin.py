from django.contrib import admin
from adminconfig.models import AdminConfig

class AdminConfigAdmin(admin.ModelAdmin):
    list_display = ('buildpath',)
#    fieldsets = (
#        ['Admin Configs',{
#            'fields':('buildpath'),
#        }],

#    )
 
admin.site.register(AdminConfig, AdminConfigAdmin)

# Register your models here.
