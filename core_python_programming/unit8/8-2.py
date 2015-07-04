# -*- coding: utf-8 -*-
"""
    8-2 循环
"""

def for_def():
    start=int(raw_input("Entry from number:"))
    end=int(raw_input("Entry end number:"))
    step=int(raw_input("Entry step number:"))
    num=start
    while num<=end:
        print num
        num=num+step
        
for_def()