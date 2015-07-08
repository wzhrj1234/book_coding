# -*- coding: utf-8 -*-
"""
    SocketServer模块下的TCP客户端
"""

from socket import *

HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

while True:
    tcpClisock=socket(AF_INET,SOCK_STREAM)
    tcpClisock.connect(ADDR)
    data=raw_input('>')
    if not data:
        break 
    tcpClisock.send('%s\r\n' %data)
    data=tcpClisock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpClisock.close()