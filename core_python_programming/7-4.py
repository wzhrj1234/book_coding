# -*- coding: utf-8 -*-
"""
    7-4
    用两个列表建立一个字典
    注：同时 for 两个 list ，用到 zip()
"""

def create_dictionary(list1,list2):
    result={}
    #同时 for 两个 list
    for key,value in zip(list1,list2):
        result[key]=value
    return result
        
test_list1=[1,2,5,4,3]
test_list2=['anc','du','smd','1dc','fud']
print create_dictionary(test_list1,test_list2)
