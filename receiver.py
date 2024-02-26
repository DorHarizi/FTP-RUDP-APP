import socket

def receive_file(filename, ip, port):
    """
    Receives a file over UDP, implementing basic reliability through sequence numbers.

    This function sets up a UDP socket to receive packets of a file being sent to it. It ensures
    that packets are processed in the correct order by checking sequence numbers, writing the data
    to a file, and sending acknowledgments (ACKs) back to the sender for each packet received in order.

    Parameters:
    - filename: The name of the file to save the received data to.
    - ip: The IP address to bind the receiving socket to.
    - port: The port number on which to listen for incoming data.
    """
    # Create and bind a UDP socket to the specified IP and port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"Listening on {ip}, port {port}")

    with open(filename, "wb") as f:
        expectedseqnum = 0  # Initialize the expected sequence number to 0
        while True:
            data, addr = sock.recvfrom(1024)  # Receive data packet
            seqnum = int.from_bytes(data[:4], byteorder="big", signed=True)  # Extract sequence number
            print(f"Received packet with sequence number: {seqnum}")
            packet = data[4:]  # Actual file data starts from byte 4

            if seqnum == -1:
                # A sequence number of -1 indicates the end of file transfer
                break

            if seqnum == expectedseqnum:
                # If the packet is the one we're expecting, write to file and increment expected sequence number
                f.write(packet)
                f.flush()  # Ensure data is written to disk
                expectedseqnum += 1
                print(f"Sending ACK for sequence number: {seqnum}")
                sock.sendto(data[:4], addr)  # Send ACK for the received packet
            elif seqnum < expectedseqnum:
                # If an earlier packet is received, resend the ACK (it may have been lost)
                print(f"Resending ACK for sequence number: {seqnum}")
                sock.sendto(data[:4], addr)

    print("File transfer complete, connection closed.")
    sock.close()  # Close the socket once file transfer is complete

if __name__ == "__main__":
    receive_file("path/to/your/file.png", "localhost", 1234)
