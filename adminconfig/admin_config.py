# -*- coding: utf-8 -*-
from adminconfig.models import AdminConfig

def get_current_path():
    adminconfig = AdminConfig.objects.filter(ConfigName="BuildPath")
    if adminconfig:
        print(adminconfig[0].Parameter)
        return adminconfig[0].Parameter

def get_current_ssh_name():
    adminconfig = AdminConfig.objects.filter(ConfigName="SshName")
    if adminconfig:
        print(adminconfig[0].Parameter)
        return adminconfig[0].Parameter

def get_current_ssh_mirror():
    adminconfig = AdminConfig.objects.filter(ConfigName="SshMirror")
    if adminconfig:
        print(adminconfig[0].Parameter)
        return adminconfig[0].Parameter
