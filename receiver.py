# import socket
import rudp_socket
from rudp_socket import RUDPSocket, RUDPPacket


def receive_file(filename, ip, port):

    # rudp_socket_inst = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # rudp_socket_inst.bind((ip, port))
    rudp_socket_inst = RUDPSocket()
    rudp_socket_inst.socket.bind(ip, port)
    print(f"{ip}, {port}")
    # list_packet = {}

    with open(filename, "wb") as f:
        print("write")
        expectedseqnum = 0
        while True:
            try:
                data , addr= rudp_socket_inst.socket.recvfrom(1024)
                packet = RUDPPacket.unpack(data)
                if packet.seqnum == -1:
                    break
                # print(data)
                ack_packet = RUDPPacket()
                ack_packet.seqnum = packet.seqnum
                if packet.seqnum == expectedseqnum:
                    f.write(packet.data)
                    f.flush()
                    print("write to the file")
                    expectedseqnum += 1
                    print(f"send ACK{packet.seqnum}")
                    rudp_socket_inst.sendto(data, addr)
                elif packet.seqnum < expectedseqnum:
                    print(f"send ACK{seqnum}")
                    rudp_socket_inst.sendto(data, addr)
            except Exception as e:
                print(e)
    print("close connection")
    rudp_socket_inst.socket.close()


if __name__ == "__main__":
    receive_file("server_files/delete_big.png", "localhost", 1234)

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
