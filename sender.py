import socket
import os
import threading
import time

MAX_PACKET_SIZE = 1020


def increase_win() -> int:
    pass


def decrease_win() -> int:
    pass


def increase_time() -> int:
    pass


def decrease_time() -> int:
    pass


def send_packet(packet, host, port, sock):
    sock.sendto(packet, (host, port))
    print(f"packet send{int.from_bytes(packet[:4], byteorder='big', signed=True)}")


def send_file(filename, host, port):
    window = 1
    finish = -1
    finish = finish.to_bytes(4, byteorder="big", signed=True)
    with open(filename, "rb") as f:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"{host}, {port}")
        sock.settimeout(1)
        packets = []
        base = 0
        index = 0
        last_ack = -1

        while True:
            data = f.read(MAX_PACKET_SIZE)
            suq = index.to_bytes(4, byteorder="big", signed=True)
            if not data:
                break
            packets.append(suq + data)
            index += 1

        while last_ack + 1 < len(packets):
            flag = True
            while flag:
                flag = False
                count = 0
                for i in range(last_ack + 1, min(base + window, len(packets))):
                    packet = packets[i]
                    send_packet(packet, host, port, sock)
                    count += 1
                for j in range(count):
                    try:
                        data, addr = sock.recvfrom(4)
                        num = int.from_bytes(data[:4], byteorder="big", signed=True)
                        if last_ack < num:
                            last_ack = num
                        else:
                            sock.settimeout(increase_time())
                    except socket.timeout:
                        sock.settimeout(increase_time())
                        window = (decrease_win())
                        flag2 = True
                        flag = True
            if not flag2:
                sock.settimeout(decrease_time())
                window = (increase_win())
            base = last_ack

        print("close connection")
        sock.sendto(finish, (host, port))
        sock.close()


if __name__ == "__main__":
    send_file("delete_big.png", "localhost", 1234)

#
# def checksum(data):
#     checksum = 0
#     for byte in data:
#         checksum += byte
#         if checksum > 0xFF:
#             checksum &= 0xFF
#             checksum += 1
#     return checksum
#
#
# def udt_send(packet, address_dest):
#     # unreliable data transfer send (udp)
#     sock.sendto(packet, (address_dest[0], address_dest[1]))
#
#
# def make_packet(data):
#     # encode the data
#     packet = (data.encode('utf-8'), checksum(data))
#     return packet
#
#
# def rdt_send(data, address_dest):
#     # reliable data transfer send
#     packet = make_packet(data)
#     udt_send(packet, address_dest)
