import socket

server_addr = ('127.0.0.1', 7500)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind("localhost", 12345)
sock.listen(1)

while True:
    (clientsocket, address) = sock.accept()
    mes = sock.recv(1024)
    clientsocket.sendto(b(mes))
    
