#coding=utf-8
import os
import time

class FileStruct():
    def __init__(self, name = ""):
        self.name = name
        self.data_dic = {}
        self.index = -1

    class Struct():
        def __init__(self, name, isdir, size, time):
            self.name = name
            self.isdir = isdir
            self.size = size
            self.time = time
    def make_struct(self,  name, isdir, size, time):
        return self.Struct( name, isdir, size, time)

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def get_FileSize(filePath):
#    filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

def get_FileModifyTime(filePath):
#    filePath = unicode(filePath,'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)

def print_simple_files(path):
    files = os.listdir(path)
    return files

def printFiles(path):
    print(path)
    filestruct = FileStruct()
    current = []

    files = os.listdir(path)
    files.sort(cmp=lambda x,y: cmp(x.lower(), y.lower()))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            current.append(filestruct.make_struct(f,1,get_FileSize(path),get_FileModifyTime(path)))

    for f in files:
        if(os.path.isdir(path + '/' + f)) == False:        
            current.append(filestruct.make_struct(f,0,get_FileSize(path),get_FileModifyTime(path)))
    return current



