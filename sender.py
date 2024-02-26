import socket
import os

# Constants defining the packet behavior and transmission properties.
MAX_PACKETS = 10  # The window size for the number of packets sent before requiring an ACK.
MAX_PACKET_SIZE = 1020  # The size of the data payload in each packet.

def send_packet(packet, host, port, sock):
    """
    Sends a single packet to the specified destination using UDP.
    
    This function is responsible for the actual transmission of a data packet. It also logs the sequence
    number of the packet being sent, providing visibility into the packet flow.

    Parameters:
    - packet: The data packet to be sent, including its sequence number.
    - host: IP address of the destination.
    - port: Port number at the destination.
    - sock: The UDP socket through which the packet is sent.
    """
    sock.sendto(packet, (host, port))
    print(f"Packet with sequence number {int.from_bytes(packet[:4], byteorder='big', signed=True)} sent.")

def send_file(filename, host, port):
    """
    Implements a simple reliable file transfer over UDP by splitting the file into packets,
    transmitting these packets within a sliding window, and handling acknowledgments (ACKs)
    to ensure all packets are received in order.

    Parameters:
    - filename: Path to the file to be sent.
    - host: Destination host IP address.
    - port: Destination port number.
    """
    # Special packet to signify the end of the file transfer.
    finish = (-1).to_bytes(4, byteorder="big", signed=True)

    # Initialize socket and set a timeout for ACKs.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)

    packets = []  # Stores the packets to be sent.
    base = 0  # Tracks the beginning of the sliding window.
    index = 0  # Sequence number for the packets.
    last_ack = -1  # The last sequence number acknowledged by the receiver.

    # Open the file, read its contents, and prepare packets.
    with open(filename, "rb") as f:
        while True:
            data = f.read(MAX_PACKET_SIZE)
            if not data:
                break  # End of file reached.
            seq = index.to_bytes(4, byteorder="big", signed=True)
            packets.append(seq + data)  # Append sequence number to data payload.
            index += 1

    # Begin sending packets and managing ACKs within the sliding window.
    while last_ack + 1 < len(packets):
        # Attempt to send and acknowledge all packets in the window.
        flag = True  # Indicates if we need to resend packets due to timeout.
        while flag:
            flag = False
            count = 0  # Number of packets sent in this iteration.
            for i in range(base, min(base + MAX_PACKETS, len(packets))):
                if i > last_ack:
                    send_packet(packets[i], host, port, sock)
                    count += 1
            # Wait for ACKs.
            for _ in range(count):
                try:
                    ack, _ = sock.recvfrom(4)
                    ack_num = int.from_bytes(ack, byteorder="big", signed=True)
                    if ack_num > last_ack:
                        last_ack = ack_num
                        flag = False  # ACK received, no need to resend.
                except socket.timeout:
                    flag = True  # Timeout occurred, resend packets in the window.
            base = last_ack + 1  # Slide the window forward based on the last ACK received.

    # Transmission complete, send the finish signal and close the socket.
    print("File transfer complete. Closing connection.")
    sock.sendto(finish, (host, port))
    sock.close()

if __name__ == "__main__":
    send_file('path/to/your/file', 'destination_host_ip', 9999)
