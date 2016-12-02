import socket, sys
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = sys.argv[1]
print(sys.argv[1])
 
class ClientThread(Thread):
 
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New thread started for "+ip+":"+str(port)
 
 
    def run(self):
        while True:
            data = conn.recv(2048)
            locations.append((conn, data))
            if not data: break
            print "received data:", data
            
TCP_PORT = 9000
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
locations = []
 
while True:
    tcpsock.listen(4)
    print "Waiting for incoming connections..."
    (conn, (ip,port)) = tcpsock.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)
    # for location in locations:
    #     print location
    # locations = []
 
for t in threads:
    t.join()