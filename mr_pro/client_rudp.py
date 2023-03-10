import socket
import time

import sender

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
CLIENT_DATA_PATH = "../client_files"
SERVER_DATA_PATH = ""


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "msg":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))

        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break

        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))

        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))

        elif cmd == "UPLOAD":
            path = f"{CLIENT_DATA_PATH}/{data[1]}"
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            time.sleep(5)
            sender.send_file(path, ADDR[0], 9999)

        elif cmd == "DOWNLOAD":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            filename = data[1]
            filename = f"{CLIENT_DATA_PATH}/{filename}"
            time.sleep(5)
            receiver.receive_file(filename, IP, 9999)
            print(f"the file downloaded {filename}")

        else:
            client.send("WRONG".encode(FORMAT))

    print("Disconnected from the server.")
    client.close()


if __name__ == "__main__":
    main()
