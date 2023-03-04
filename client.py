import socket
import receiver

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    receiver.receive_file('client_files/delete_big.png', IP, PORT)


if __name__ == "__main__":
    main()