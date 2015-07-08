# -*- coding: utf-8 -*-

"""
    TCP服务端
"""
from socket import *
from time import ctime

HOST=''
PORT=21567     #端口号
BUFSIZ=1024    #缓冲区大小 1K
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)   #绑定地址到套接字上
tcpSerSock.listen(3)    #最多3个连接

while True:
    text=raw_input('Should the computer continue to listen ? ')
    if text=='no':
        break
        
    print 'Waiting for connection...'
    
    tcpCliSock,addr=tcpSerSock.accept()
    print '...connected from :',addr
    
    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(ctime(),data))
    tcpCliSock.close()
    
tcpSerSock.close()