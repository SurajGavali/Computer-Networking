import socket
import threading
import time
import random
import hashlib
import os



def receiver(p):
    host = '127.0.0.1'      
    port = 12004      

    s = socket.socket()
    s.bind((host,port))     

    s.listen(5)            
    print("Server is on...")
    c,addr = s.accept()     
    c_ack,addr_ack = s.accept()
    print("Connection from: " + str(addr))
    
    expect_seq_num = 1


    while(1):
        message = c.recv(1024).decode()    
    
        message = message.split('/////')
       
        if not message[2]:
            break
        
        if float(message[3]) >= p:
            print("Received Packet with Sequence Number:",message[1])
        else:
            print("Dropped packet ", message[1])
        seq_num = message[1]
        prob = message[3]
      
        if (int(seq_num) == expect_seq_num) and (float(prob) >= p) :
            
            ack_msg = 'ACK for packet ' + seq_num
            print("Sending ACK for Sequence Number:",seq_num)
            c_ack.send(ack_msg.encode())
            expect_seq_num = expect_seq_num+1
    c.close()
    c_ack.close()
