import threading
import time
import random
import sys

import socket

try:
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[TS1]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
ts.bind(server_binding)
ts.listen(1)
host = socket.gethostname()
print("[TS1]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[TS]: Server IP address is {}".format(localhost_ip))


hosts = []
ip = []
fl = []
with open('PROJ2-DNSTS1.txt', 'r') as file:
    for l in file:
        line = l.split(" ")
        hosts.append(line[0])
        ip.append(line[1])
        fl.append(line[2].rstrip("\r\n"))

dns = {"hostName" : hosts, "IP": ip, "flag": fl}

while True:
    csockid, addr = ts.accept()
    try:
        while True:
            # Receive data from the server
            data_from_client = csockid.recv(1024)
            message = data_from_client.decode('utf-8')
            print(message)

            # Lookup the queried domain in the RS-DNS table
            host_name = [name.lower() for name in dns["hostName"]]

            trial = False

            if message.lower() in host_name:
                ind = host_name.index(message.lower())
                msg = dns["hostName"][ind] + " " + dns["IP"][ind] + " " + dns["flag"][ind]
                trial = True

            if trial:
                print(msg)
                csockid.sendall(msg.encode('utf-8'))
            #else:
            #    msg = ''
            #    csockid.sendall(msg.encode('utf-8'))

    except:
        pass

csockid.close()