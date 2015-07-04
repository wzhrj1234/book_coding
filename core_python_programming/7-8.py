# -*- coding: utf-8 -*-
"""
    7-8
    人力资源
    注：
    字符对齐 ’abc'.ljust(20)
"""

import operator

staffs={}
test_staffs={'banana':'3','orange':'1','apple':'6','egg':'5'}
staffs=test_staffs

def show_staff():
    result=sorted(staffs.items())
    for name in result:
        print name[0].ljust(20),' : ',str(name[1])

def show_staff_by_number():
    result=sorted(staffs.items(),key=operator.itemgetter(1))
    for name in result:
        print name[0].ljust(20),' : ',str(name[1])
    
def add_staff():
    prompt_name='Entry staff\'s name(\'999\' will quit):'
    prompt_number='Entry staff\'s number:'
    while True:
        name=raw_input(prompt_name)
        if name=='999':
            break
        number=raw_input(prompt_number)
        staffs[name]=number
    

def show_menu():
    menu="""
    (A)dd staffs
    (S)how staffs
    (b)y number show staffs
    (Q)uit
    Entry your choice:"""
    while True:
        try:
            choice=raw_input(menu).strip()[0].lower()
        except(EOFError,KeyboardInterrupt):
            choice='q'
        print 'Your choice is [%s].' %choice
        if choice not in 'asbq':
            print 'Wrong choice!'
            continue
        if choice=='a': add_staff()
        if choice=='s': show_staff()
        if choice=='b': show_staff_by_number()
        if choice=='q': break
        
        
show_menu()