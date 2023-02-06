import socket
import dataman as dm

global n


class Server:
    def __init__(self):
        self.host='127.0.0.1'
        self.port = 12345
        self.n = 0
        self.server_socket = socket.socket()

    def ninput(self):
        #The bind() function takes tuple as argument
        self.server_socket.bind((self.host, self.port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        self.server_socket.listen(2)
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        while True:

            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            self.n = int(data)
            print("from connected user: " + str(data))

            break

        for i in range(0,self.n):
            data = conn.recv(1024).decode()
            dm.add(i,data)
        
        dm.view()


if __name__ == '__main__':
    Server().ninput()
