import socket
import datetime


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        self.ip = None

    def insert(self, word, ip):
        node = self
        for i in range(len(word) + 1):
            if i == len(word):
                node.end = True
                node.ip = ip
                break

            index = ord(word[i]) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()

            node = node.children[index]

    def search(self, word):
        node = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if node.children[index] is None:
                return "Not found"
                break
            node = node.children[index]
        if node.end:
            return node.ip


def domain_sanitizer(url):
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    url = url.replace(".", "")
    return url.strip()


def ip_sanitizer(internet_protocol):
    return internet_protocol.strip()


def __main__():
    print("Hello User!")
    print("Welcome to Jay's DNS Server :D")
    tree = Trie()
    while True:
        print("1. Insert 2. Search 3. Exit and allow client to connect")
        choice = input("Enter your choice: ")
        if choice == "1":
            domain = input("Enter the domain name: ")
            ip = input("Enter the IP address: ")

            domain = domain_sanitizer(domain)
            ip = ip_sanitizer(ip)

            tree.insert(domain, ip)
        elif choice == "2":

            domain = input("Enter the domain name: ")
            domain = domain_sanitizer(domain)

            tree.search(domain)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

    ip = "192.168.50.60"
    port = 1234


    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip, port))
        server.listen(2)
        client, address = server.accept()
        string = client.recv(1024).decode("utf-8")
        print(f"Client Reqested: {string}")
        msg = tree.search(domain)
        print("Sending ", msg, "to client...")
        client.send(msg.encode("utf-8"))
        print("Done!")

__main__()
