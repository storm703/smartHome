import socket
"""
IP = "192.168.178.22"
PORT = 7000
MESSAGE = b'Hello World'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (IP, PORT))

"""
local_addr = ('localhost', 11000)
ard_cont_addr = ('192.168.178.178', 31415)



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def set(id, closed): # 100 -> geschlossen ; 0 -> offen
    MESSAGE = b'IDFFFFFFFFFFFFFLength'
    sock.sendto(MESSAGE, ard_cont_addr)

def get():
    MESSAGE = b'IDFFFFFFFFFFLength'
    sock.sendto(MESSAGE, ard_cont_addr)
    #TODO: Listen
    #sock.bind("localhost", 12345)???????????
    #sock.listen(1)

    # accept connections from outside
    #(clientsocket, address) = serversocket.accept()
    #closed = sock.recv(2048)
    #return closed
