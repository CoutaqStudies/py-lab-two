# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:27:21 2017

@author: admin
"""

import subprocess
import os
import hashlib

def printPath():
    try:
        PATH = "./"
        print(os.listdir(PATH))
        subprocess.Popen('explorer "%s"'%(PATH))
        return PATH
    except(FileNotFoundError,OSError,UnicodeEncodeError):
        print("неа")

PATH = printPath()
files = os.listdir(PATH)

##############MD5
def getMD5sum(file):
    hashs = hashlib.md5()
    fd = open(file, 'r')
    b = fd.read()
    hashs.update(b.encode('utf-8'))
    fd.close()
    return hashs.hexdigest()
#############

dict = {}
dubs = {}
for top, dirs, files in os.walk(PATH):
    for num in files:
        fname =  os.path.join(top, num)
        fname = str(fname)
        md5sum = getMD5sum(fname)
        print(md5sum, 'utf-8')
        if md5sum  in dict.keys():
            dubs[md5sum] = str(fname + ';  ' + dict[md5sum])
        dict[md5sum] = fname
            
print(dubs)

