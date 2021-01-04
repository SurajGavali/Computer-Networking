from socket import *
import sys
from threading import Thread

IP = "127.0.0.1"
PORT = int(sys.argv[1])
USERNAME = sys.argv[2]
#my_username = sys.argv[2]

client_socket = socket(AF_INET,SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.send(bytes(USERNAME,'utf-8'))



def message_to_all_clients():
	while 1:
		MESSAGE = client_socket.recv(2048).decode('utf-8')
		if (MESSAGE == "CONFIRMATION"):
			client_socket.send(USERNAME.encode('utf-8'))
		else:
			print(MESSAGE)
			
			

#this takes message from the client sends to server and diplays to all clients
def recieving_and_sending_message():
	print("Users on the group")
	while 1:
		
		
		message_to_server =  f'{USERNAME}: {input("")}'
		
		client_socket.send(message_to_server.encode('utf-8'))
		
		
		
		
		#message_to_clients = client_socket.recv(2048).decode('utf-8')
		#print(message_to_clients)
		

#thread for te parallel clients
th2 = Thread(target = message_to_all_clients)
th2.start()

#thread for the messages	
th1 = Thread(target = recieving_and_sending_message)
th1.start()	

	
