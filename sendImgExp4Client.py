import socket

ip = "127.0.0.1"
port = 1230

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))

fp = open("m2.png", "wb")

while True:
    try:
        message = server.recv(1024)
        fp.write(message)
        server.send("ack".encode("utf-8"))
    except:
        break

server.close()
fp.close()
