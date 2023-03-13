import os
import socket
import threading

import receiver

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
MAX_PACKET_SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = 'server_files'


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("msg@Welcome to the File Server.".encode(FORMAT))

    while True:
        data = conn.recv(MAX_PACKET_SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == "LIST":
            files = os.listdir('server_files')
            send_data = "msg@"

            if len(files) == 0:
                send_data += "The server directory is empty"
            else:
                send_data += "\n".join(f for f in files)
            conn.send(send_data.encode(FORMAT))

        elif cmd == "DELETE":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "msg@"
            filename = data[1]
            print(f"{filename}")

            if len(files) == 0:
                send_data += "The server directory is empty"
            else:
                if filename in files:
                    os.remove(f"{SERVER_DATA_PATH}/{filename}")
                    send_data += "File deleted successfully."
                else:
                    send_data += "File not found."
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

        else:
            conn.send(f"msg@Command does not exist".encode(FORMAT))

    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()


def start_server():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on IP:{IP} PORT:{PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


start_server()
