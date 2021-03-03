import socket
import threading
server = socket.socket()
host_name = socket.gethostname()
port = 9999
server.bind((host_name, port))
server.listen(1)
def accept_players():
    while len(connections)!=2:
        connection, address = server.accept()
        connections.append(connection)
    else:
        a2.start()
        a3.start()
def recv1():
    while True:
        msg = connections[0].recv(1024).decode()
        send(msg.encode())
def recv2():
    while True:
        msg = connections[1].recv(1024).decode()
        send2(msg.encode())
def send(message):
    connections[1].send(message)
def send2(message):
    connections[0].send(message)
connections =[]
a1 = threading.Thread(target=accept_players)
a2 =threading.Thread(target=recv1)
a3 =threading.Thread(target=recv2)
a1.start()
