# -*- coding: utf-8 -*-
"""
    7-7
    颠倒字典的键和值
"""

def trans_dic(dictionary):
    result={}
    for key in dictionary:
        result[dictionary[key]]=key
    return result
    
test_dic={'a':1,'b':2,'c':3,'d':4,'e':5}
print trans_dic(test_dic)