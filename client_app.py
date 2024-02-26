import socket
import time
import os
import sender
import receiver

# Constants for encoding format, packet size, and file directories.
FORMAT = "utf-8"
PACKET_SIZE = 1024
CLIENT_DATA_PATH = "client_files"
SERVER_DATA_PATH = 'server_files'

class client_app:
    """
    A client application for a File Transfer Protocol (FTP) system.

    This class manages the client side of an FTP system, allowing users to
    connect to a server and perform operations such as uploading, downloading,
    listing, and deleting files.

    Attributes:
        ip_client_tcp (str): IP address of the client.
        port_client_tcp (int): TCP port number for the client connection.
        ADDR_client (tuple): Tuple combining IP address and port number.
        socket_client (socket.socket): Socket object for client-server communication.
        stop_ftp (bool): Flag to control the running of the FTP operations (currently not used).
    """

    def __init__(self):
        """
        Initializes the client application, setting up the connection parameters
        and establishing a connection to the server.
        """
        self.ip_client_tcp = socket.gethostbyname(socket.gethostname())
        self.port_client_tcp = 5555
        self.ADDR_client = (self.ip_client_tcp, self.port_client_tcp)
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stop_ftp = False
        self.run()

    def uploadFile(self, file_path):
        """
        Uploads a file to the server.

        Parameters:
            file_path (str): The path of the file to upload.

        Returns:
            str: Status message of the upload operation.
        """
        file_name = os.path.basename(file_path)
        files = os.listdir(SERVER_DATA_PATH)
        send_data = ""
        for f in files:
            if f == file_name:
                send_data += f"The file: {file_name} is already exists in server file"
                return send_data
        self.socket_client.send(f"UPLOAD@{file_name}".encode(FORMAT))
        sender.send_file(file_path, self.ADDR_client[0], 9999)
        send_data = self.socket_client.recv(PACKET_SIZE).decode(FORMAT)
        return send_data

    def downloadFile(self, file_name):
        """
        Downloads a file from the server.

        Parameters:
            file_name (str): The name of the file to download.

        Returns:
            str: Status message of the download operation.
        """
        file_path = f"{CLIENT_DATA_PATH}/{file_name}"
        files = os.listdir(CLIENT_DATA_PATH)
        send_data = ""
        for f in files:
            if f == file_name:
                send_data += f"The file: {file_name} is already exists in client files"
                return send_data
        self.socket_client.send(f"DOWNLOAD@{file_name}".encode(FORMAT))
        receiver.receive_file(file_path, self.ADDR_client[0], 9999)
        send_data = self.socket_client.recv(PACKET_SIZE).decode(FORMAT)
        return send_data

    def get_list(self):
        """
        Retrieves a list of files from the server.

        Returns:
            str: A list of files available on the server.
        """
        cmd = "LIST@"
        self.socket_client.send(cmd.encode(FORMAT))
        send_data = self.socket_client.recv(PACKET_SIZE).decode(FORMAT)
        return send_data

    def deleteFile(self, file_name):
        """
        Deletes a file from the server.

        Parameters:
            file_name (str): The name of the file to delete.

        Returns:
            str: Status message of the delete operation.
        """
        send_data = f"DELETE@{file_name}"
        self.socket_client.send(send_data.encode(FORMAT))
        data = self.socket_client.recv(PACKET_SIZE).decode(FORMAT)
        return data

    def disconnected(self):
        """
        Disconnects the client from the server and closes the socket.
        """
        self.socket_client.send("DISCONNECTED@".encode(FORMAT))
        print("the client_app has been disconnected")
        self.socket_client.close()

    def run(self):
        """
        Initiates the connection to the server.
        """
        self.socket_client.connect(self.ADDR_client)
        print(f"client_app connected to server")
