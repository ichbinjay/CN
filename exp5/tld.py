import socket


def __main__():
    ip = "192.168.50.59"
    port = 1234

    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip, port))
        server.listen(2)
        client, address = server.accept()
        string = client.recv(1024).decode("utf-8")
        print(f"Client Requested: {string}")
        msg = "null"
        if string[-4:] == ".com":
            msg = "192.168.50.60"
        print("send ", msg, "to client...")
        client.send(msg.encode("utf-8"))
        print("Done!")


__main__()
