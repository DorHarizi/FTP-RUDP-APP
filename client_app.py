import socket
import time
import os
import sender

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


    def uploadFile(self, file_path):
        file_name = os.path.basename(file_path)
        self.socket_client.send(f"UPLOAD@{file_name}".encode(FORMAT))
        time.sleep(5)
        sender.send_file(file_path, self.ip, 9999)
        send_data = f"the file {file_name} is uploaded!"
        print(send_data)
        return send_data

    def downloadFile(self, file_name):
        self.socket_client.send(f"DOWNLOAD@{file_name}".encode(FORMAT))
        path_file = f"{CLIENT_DATA_PATH}/{filename}"
        time.sleep(5)
        receiver.receive_file(path_file, IP, 9999)
        send_data = f"The file {file_name} is downloaded!"
        print(send_data)
        return send_data

    def get_list(self):
        self.socket_client.send("LIST".encode(FORMAT))
        data = self.socket_client.recv(PACKET_SIZE).decode(FORMAT)
        print(f"{data}")
        return data

    def deleteFile(self, file_name):
        send_data = f"DELETE@{file_name}"
        self.socket_client.send(send_data.encode(FORMAT))
        data = self.socket_client.recv(PACKET_SIZE).decode(FORMAT)
        print(f"{data}")
        return data


    def disconnected(self):
        self.socket_client.send("DISCONNECTED@".encode(FORMAT))
        print("the client_app has been disconnected")
        self.socket_client.close()
        print("job done")


    def run(self):
        self.socket_client.connect(self.addr_server)
        print(f"client_app connected to server")



