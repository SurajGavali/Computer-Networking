#!/usr/bin/python
from socket import * 
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort));

print("server is ready");
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode().upper()
	print("message from"); print(clientAddress);
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)



