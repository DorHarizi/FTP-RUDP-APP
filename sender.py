import socket
import os
import threading
import time

MAX_PACKETS = 10
MAX_PACKET_SIZE = 1024


def send_packet(packet, host, port, sock):
    sock.sendto(packet, (host, port))
    while True:
        try:
            data, addr = sock.recvfrom(MAX_PACKET_SIZE)
            if data == b"ACK" and addr[0] == host:
                break
        except socket.timeout:
            sock.sendto(packet, (host, port))


def send_file(filename, host, port):

    with open(filename, "rb") as f:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        packets = []
        base = 0
        nextseqnum = 0

        while True:
            data = f.read(MAX_PACKET_SIZE)
            if not data:
                break
            packets.append(data)

        while base < len(packets):
            threads = []
            for i in range(base, min(base + MAX_PACKETS, len(packets))):
                packet = packets[i]
                t = threading.Thread(target=send_packet, args=(packet, host, port, sock))
                threads.append(t)
                t.start()

            start_time = time.time()
            for t in threads:
                t.join(1.0 - (time.time() - start_time))

            for i in range(base, min(base + MAX_PACKETS, len(packets))):
                if i == nextseqnum:
                    nextseqnum += 1
                    if base < nextseqnum:
                        base = nextseqnum

            if nextseqnum == len(packets):
                MAX_PACKETS += 1

            while nextseqnum >= base + MAX_PACKETS:
                time.sleep(0.01)

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
