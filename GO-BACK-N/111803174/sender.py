import socket
import time
import os
import random
import hashlib
import threading
import sys

sent_flag = []          
ACK_num = []

def get_ACK(a,s):

    while(1):
        msg = s.recv(1024).decode()
        print(msg)
        msg = msg.split()
      
        if msg[0] == 'ACK':
            ACK_num[int(msg[3])] = 1
            

def makePack(num, pac): 
    sequence_number = num
    file_check_sum = hashlib.md5(pac).hexdigest()
    prob = random.randint(1, 10)/10.0
    packet = str(file_check_sum) + '/////' + str(sequence_number) + '/////'  + str(pac) + '/////' + str(prob) + '/////'
    return packet




def divideintopac(data, num):
    lis = []
    while data:
        lis.append(data[:num])
        data = data[num:]
    return lis

def run(cSocket, window_size, numpack):
    timeout = 1
    timelist = []
    win_base = 1
    try:
        fil = open('data.txt', 'rb')
        data = fil.read()
        pack_list = divideintopac(data, 7)
        fil.close()
    except IOError:
        print("file doesn't exists") 
    timer = time.time()
    l=len(pack_list)
    for i in range(1,numpack+2):
        sent_flag.append(0)
        ACK_num.append(0)
    
    while win_base+window_size-1 < numpack:
        for j in range(win_base,win_base+window_size):
            if sent_flag[j] == 0:
                packet = makePack(j, pack_list[j])
                print("Sending packet No.", int(packet.split('/////')[1]))
                sent_flag[j] = 1
                cSocket.send(packet.encode())
                
        presenttime = time.time()
            
        
        if presenttime - timer > timeout:
            print("\nTimeout: Resending and resetting timer")
            for j in range(win_base,win_base+window_size):
                sent_flag[j] = 0
            timer = time.time()
            continue
        elif ACK_num[win_base] == 1:
           
            win_base = win_base+1
            print(win_base)
            timer = time.time()
        

    pointer = numpack - window_size + 1         
    if numpack < window_size:
        pointer = 1         
    timer = time.time()
    while pointer <= numpack:
        for j in range(pointer,numpack+1):
            if sent_flag[j] == 0:
                packet = makePack(j, pack_list[j])
                print("Sending packet No.", int(packet.split('/////')[1]))
                sent_flag[j] = 1
                cSocket.send(packet.encode())
                
        presenttime = time.time()
        if presenttime - timer > timeout:
            print ("\nTimeout Occurred : Resending and Resetting Timer")
            for j in range(pointer,numpack+1):
                sent_flag[j] = 0
            timer = time.time()
            continue
        elif ACK_num[pointer] == 1:
            pointer = pointer+1
            timer = time.time()


def sender(window_size, numpack):
    host = '127.0.0.1'
    port = 12004
    s = socket.socket()
    s.connect((host,port))         

    s_ack = socket.socket()
    s_ack.connect((host,port))        
    t1 = threading.Thread( target=get_ACK, args=(2,s_ack) )
    t1.start()

    run(s, window_size, numpack)
    t1.join()
    s_ack.close() 
    s.close()  
