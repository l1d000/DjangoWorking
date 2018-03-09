# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
import threading
import time
import json
from  pytools.tool_shell import shell_command
from models import BuildProject
 
#class PrintThread(threading.Thread):
#    def run(self):
#        sync_rom.sync_rom("","/home/lidongzhou/HTC/work/Web")


def search_post(request):
    ctx ={}
    if request.POST:
#        ctx['rlt'] = request.POST['url']
        print(request.POST['project_name'])
        print(request.POST['cl_number'])
        try:
            project_info = BuildProject.objects.filter(project_name=request.POST['project_name'])
            exe_cmd_list = "cd "+project_info[0].build_path+";"+"mkdir "+project_info[0].project_name+";"
            shell_command(exe_cmd_list)
            for i in project_info:
                print(i.build_path)   
         	#print(BuildProject.objects.get(project_name=request.POST['project_name']))
            print("have")
        except BuildProject.DoesNotExist: 
            print("null")
#        prints = PrintThread()
#        prints.start()
    return render(request, "sync.html", ctx)

