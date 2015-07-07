# -*- coding: utf-8 -*-
"""
    8-11 (8-10完成后未保存）
    未完成对齐
"""
def show():
    start=int(raw_input("输入起始数字： "))
    end=int(raw_input("输入截止数字： "))
    print '十进制      二进制    八进制    十六进制   ASCII'
    print '-'*30
    num=start
    while num<=end:
        if num<255:
            asc=chr(num)
        else:
            asc=''
        print "%d     %s    %s    %s    %s" %(num,bin(num),oct(num),hex(num),asc)
        num+=1
        
show()
    
    