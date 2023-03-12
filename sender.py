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
        flag2 = False

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
    send_file("mr_pro/delete_big.png", "localhost", 1234)

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


########################################################################################################################
# def send_packet(packet, host, port, sock):
#     # Send packet
#     sock.sendto(packet, (host, port))
#     # Wait for ACK
#     while True:
#         try:
#             data, addr = sock.recvfrom(1024)
#             if data == b"ACK" and addr[0] == host:
#                 break
#         except socket.timeout:
#             # Resend packet
#             sock.sendto(packet, (host, port))
#
#
# def send_file(filename, host, port):
#     # Open file for reading
#     with open(filename, "rb") as f:
#         # Create UDP socket
#         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         sock.settimeout(1)
#
#         # Split file into packets
#         packets = []
#         while True:
#             data = f.read(MAX_PACKET_SIZE)
#             if not data:
#                 break
#             packets.append(data)
#
#         # Send packets using multiple threads
#         base = 0
#         nextseqnum = 0
#         while base < len(packets):
#             # Send packets in current window
#             threads = []
#             for i in range(base, min(base + WINDOW_SIZE, len(packets))):
#                 packet = packets[i]
#                 t = threading.Thread(target=send_packet, args=(packet, host, port, sock))
#                 threads.append(t)
#                 t.start()
#
#             # Wait for threads to complete or timeout
#             start_time = time.time()
#             for t in threads:
#                 t.join(1.0 - (time.time() - start_time))
#
#             # Update base and nextseqnum
#             for i in range(base, min(base + WINDOW_SIZE, len(packets))):
#                 if i == nextseqnum:
#                     nextseqnum += 1
#                     if base < nextseqnum:
#                         base = nextseqnum
#
#             # Congestion control: increase window size if all packets are ACKed
#             if nextseqnum == len(packets):
#                 WINDOW_SIZE += 1
#
#             # Flow control: wait if the send buffer is full
#             while nextseqnum >= base + WINDOW_SIZE:
#                 time.sleep(0.01)
#
#         # Close socket
#         sock.close()
#
#
# if __name__ == "__main__":
#     send_file("filename.txt", "localhost", 1234)
