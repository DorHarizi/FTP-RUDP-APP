import socket
import os
import threading
import time

MAX_PACKETS = 10  # Maximum packets to send before waiting for ACK
MAX_PACKET_SIZE = 1020  # Maximum data payload size in bytes for each packet

def send_packet(packet, host, port, sock):
    """
    Sends a single packet to a specified host and port using a given socket.
    
    Parameters:
    - packet: The packet data to be sent.
    - host: The destination host IP address.
    - port: The destination port number.
    - sock: The socket object used for sending the packet.
    """
    sock.sendto(packet, (host, port))
    print(f"Number packet sent is: {int.from_bytes(packet[:4], byteorder='big',signed=True)}")

def send_file(filename, host, port):
    """
    Sends a file to a specified host and port, breaking the file into packets,
    and managing acknowledgments to ensure reliable transfer.
    
    Parameters:
    - filename: The path to the file to be sent.
    - host: The destination host IP address.
    - port: The destination port number.
    """
    finish = -1
    finish = finish.to_bytes(4, byteorder="big", signed=True)  # Finish packet marker
    with open(filename, "rb") as f:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)  # Set socket timeout for ACK waiting
        packets = []  # To hold all file packets
        base = 0  # Base index for window
        index = 0  # Packet sequence number
        last_ack = -1  # Last ACK received

        # Read the file and create packets
        while True:
            data = f.read(MAX_PACKET_SIZE)
            seq = index.to_bytes(4, byteorder="big",signed=True)  # Packet sequence number
            if not data:
                break  # End of file
            packets.append(seq + data)  # Add packet to the list
            index += 1

        # Send packets and manage ACKs
        while last_ack + 1 < len(packets):
            flag = True
            while flag:
                flag = False
                count = 0  # Count of packets sent
                # Send window of packets
                for i in range(base, min(base + MAX_PACKETS, len(packets))):
                    if last_ack < i:
                        print("Sending packet")
                        packet = packets[i]
                        send_packet(packet, host, port, sock)
                        count += 1
                # Receive ACKs
                for j in range(count):
                    try:
                        data, addr = sock.recvfrom(4)
                        num = int.from_bytes(data[:4], byteorder="big", signed=True)
                        print(f"Expected ACK {num}")
                        if last_ack < num:
                            last_ack = num
                    except socket.timeout:
                        flag = True  # Timeout, retransmit window
            base = last_ack + 1  # Move window

        print("Closing connection")
        sock.sendto(finish, (host, port))  # Send finish packet
        sock.close()

if __name__ == "__main__":
    send_file('path/to/your/file', 'destination_host_ip', 9999)
