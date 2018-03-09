#!/usr/bin/python
# coding:utf-8
import os
import sys
import time
import subprocess

def shell_command(command):
    print("hello start"+command)
    ps = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    while ps.poll() is None:
        line = ps.stdout.readline()  
        line = line.strip()  
        if line:  
            print('Subprogram output: [{}]'.format(line))  
    print("hello end")   
    return "hello"


	
             
if __name__ == '__main__':
    shell_command("find -name *.txt")
   
