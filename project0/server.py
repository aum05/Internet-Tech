import threading
import time
import random

import socket

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50007)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()
print("[S]: Got a connection request from a client at {}".format(addr))

# Receive data from the server
data_from_client = csockid.recv(100)
message = data_from_client.decode('utf-8')
print("[S]: Data received from client : {}".format(message))

# send a intro message to the client.
msg = message[::-1]
csockid.send(msg.encode('utf-8'))

# Close the server socket
ss.close()
exit()
