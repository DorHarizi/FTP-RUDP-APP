import socket
import time


FORMAT = "utf-8"
PACKET_SIZE = 1024
CLIENT_DATA_PATH = "../client_files"
SERVER_DATA_PATH = ""


class client_app:
    """
    Client class for the FTP application.
    """

    def __init__(self):
        ip_server = '192.168.1.19'
        port_server = 4455
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr_server = (ip_server, port_server)
        self.run()


    def run(self):
        self.socket_client.connect(self.addr_server)
        print(f"client connected to server")
        while True:
            packet = self.socket_client.recv(PACKET_SIZE).decode(FORMAT)
            cmd, data = packet.split("@")

            if cmd == "DISCONNECTED":
                print("the client disconnected from the server")
                break
            if cmd == "MESSAGE":
                print(f'[message from client]{data}')
            if cmd == "LIST":
                self.socket_client.send(cmd.encode(FORMAT))



        client.close()
        print(" the client close the connection")



