# -*- coding: utf-8 -*-
"""
    7-3
    字典根据键来排序和根据值来排序
    注：根据值来排序用到 operator.itemgetter(1) 
"""

import operator

def sort_by_key(dictionary):
    result=sorted(dictionary.items())
    print result
        
def sort_by_value(dictionary):
    result=sorted(dictionary.items(),key=operator.itemgetter(1))
    print result
    
test={'d':'e4','e3':'c2','ba':'a','c':'d','a7':'b7'}
sort_by_key(test)
sort_by_value(test)