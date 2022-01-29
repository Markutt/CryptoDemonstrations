import socket
import sys
import time

HOST = "127.0.0.1"  # using loopback address
PORT = 65450
# Roles that will be sent to the clients
REC = "01"
SEND = "10"


class Client:
    conn = None
    ipaddress = None
    port = None

    def __init__(self, accept):
        conn, info = accept
        self.conn = conn
        self.ipaddress = info[0]
        self.port = info[1]


def establish_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # port type: IPv4, socket type: stream
    s.bind((HOST, PORT))
    s.listen(2)
    client = [None,None]
    turn = 0

    while True:
        try:

            if client[0] is None:
                client[0] = Client(s.accept())
                print("New connection established with " + str(client[0].ipaddress) + ". On the port "
                      + str(client[0].port) + ".")
            elif client[1] is None:
                client[1] = Client(s.accept())
                print("New connection established with " + str(client[1].ipaddress) + ". On the port "
                      + str(client[1].port) + ".")
            else:

                message = ""
                if turn == 0:
                    client[0].conn.sendall(SEND.encode())
                    client[1].conn.sendall(REC.encode())
                    response = client[0].conn.recv(4096)
                    message = response.decode()
                    print("Alice: " + message)
                    client[1].conn.sendall(message.encode())
                    turn = 1
                else:
                    client[0].conn.sendall(REC.encode())
                    client[1].conn.sendall(SEND.encode())
                    response = client[1].conn.recv(4096)
                    message = response.decode()
                    print("Bob: "+message)
                    client[0].conn.sendall(message.encode())
                    turn = 0

        except socket.error:
            print("Send failed")
            sys.exit()


establish_server()
