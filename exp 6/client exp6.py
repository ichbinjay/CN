import socket
from time import sleep
ip = "127.0.0.1"
port = 1230

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))

while True:
    message = server.recv(1024).decode("utf-8")
    print(f"Server: {message}")
    sleep(7)
    server.send("ack".encode("utf-8"))
