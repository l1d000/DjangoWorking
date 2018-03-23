# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from  pytools.tool_shell import shell_command, get_sync_current
from models import BuildProject
import threading
import time
import json
import re
import os

threadLock = threading.Lock()
running = False
current_name = ""
current_path = ""

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
    if current_name:
        return current_name
    else:
        return "/home/lidongzhou/HTC/work/Web/OceanLifeUHL_Asia_AU_O81_Mainline_Sense90A1_Stable_StockUI_MR/"

def rom_running(project_name):
    global current_name
    global current_path
    try:
        project_info = BuildProject.objects.filter(project_Name=project_name)
        if project_info:
            exe_cmd_list = " cd "+project_info[0].build_Path+";"
            exe_cmd_list += "rm  -rf "+project_info[0].project_Name+";"
            exe_cmd_list += "mkdir "+project_info[0].project_Name+";"
            exe_cmd_list += "cd "+project_info[0].project_Name+";"
            exe_cmd_list += project_info[0].sync_Command.replace("$ID", project_info[0].ssh_Name)\
                                                            .replace("$MIRROR", project_info[0].ssh_Mirror)
            exe_cmd_list += " ; repo sync -c;"
            exe_cmd_list += project_info[0].export_Variables
            exe_cmd_list += project_info[0].build_Command
            print(exe_cmd_list)
            current_name = project_info[0].project_Name
            current_path = project_info[0].build_Path+"/"+project_info[0].project_Name+"/out-log.txt"
            print(current_path)
            return True
            shell_thread = ShellThread(1, "Thread-Shell-Running", exe_cmd_list)
            shell_thread.start()
            return True
    except BuildProject.DoesNotExist:
            return False
    return False

def get_build_current(path, max_number):
    current_percent = 0
    with open(path, 'r') as f:
            for line in f:
                oneline = re.findall(r"[\d.]+%",line)
                if oneline:
                    string_line = re.findall(r"\[(.*?)\]",line)
                    if string_line:
                       string = re.findall(r"/(\d*)",string_line[0])
                       newint = int(oneline[0].strip("%"))
                       if int(string[0]) > max_number and newint> current_percent:
                           current_percent = newint
    return current_percent



def get_sync_progress(request):
    num = {}
    num["progressbar_s"] = get_sync_current()
    if os.path.exists(current_path):
        num["progressbar_b"] = get_build_current(current_path, 100000)
    else:
        num["progressbar_b"] = 0
    print(json.dumps(num))
    return HttpResponse(json.dumps(num))
