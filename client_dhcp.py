import socket
import threading

FORMAT = 'utf-8'

class client_dhcp:
    """
    A simplified DHCP client simulation.

    This class implements the basic functionality of a DHCP client, capable of sending
    a discovery message to a DHCP server, receiving an IP address offer, and sending
    an acknowledgment for the received IP address.

    Attributes:
        socket (socket.socket): UDP socket for sending and receiving messages.
        ip (str): IP address of the client, determined by the hostname.
        port (int): The port number used by the client (default is 68, the DHCP client port).
        ip_table (dict): A dictionary to store IP addresses (unused in this snippet).
        ip_rcv (str): The received IP address from the server.
        is_connected (bool): Flag to indicate if the client is connected.
    """

    def __init__(self):
        """
        Initializes the client with a UDP socket and binds to the DHCP client port (68).
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
        self.ip = socket.gethostbyname(socket.gethostname())  # Client's IP address
        self.port = 68  # DHCP client port
        self.ip_table = {}  # Unused in this snippet
        self.ip_rcv = ""  # Received IP address
        self.is_connected = True  # Connection flag

    def send_message(self):
        """
        Sends a DHCP discovery message to the DHCP server.
        """
        print("Discovery Message")
        self.socket.sendto("discovery".encode(FORMAT), (self.ip, self.port))
        print("Message sent")

    def get_ip(self):
        """
        Sends a DHCP discovery message and waits for an IP offer from the DHCP server.
        Upon receiving an offer, it sends an acknowledgment.

        Returns:
            str: The new IP address assigned by the DHCP server.
        """
        self.socket.sendto("discovery".encode(FORMAT), (self.ip, self.port))
        new_ip, addr = self.socket.recvfrom(1024)  # Receive the offered IP address
        new_ip = new_ip.decode(FORMAT)
        print(f"The new IP is {new_ip}")
        print("I want this IP")
        self.socket.sendto("ACK".encode(FORMAT), (self.ip, self.port))  # Send acknowledgment
        return new_ip

    def run(self):
        """
        Binds the client socket to its IP and port, and marks the client as connected to the server.
        """
        self.socket.bind((self.ip, self.port))
        print("The client is connected to the server.")

    def disconnect(self):
        """
        Closes the client socket and marks the client as disconnected from the server.
        """
        print("The client disconnected from the server.")
        self.socket.close()

if __name__ == "__main__":
    client_dhcp().get_ip()
