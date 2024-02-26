import sender
import os
import socket
import threading
import receiver
import time

# Define constants for packet size, encoding format, and server/client data paths.
MAX_PACKET_SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = 'server_files'
CLIENT_DATA_PATH = "client_files"

class server_app:
    """
    A server application for handling basic file transfer operations.
    
    This class implements a server that supports uploading, downloading, deleting,
    and listing files stored in a specified directory on the server.
    """

    def __init__(self):
        # Initialize server address, socket, and file list.
        self.ip_server_tcp = socket.gethostbyname(socket.gethostname())
        self.port_server_tcp = 5555
        self.ADDR_server = (self.ip_server_tcp, self.port_server_tcp)
        self.list_files = []
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        
        # Populate initial file list from the server directory.
        files = os.listdir(SERVER_DATA_PATH)
        if files:
            self.list_files.extend(files)

    def downloadFile(self, msg):
        """
        Handles a request to download a file from the server.
        """
        file_path = f"{SERVER_DATA_PATH}/{msg}"
        # Simulate a delay for the download
        time.sleep(10)
        # Use the sender module to send the file to the client.
        sender.send_file(file_path, self.ip_server_tcp, 9999)
        return f"The file: {msg} downloaded"

    def uploadFile(self, msg):
        """
        Handles a request to upload a file to the server.
        """
        file_path = f"{SERVER_DATA_PATH}/{msg}"
        # Use the receiver module to receive the file from the client.
        receiver.receive_file(file_path, self.ip_server_tcp, 9999)
        return f"The file: {msg} uploaded"

    def deleteFile(self, file_name):
        """
        Handles a request to delete a file from the server.
        """
        send_data = ""
        if file_name in self.list_files:
            os.remove(f"{SERVER_DATA_PATH}/{file_name}")
            self.list_files.remove(file_name)  # Remove from the list_files as well
            send_data += "File deleted successfully."
        else:
            send_data += "File not found."
        return send_data

    def getList(self):
        """
        Generates a list of files currently stored on the server.
        """
        send_data = "The server directory is empty" if not self.list_files else "\n".join(self.list_files)
        return send_data

    def handle_client(self, conn, addr):
        """
        Manages communications with a connected client.
        """
        print(f"[NEW CONNECTION] {addr} connected.")

        while True:
            data = conn.recv(MAX_PACKET_SIZE).decode(FORMAT)
            cmd, msg = data.split("@")
            # Process commands from the client
            if cmd == "LIST":
                send_data = self.getList()
            elif cmd == "DELETE":
                send_data = self.deleteFile(msg)
            elif cmd == "UPLOAD":
                send_data = self.uploadFile(msg)
            elif cmd == "DOWNLOAD":
                send_data = self.downloadFile(msg)
            elif cmd == "DISCONNECTED":
                break
            conn.send(send_data.encode(FORMAT))
            
        print(f"[DISCONNECTED] {addr} disconnected")
        conn.close()

    def run(self):
        """
        Starts the server and listens for incoming connections.
        """
        self.socket_server.bind(self.ADDR_server)
        self.socket_server.listen()
        print(f"[LISTENING] Server is listening on {self.ip_server_tcp}:{self.port_server_tcp}")

        while self.running:
            conn, addr = self.socket_server.accept()
            # Handle each client connection in a new thread
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        self.socket_server.close()

if __name__ == "__main__":
    server_app().run()
