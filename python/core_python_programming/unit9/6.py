# -*- coding: utf-8 -*-
"""
    9-6 文件比较
    未完成
"""
import sys,os.path

def compareTxt():
    txt1=raw_input("Please enter the first file: ")
    txt2=raw_input("Please enter the second file: ")
    try:
        file1=open(os.path.join(sys.path[0],txt1),'r')
        file2=open(os.path.join(sys.path[0],txt2),'r')
        lines1=file1.readlines()
        lines2=file2.readlines()
        for i in range(min(len(lines1),len(lines2))):
            if lines1[i]!=lines2[i]:
                print i
                break
        if len(lines1)!=len(lines2):
            print i+1
    except IOError,e:
        print e
        
compareTxt()