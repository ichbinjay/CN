import socket
from time import time
while True:
    start=time()
    string = input("domain: ")
    ip = "192.168.50.90"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    server.send(bytes(string, "utf-8"))
    ip = server.recv(1024).decode("utf-8")
    server.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    server.send(bytes(string, "utf-8"))
    ip = server.recv(1024).decode("utf-8")
    server.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    server.send(bytes(string, "utf-8"))
    print(server.recv(1024).decode("utf-8"))
    stop = time()
    print("Delay:", stop-start, "ms")
    server.close()
