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
        ip_server = socket.gethostbyname(socket.gethostname())
        port_server = 4456
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr_server = (ip_server, port_server)
        self.stop = False
        self.run()



    def run(self):
        self.socket_client.connect(self.addr_server)
        print(f"client_app connected to server")



