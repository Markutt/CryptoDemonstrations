import json
import socket
import sys

from pydoc import locate

HOST = "127.0.0.1"  # using loopback address
PORT = 65450
# Roles that will be sent to the clients
REC = "01"
SEND = "10"
INFO = "11"


def establish_connection():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # port type: IPv4, socket type: stream
    conn.connect((HOST, PORT))
    scheme = None
    message = ""
    while True:
        try:
            response = conn.recv(4096).decode()
            if response[0:2] == REC:
                message = scheme.decrypt(conn.recv(4096).decode())
                print(message)
            elif response[0:2] == SEND:
                message = input("Please enter your message: ")
                conn.sendall(scheme.encrypt(message).encode())
            elif response[0:2] == INFO:
                path = select_encryption(response[2:])
                module = locate(path)
                scheme = module()

        except socket.error:
            print("Send failed")
            sys.exit()

def select_encryption(scheme_name):
    with open("help.json", "r") as f:
        ciphers = json.load(f)
        for cipher in ciphers:
            if scheme_name == cipher:
                return ciphers[cipher]["path"]








establish_connection()
