import socket
from time import time

ip = "127.0.0.1"
port = 1230

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))

i = "1"
start = time()
fp = open("m" + i + ".jpg", "wb")
while True:
    try:
        message = server.recv(1024)
        fp.write(message)
        server.send("ack".encode("utf-8"))
    except:
        break
fp.close()
end = time()

size = float(i) * 8000
time_taken = end - start
print("throughput for", i, "mb is", size / time_taken, "kilobits/sec")

server.close()
