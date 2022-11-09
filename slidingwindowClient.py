import socket
ip = "127.0.0.1"
port = 1230

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))
buffer = []
while True:
    try:
        message = server.recv(1024).decode("utf-8")
        print(f"Server: {message}")
        buffer.append(message)
        reply = input("Client:")
        server.send(reply.encode("utf-8"))
    except ConnectionAbortedError:
        print("sequence received successfully. Data is",buffer)
        server.close()
        break
