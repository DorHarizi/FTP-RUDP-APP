import socket
import os
import threading
import time

MAX_PACKETS = 10
MAX_PACKET_SIZE = 1020


def send_packet(packet, host, port, sock):
    sock.sendto(packet, (host, port))
    print(f"number packet send is: {int.from_bytes(packet[:4], byteorder='big',signed=True)}")


def send_file(filename, host, port):
    finish = -1
    finish = finish.to_bytes(4, byteorder="big", signed=True)
    with open(filename, "rb") as f:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        packets = []
        base = 0
        index = 0
        last_ack = -1

        while True:
            data = f.read(MAX_PACKET_SIZE)
            suq = index.to_bytes(4, byteorder="big",signed=True)
            if not data:
                break
            packets.append(suq + data)
            index += 1

        while last_ack + 1 < len(packets):
            flag = True
            while flag:
                flag = False
                count = 0
                for i in range(base, min(base + MAX_PACKETS, len(packets))):
                    if last_ack < i:
                        print("packet")
                        packet = packets[i]
                        send_packet(packet, host, port, sock)
                        count += 1
                for j in range(count):
                    try:
                        data, addr = sock.recvfrom(4)
                        num = int.from_bytes(data[:4], byteorder="big", signed=True)
                        print(f"expected ACK {num}")
                        if last_ack < num:
                            last_ack = num
                    except socket.timeout:
                        flag = True
            base = last_ack
        print("close connection")
        sock.sendto(finish, (host, port))
        sock.close()
