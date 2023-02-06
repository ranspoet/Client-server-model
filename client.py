import sys
import socket


class Client:
    def __init__(self):
        self.port = 12345
        self.n = 0

        self.client_socket = socket.socket()

    def connect(self):
        # Create a socket object
        self.client_socket.connect(('127.0.0.1', self.port))
        self.n = input('Enter no of inputs:')

        self.client_socket.send(self.n.encode())

        for i in range(0, int(self.n)):

            message = input(" -> ")  # again take input
            x = message.encode()
            self.client_socket.send(x)  # send message

        self.client_socket.close()  # close the connection


if __name__ == '__main__':
    Client().connect()
