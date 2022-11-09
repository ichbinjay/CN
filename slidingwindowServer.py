import socket

ip = "127.0.0.1"
port = 1230

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)
print("Server started...", end="")
client, address = server.accept()
print(f"Connected to {address}")

def server():
    sequence = ["1", "2", "3", "4", "5", "6"]
    i = 0
    for _ in range(2):
        buffer = sequence[i:i+3]
        for message in buffer:
            client.send(message.encode("utf-8"))
            reply = client.recv(1024).decode("utf-8")
            if reply == "ack":
                print("Acknowledge received")
            else:
                buffer = sequence[i:i+3]
        i+=3
    client.close()


server()
