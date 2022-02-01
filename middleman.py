import json
import socket
import sys

HOST = "127.0.0.1"  # using loopback address
PORT = 65450
# Roles that will be sent to the clients
REC = "01"
SEND = "10"
INFO = "11"


class Cipher:
    def encrypt(self):
        return

    def decrypt(self):
        return


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
    client = [None, None]
    turn = 2

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
                if turn == 2:
                    scheme_name = select_encryption()
                    client[0].conn.sendall((INFO + scheme_name).encode())
                    client[1].conn.sendall((INFO + scheme_name).encode())
                    turn = 0

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
                    print("Bob: " + message)
                    client[0].conn.sendall(message.encode())
                    turn = 0

        except socket.error:
            print("Send failed")
            sys.exit()


def select_encryption():
    encryption_scheme = None
    while encryption_scheme is None:
        user_input = input("Please enter your desired encryption scheme. For information about available "
                           "encryption scheme please enter help:")
        if user_input == "help":
            with open("help.json", "r") as f:
                ciphers = json.load(f)
                print("Enter [key] for [cipher] demonstration.")
                print("Key - Cipher")
                for cipher in ciphers:
                    print(cipher + " - " + ciphers[cipher]["name"])
        else:
            with open("help.json", "r") as f:
                ciphers = json.load(f)
                for cipher in ciphers:
                    if user_input == cipher:
                        encryption_scheme = cipher
                        break

            if encryption_scheme is None:
                print("There is no cipher named " + user_input + ".")
    return encryption_scheme


# scheme = PrivateKeyCryptography.HistoricalCiphers.VigenereCipher()
# scheme.generate()
# enc = scheme.encrypt(input("input:"))
# print("enc: " + enc)
# dec = scheme.decrypt(enc)
# print("dec: " + dec)
# exit()
establish_server()
