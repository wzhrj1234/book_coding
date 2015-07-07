# -*- coding: utf-8 -*-
"""
    7-10 加密
"""
import string

down_a='abcdefghijklmnopqrstuvwxyz'
down_b='nopqrstuvwxyzabcdefghijklm'
up_a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
up_b='NOPQRSTUVWXYZABCDEFGHIJKLM'

def encrypt(strings):
    table=string.maketrans(down_a+up_a,down_b+up_b)
    return strings.translate(table)
    
test='I have a APPLE'
test2='V unir n NCCYR'
print encrypt(test)
print encrypt(test2)