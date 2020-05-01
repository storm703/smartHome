import socket

number_of_arduinos = 1

server_addr = ('127.0.0.1', 7500)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind("localhost", 12345)
sock.listen(number_of_arduinos)

while True:
    (clientsocket, address) = sock.accept()
    mes = sock.recv(1024)
    clientsocket.sendto(mes)
