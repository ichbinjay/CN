import socket
from time import time, sleep
import _thread

ip = "127.0.0.1"
port = 1230
start_time = 0
flag = False
message = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(2)
print("Server started...", end="")
client, address = server.accept()
print(f"Connected to {address}")


def server():
    while True:
        global message
        global flag
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
        flag = True
        reply = client.recv(1024).decode("utf-8")
        if reply == "ack":
            flag = False


def check(timer):
    while True:
        sleep(timer)
        if flag:
            print("Acknowledge not received, sending again...")
            client.send(message.encode("utf-8"))


_thread.start_new_thread(check, (5,))
server()

