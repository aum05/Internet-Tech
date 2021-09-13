import threading
import time
import random
import sys

import socket

try:
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[RS]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
rs.bind(server_binding)
rs.listen(1)
host = socket.gethostname()
print("[RS]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[RS]: Server IP address is {}".format(localhost_ip))


hosts = []
ip = []
fl = []
with open('PROJI-DNSRS.txt', 'r') as file:
    for l in file:
        line = l.split(" ")
        hosts.append(line[0])
        ip.append(line[1])
        fl.append(line[2].rstrip("\r\n"))

dns = {"hostName" : hosts, "IP": ip, "flag": fl}

while True:
    csockid, addr = rs.accept()
    try:
        while True:
            # Receive data from the server
            data_from_client = csockid.recv(1024)
            message = data_from_client.decode('utf-8')

            # Lookup the queried domain in the RS-DNS table
            host_name = [name.lower() for name in dns["hostName"]]

            if message.lower() in host_name:
                ind = host_name.index(message.lower())
            else:
                ind = dns["flag"].index("NS")

            # Send either the resolved DNS or the TShostname
            msg = dns["hostName"][ind] + " " + dns["IP"][ind] + " " + dns["flag"][ind]
            csockid.sendall(msg.encode('utf-8'))
    except:
        pass