# -*- coding: utf-8 -*-
"""
    7-5
    添加用户登入时间记录,用户名不区分大小写,不带特殊字符
    cdg三问未完成，cd之后完成
    注：
    1，当前时间的合理字符串输出 time.strftime()
    2，删除字典中某个值，dictionary.pop(key)
    3，字符数字集合，string.ascii_letters,string.digits
    4，python 没有goto语句，要跳出多重循环的话可以写个函数，然后用return直接跳出
    
"""

from time import strftime,localtime
import string

db={}
db_time={}
character=string.ascii_letters+string.digits


def newuser():
    prompt='login desired:'
    while True:
        name=raw_input(prompt).lower()
        for char in name:
            if char not in character:
                print 'name can\'t hava a special letter!'
                return 
        if db.has_key(name):
            prompt='name taken, try another:'
            continue
        else:
            break
    pwd=raw_input('passwd:')
    db[name]=pwd
    db_time[name]=strftime("%a,%d %b %Y %H:%M:%S",localtime())
    
    
def olduser():
    name=raw_input('login:').lower()
    pwd=raw_input('passwd:')
    passwd=db.get(name)
    if passwd == pwd:
        print 'welcome back',name
        print 'Your last login time is :'+db_time[name]
        db_time[name]=strftime("%a,%d %b %Y %H:%M:%S",localtime())
    else:
        print 'login incorrect'

def deleteuser():
    name=raw_input('which user you want to delete:').lower()
    if db.has_key(name):
        db.pop(name)
        db_time.pop(name)
    else:
        print 'wrong name!'
    control()
    

def showusers():
    print 'showusers:'
    for name in db.keys():
        print name,',',db[name],' , last login time:',db_time[name]
    control()
        
def control():
    prompt="""
(D)elete a user
(S)how all user
(B)ack
Enter choice:"""
    chosen=False
    while not chosen:
        try:
            choice=raw_input(prompt).strip()[0].lower()
        except(EOFError,KeyboardInterrupt):
            choice='b'
        print '\nYou picked:[%s]' %choice
        if choice not in 'dsb':
            print 'invalid option, try again'
        else:
            chosen=True
        if choice=='d': deleteuser()
        if choice=='s': showusers()
        if choice=='b': showmenu()
    
def showmenu():
    prompt="""
(N)ew User Login
(E)xisting User Login
(Q)uit
(C)ontorl
Enter choice:"""
    done=False
    while not done:
        chosen=False
        while not chosen:
            try:
                choice=raw_input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice='q'
            print '\nYou picked:[%s]' %choice
            if choice not in 'neqc':
                print 'invalid option, try again'
            else:
                chosen=True
        if choice=='q':done=True
        if choice=='n':newuser()
        if choice=='e':olduser()
        if choice=='c':control()
        
if __name__=='__main__':
    showmenu()