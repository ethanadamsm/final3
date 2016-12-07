import socket 
import os
from threading import Thread
import threading
import thread
clients = set()
clients_lock = threading.Lock()
dataset = []

def listener(client, address):
    global clients_lock
    print "Accepted connection from: ", address
    with clients_lock:
        clients.add(client)
    try:
        while True:
            data = client.recv(1024)
            if len(data.replace(' ', '').split(',')):
            dataset.append(data)
            if not data:
                break
            else:
                print repr(data)
                with clients_lock:
                    for c in clients:
                        c.sendall(data)
    finally:
        with clients_lock:
            clients.remove(client)
            client.close()

host = str(socket.gethostbyname(socket.gethostname()))
port = 9000

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(2)
th = []

while True:
    print "Server is listening for connections>>>"
    client, address = s.accept()
    th.append(Thread(target = listener, args = (client, address)).start())
    if len(clients) > 1:
        if len(dataset) == 2:
            for client in clients:
                for data in dataset:
                    mylist = my_string.replace(' ','').split(',')
                    ip = mylist[2]
                    if ip == str(socket.gethostbyname(client.gethostname())):
                        print "same"
                    else:
                        client.sendall(data)

s.close()