# -*- coding: utf-8 -*-
"""
    UDP服务端
"""

from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    text=raw_input('Should the computer continue to listen ? ')
    if text=='no':
        break
    print 'waiting for message...'
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' %(ctime(),data),addr)
    print '...received from and returned to:',addr

udpSerSock.close()