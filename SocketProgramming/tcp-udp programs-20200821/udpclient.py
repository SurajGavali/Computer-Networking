#!/usr/bin/python
from socket import * 
message = raw_input('enter data')

#serverName = '127.0.0.1'
serverName = '210.212.183.7'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message.encode(), (serverName, serverPort));

modifiedMessage, serverAddress = clientSocket.recvfrom(2048);
print(modifiedMessage.decode())
raw_input('press something to end')
clientSocket.close()
