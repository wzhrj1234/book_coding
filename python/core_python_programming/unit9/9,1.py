# -*- coding: utf-8 -*-
"""
    9-1 文件过滤
    注：
    1,读取脚本所在目录里的文件的方法，使用sys,os模块
    2,文件读取后输出每行默认带换行符
"""
import sys,os.path

def filter(filename):
    try:
        f=open(os.path.join(sys.path[0],filename),'r')
        for line in f:
            if line[0]!='#':
                print line,
        f.close()
    except IOError,e:
        print e
    
filter('test.txt')