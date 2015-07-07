# -*- coding: utf-8 -*-
"""
    8-4,8-5,8-6，8-7 素数，约数,素因子分解，完全数 
    注：
    1,math模块的sqrt返回的是 float 型，cmath模块的sqrt返回的是 complex 复数型
    2,[x for x in seq if x%2] ，for语句嵌套if只能用在创立迭代器时使用，而不能用于循环语句时
"""
from math import sqrt

def isprime(num):
    i=2
    end=int(sqrt(num))
    while i<end:
        if num%i==0:
            return False
        i+=1
    return True

def getfactors(num):
    i=1
    result=[]
    while i<=num:
        if num%i==0:
            result.append(i),
        i+=1
    return result
    
def resolve_num(num):
    result=[]
    sprimefactors=[]
    factors=getfactors(num)
    factors.remove(1)
    factors.remove(num)
    for fact in factors:
        if isprime(fact):
            sprimefactors.append(fact)
    for fact in sprimefactors :
        while num%fact==0:
            result.append(fact)
            num=num/fact
    return result
    
def all_num(num):
    all_factors=getfactors(num)
    all_factors.remove(num)
    if sum(all_factors)==num:
        return True
    return False
    
test1=53
test2=52
test3=51
test4=20
print isprime(test1)
print isprime(test2)
print isprime(test3)
print getfactors(test1)
print getfactors(test2)
print getfactors(test3)
print resolve_num(test1)
print resolve_num(test2)
print resolve_num(test3)
print resolve_num(test4)
print all_num(6)
print all_num(7)