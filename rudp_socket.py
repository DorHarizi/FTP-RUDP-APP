import socket
import os
import threading
import time
import struct

MAX_PACKET_SIZE = 1020
FORMAT = 'utf-8'


class RUDPSocket:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.seqnum = 0
        self.last_ack = -1
        self.current_window = 1

    def sendto(self, data, address: (str, int)):
        # print(f"packet send{data.from_bytes(data[:4], byteorder='big', signed=True)}")
        self.socket.sendto(data, address)



class RUDPPacket:
    """ RUDP packet class"""
    TYPE_DATA = 1
    TYPE_SYN = 2
    TYPE_ACK = 4
    TYPE_FIN = 5

    def __init__(self):
        self.seqnum = 0
        self.data = b""


    def pack(self):
        self.seqnum = self.seqnum.to_bytes(4, byteorder="big", signed=True)
        packet = self.seqnum + self.data
        return packet

    @classmethod
    def unpack(cls, binary_data):
        inst = cls()
        seqnum = int.from_bytes(binary_data[:4], byteorder="big", signed=True)
        inst.data = binary_data[4:]
        inst.seqnum = seqnum
        return inst


if __name__ == "__main__":
    a = RUDPPacket.unpack( int(4).to_bytes(4, byteorder="big", signed=True) + b'Shlomi')
    print(a.data)
    print(a.seqnum)
