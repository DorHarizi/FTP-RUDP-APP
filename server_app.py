
import os
import socket
import threading

import receiver

MAX_PACKET_SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = 'server_files'


class server_app:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 9999
        self.ADDR = (self.ip, self.port)
        self.list_files = []
        files = os.listdir('server_files')
        if not len(files) == 0:
            for f in files:
                self.list_files.append(f)
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening = True
        self.run()

    def deleteFile(self, file_name):
        send_data = ""
        if file_name in self.list_files:
            os.remove(f"{SERVER_DATA_PATH}/{filename}")
            send_data += "File deleted successfully."
        else:
            send_data += "File not found."
        return send_data

    def getList(self):
        send_data = ""
        if len(self.list_files) == 0:
            send_data = "The server directory is empty"
        else:
            for file in self.list_files:
                send_data += f"{file}\n"
        return send_data

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        while True:
            cmd = conn.recv(MAX_PACKET_SIZE).decode(FORMAT)

            if cmd == "LIST":
                send_data = self.getList()
                conn.send(send_data.encode(FORMAT))

            elif cmd == "DELETE":
                filename = data[1]
                send_data = "msg@"
                send_data += self.deleteFile(filename)
                print(f"{send_data}, {filename}")
                conn.send(send_data.encode(FORMAT))

            elif cmd == "UPLOAD":
                send_data = "msg@"
                filename = data[1]
                filename = f"{SERVER_DATA_PATH}/{filename}"
                receiver.receive_file(filename, IP, 9999)
                print(f"the file uploaded {filename}")
                send_data += "the file uploaded"
                conn.send(send_data.encode(FORMAT))

            elif cmd == "DOWNLOAD":
                path = f"{SERVER_DATA_PATH}/{data[1]}"
                client.send(f"{cmd}@{data[1]}".encode(FORMAT))
                sender.send_file(path, ADDR[0], 9999)

            elif cmd == "DISCONNECTED":
                break
        print(f"[DISCONNECTED] {addr} disconnected")
        conn.close()


    def run(self):
        print("[STARTING] Server is starting")
        self.socket_server.bind((self.ip, self.port))
        self.socket_server.listen()
        print(f"[LISTENING] Server is listening on IP:{self.ip} PORT:{self.port}")

        while self.listening:
            conn, addr = self.socket_server.accept()
            thread = threading.Thread(target=handle_client, args=(self, conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        self.socket_server.close()


