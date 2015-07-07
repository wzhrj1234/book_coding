# -*- coding: utf-8 -*-
"""
    9-2,3,4  文件访问,文件行数,文件访问2
"""
import os.path,sys

def openfile():
    filename=raw_input("Enter file's name: ")
    number=int(raw_input("How many lines to print: "))
    try:
        f=open(os.path.join(sys.path[0],filename),'r')
        for line in f:
            print line,
            number-=1
            if number==0:
                break
        f.close()
    except IOError,e:
        print e
        
def file_num():
    filename=raw_input("Enter file's name: ")
    try:
        f=open(os.path.join(sys.path[0],filename),'r')
        result=0
        for line in f:
            result+=1
        f.close()
        print "The file have %d lines" %result
    except IOError,e:
        print e
        
def showfile():
    filename=raw_input("Enter file's name: ")
    try:
        f=open(os.path.join(sys.path[0],filename),'r')
        num=1
        for line in f:
            print line,
            if num==25:
                p=raw_input('Please enter any word to continue...')
                num=0
            num+=1
        f.close()
    except IOError,e:
        print e
        
openfile()
file_num()
showfile()