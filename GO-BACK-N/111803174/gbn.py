import sys
from sender import *
from receiver import *
from threading import Thread

if(len(sys.argv) < 4):
    print("Check number of arguments!!!")
    
else:
    N = int(sys.argv[2])
    p = float(sys.argv[4])
    n = int(sys.argv[6])
    print("{} {} {}".format(N,p,n))
    Thread(target = receiver, args=(p,)).start()
    sender(N,n) 
