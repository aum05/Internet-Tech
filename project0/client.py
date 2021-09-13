import threading
import time
import random
import sys

import socket


try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# Define the port on which you want to connect to the server
port = 50007
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)

# read input file
with open(sys.argv[1], 'r') as f:
    read_file = f.readlines()


# send a intro message to the client.
n = random.randint(0,len(read_file)-1)
msg = read_file[n].rstrip("\r\n")
cs.send(msg.encode('utf-8'))

# Receive data from the server
data_from_server = cs.recv(100)
decoded_msg = data_from_server.decode('utf-8')
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

# write received data to outupt file
with open(sys.argv[2], "a") as text_file:
    text_file.write(decoded_msg)


# close the client socket
cs.close()
exit()