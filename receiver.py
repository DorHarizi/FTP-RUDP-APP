import socket


def receive_file(filename, ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    with open(filename, "wb") as f:
        expectedseqnum = 0
        while True:
            data, addr = sock.recvfrom(1024)
            if not data:
                break
            seqnum = int.from_bytes(data[:4], byteorder="big")
            packet = data[4:]
            if seqnum == expectedseqnum:
                f.write(packet)
                expectedseqnum += 1
                sock.sendto(b"ACK", addr)
            elif seqnum < expectedseqnum:
                sock.sendto(b"ACK", addr)
            else:
                sock.sendto(b"ACK", addr)
    sock.close()


if __name__ == "__main__":
    receive_file("delete_big.png", "localhost", 1234)

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
# def deliver_data(data):
#     # return the process can continue
#     return data
#
#
# def extract(packet):
#     # decode the data from the packet that the sender send
#     return packet[0].decode('utf-8')
#
#
# def corrupt(data, check_sum):
#     rcv_checksum = checksum(data)
#     if rcv_checksum == check_sum:
#         return True
#     else:
#         return False
#
#
# def rdt_rcv(packet, address_source):
#     # reliable data transfer receive from the sender
#     data = exstract(packet)
#     if not corrupt(data, packet[1]):
#         deliver_data(data)
#     else:
#         pass
