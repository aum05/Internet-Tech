import threading
import Queue
import time
import sys

import socket

#--------------------------------socket for client------------------------------------#
try:
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[ls]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
ls.bind(server_binding)
ls.listen(1)
host = socket.gethostname()
print("[ls]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[ls]: Server IP address is {}".format(localhost_ip))

#--------------------------------socket for TS1------------------------------------#
try:
    ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[TS1]: Client socket for ls created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# port and hostname from cmd line argument
ts1_port = int(sys.argv[3])
ts1host_addr = socket.gethostbyname(sys.argv[2])

# connect to ts1
ts1_binding = (ts1host_addr, ts1_port)
ts1.connect(ts1_binding)
ts1.settimeout(3)

#--------------------------------socket for TS2------------------------------------#
# socket for TS2
try:
    ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[TS2]: Client socket for ls created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# port and hostname from cmd line argument
ts2_port = int(sys.argv[5])
ts2host_addr = socket.gethostbyname(sys.argv[4])

# connect to ts2
ts2_binding = (ts2host_addr, ts2_port)
ts2.connect(ts2_binding)
ts2.settimeout(3)

#-----------------------------store the client message------------------------------#
q = Queue.Queue()
threads = list()

#------------------------forwarding queries to TS1 and TS2--------------------------#
def recv_and_fwd(csockid, my_q):
    while True:
        try:
            # Receive query from the client
            data_from_client = csockid.recv(1024)
            message = data_from_client.decode('utf-8')
            print(message)

            my_q.put(message)

            # Send queries to both Top-level Servers
            ts1.sendall(message.encode('utf-8'))
            ts2.sendall(message.encode('utf-8'))
        
        except socket.error:
            print("client connection closed")
            csockid.close()
            break

def recv_from_ts1(csockid, addr):
    while True:
        try:
            data_from_ts1 = ts1.recv(1024)

            decoded_msg_1 = data_from_ts1.decode('utf-8')
            print('TS1 recv: ' + decoded_msg_1)

            if decoded_msg_1:
                csockid.sendall(decoded_msg_1.encode('utf-8'))

        except socket.timeout as err:
            print('time-out')
            error_msg = msg + ' - Error:HOST NOT FOUND'
            csockid.sendall(error_msg.encode('utf-8'))
            
            
def recv_from_ts2(csockid, addr):
    while True:
        try:
            data_from_ts2 = ts2.recv(1024)

            decoded_msg_2 = data_from_ts2.decode('utf-8')
            print('TS2 recv: ' + decoded_msg_2)

            if decoded_msg_2:
                csockid.sendall(decoded_msg_2.encode('utf-8'))
        
        except socket.timeout as err:
            pass
            
#--------------------------------------runner---------------------------------------#
while True:
    csockid, addr = ls.accept()
    try:
        t1 = threading.Thread(name='recv_and_fwd', target=recv_and_fwd, args=(csockid,q))
        t1.start()
        #t1.join()
        threads.append(t1)
        
        t2 = threading.Thread(name='recv_from_ts1', target=recv_from_ts1, args=(csockid,addr))
        t2.start()
        #t2.join()
        threads.append(t2)

        t3 = threading.Thread(name='recv_from_ts2', target=recv_from_ts2, args=(csockid,addr))
        t3.start()
        #t3.join()
        threads.append(t3)

        while q.qsize > 0:
            msg = q.get()
        
        for t in threads:
            t.join()

    except Exception as err:
        print(err)
