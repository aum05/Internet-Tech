import threading
import time
import random
import sys

import socket

# client for load-balancing server
try:
    cls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[Cls]: Client socket for ls created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# port and hostname from cmd line argument
ls_port = int(sys.argv[2])
lshost_addr = socket.gethostbyname(sys.argv[1])

# connect to ls
ls_binding = (lshost_addr, ls_port)
cls.connect(ls_binding)

# read input file
with open('PROJ2-HNS.txt', 'r') as f:
    read_file = f.readlines()

# send a DNS query to the client.
for line in read_file:
    msg = line.rstrip("\r\n")
    print(msg)
    cls.sendall(msg.encode('utf-8'))

    # Receive data from the root-server
    data_from_ls = cls.recv(1024)
    decoded_msg = data_from_ls.decode('utf-8')

    with open('RESOLVED.txt', 'a') as text_file:
        text_file.write(decoded_msg + "\n")