import importlib
import socket
import sys
import importlib

HOST = "127.0.0.1"  # using loopback address
PORT = 65450
# Roles that will be sent to the clients
REC = "01"
SEND = "10"


def establish_connection():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # port type: IPv4, socket type: stream
    conn.connect((HOST, PORT))
    message = ""
    while True:
        try:
            response = conn.recv(4096).decode()
            if response[0:2] == REC:
                message = conn.recv(4096).decode()
                print(message)
            elif response[0:2] == SEND:
                message = input("Please enter your message: ")
                conn.sendall(message.encode())
        except socket.error:
            print("Send failed")
            sys.exit()


def select_encryption():
    input()


select_encryption()
establish_connection()
