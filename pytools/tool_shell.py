#!/usr/bin/python
# coding:utf-8
import os
import sys
import time
import subprocess
import random
import re

sync_tmpfile =""

def shell_command_old(command):
    print("hello start"+command)
#    ps = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
#source cmd didn't work in sh. need to work in bash
    ps = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, shell=True,executable="/bin/bash")
    while ps.poll() is None:
        line = ps.stdout.readline()  
        line = line.strip()  
        if line:  
            print('Subprogram output: [{}]'.format(line))  
    print("hello end")   
    return "hello"


def shell_command(command):
    print("hello start"+command)
    global sync_tmpfile
    sync_tmpfile = "/tmp/%d.tmp" % random.randint(10000,99999)
    fpWrite = open(sync_tmpfile,'w')
    print(sync_tmpfile)
    ps = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=fpWrite, universal_newlines=True, shell=True,executable="/bin/bash")
    while True:
        fpRead = open(sync_tmpfile,'r')  
        lines = fpRead.readlines()
        for line in lines:
            print line
        if ps.poll():
            break;
        time.sleep(3)
  #  os.popen('rm -rf %s' % sync_tmpfile) 
    print 'finished'
    return "hello"     

def get_sync_total(path, grep_var):
    output=os.popen(' cat %s | grep -E "%s" '%(path,grep_var)).read().splitlines()
    if output:
        current_num = len(output)
    else:
        current_num = 0
    return current_num


def get_sync_current():
    total = 0
    if sync_tmpfile :
        total=get_sync_total(sync_tmpfile, "Fetching project")  
    print(total)
    return ((total*100/735))  
	
             
if __name__ == '__main__':
    shell_command("find -name *.txt")
   
