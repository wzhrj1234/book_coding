# -*- coding: utf-8 -*-
'''
    7-9
    翻译
'''
from string import replace

def tr(srcstr,dststr,string,dif=True):
    if dif==True:
        srcstr=srcstr.lower()
        dststr=dststr.lower()
        string=string.lower()
    return string.replace(srcstr,dststr)
    
test_srcstr='abcde'
test_dststr='mno'
test_string='abcdemno'
print tr(test_srcstr,test_dststr,test_string)