# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
import threading
import time
import json
from  pytools.tool_shell import shell_command, get_sync_current
from models import BuildProject

threadLock = threading.Lock()
running = False
current_name = ""

class ShellThread (threading.Thread):
    def __init__(self, threadID, name, cmds):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cmds = cmds
    def run(self):
        print "Starting " + self.name
        global running
        running = True
        threadLock.acquire()
        shell_run(self.name, self.cmds)
        threadLock.release()
        running = False 

def shell_run(threadName, cmds):
    shell_command(cmds)

def get_running_status():
    global running
    return running

def get_running_project():
    return current_name

def rom_running(project_name):
    global current_name
    try:
        project_info = BuildProject.objects.filter(project_Name=project_name)
        if project_info:
            exe_cmd_list = " cd "+project_info[0].build_Path+";"
    #            exe_cmd_list += "rm  -rf "+project_info[0].project_Name+";"
    #            exe_cmd_list += "mkdir "+project_info[0].project_Name+";"
            exe_cmd_list += "cd "+project_info[0].project_Name+";"
    #            exe_cmd_list += project_info[0].sync_Command.replace("$ID", project_info[0].ssh_Name)\
    #                                                        .replace("$MIRROR", project_info[0].ssh_Mirror)
    #            exe_cmd_list += " ; repo sync -c;"
            exe_cmd_list += project_info[0].export_Variables
            exe_cmd_list += project_info[0].build_Command
            print(exe_cmd_list)
            current_name = project_info[0].project_Name
            shell_thread = ShellThread(1, "Thread-Shell-Running", exe_cmd_list)
            shell_thread.start()  
            return True
    except BuildProject.DoesNotExist: 
            return False
    return False
    


def get_sync_progress(request):
    num = get_sync_current()
#    print(num)
    return HttpResponse(json.dumps(num))
