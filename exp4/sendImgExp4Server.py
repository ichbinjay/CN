import socket

ip = "127.0.0.1"
port = 1230

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
server.listen(1)
print("Server started...", end="")
client, address = server.accept()
print(f"Connected to {address}")

print("sending file...")

fp = open("1.jpg", "rb")

data = fp.read(1024)
while data:
    if client.send(data):
        data = fp.read(1024)
        print(fp.tell(), data[:10])
    else:
        break

print("done..")
fp.close()

server.close()
client.close()
