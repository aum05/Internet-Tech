import threading
import time
import random
import sys

import socket

# client for root server
try:
    crs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CRS]: Client socket for RS created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# port and hostname from cmd line argument
rs_port = int(sys.argv[2])
rshost_addr = socket.gethostbyname(sys.argv[1])

# connect to rs
rs_binding = (rshost_addr, rs_port)
crs.connect(rs_binding)

# read input file
with open('PROJI-HNS.txt', 'r') as f:
    read_file = f.readlines()

# send a DNS query to the client.
for line in read_file:
    msg = line.rstrip("\r\n")
    crs.sendall(msg.encode('utf-8'))

    # Receive data from the root-server
    data_from_rs = crs.recv(1024)
    decoded_msg = data_from_rs.decode('utf-8')

    # write received data to outupt file if DNS is resolved
    if "A" in decoded_msg:
        with open('RESOLVED.txt', 'a') as text_file:
            text_file.write(decoded_msg + "\n")
    elif "NS" in decoded_msg:
        try:
            cts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[CTS]: Client socket for TS created")
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()

        ts_port = int(sys.argv[3])

        name = decoded_msg.split(" - ")
        host = name[0]

        localhost_addr = socket.gethostbyname(host)
        server_binding = (localhost_addr, ts_port)
        cts.connect(server_binding)

        cts.sendall(msg.encode('utf-8'))

        # Receive data from the server
        data_from_ts = cts.recv(100)
        decoded = data_from_ts.decode('utf-8')

        with open('RESOLVED.txt', 'a') as text_file:
            text_file.write(decoded + "\n")
