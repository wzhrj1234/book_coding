# -*- coding: utf-8 -*-
"""
    8-8,8-9 阶乘，斐波那耶数
"""

def factorial(num):
    i=1
    result=1
    while i<=num:
        result*=i
        i+=1
    return result

def fbny(num):
    result=[1,1]
    if num in (1,2):
        return 1
    i=3
    while i<=num:
        result.append(result[i-2]+result[i-3])
        i+=1
    return result[num-1]
    
print factorial(5)
print fbny(5)