from socket import *
import sys
from threading import Thread

IP = "127.0.0.1"
PORT = int(sys.argv[1])


server_socket = socket(AF_INET, SOCK_STREAM) #creates server socket

#this binds the ip address and port number
server_socket.bind((IP, PORT))

#server starts listeniing
server_socket.listen()

clients_socket_and_port_number = {}






def recieving_and_sending_message(cs):
	
	while 1:
		message_from_client = cs.recv(2048)
		#t = message_from_client.upper()
		#cs.send(t.encode())
		for client_socket in clients_socket_and_port_number:
			client_socket.send(message_from_client)
	
	
print("The server is ready to recieve connections on {} : {}".format(IP,PORT))	
#server waits for the connections from clients
while 1:
	client_socket , addr = server_socket.accept()
	username = client_socket.recv(2048).decode()
	print()
	print("New connection recieved from this IP address and port number: {} {}".format(addr,username))
	
	client_socket.send("CONFIRMATION".encode('utf-8'))
	
	#recieving_and_sending_message(client_socket)
	clients_socket_and_port_number[client_socket] = username
	#client_socket.send("******Welcome to our Chat server******".encode('utf-8'))
	th = Thread(target=recieving_and_sending_message, args=(client_socket,))
	th.start()
	
	

	
	
