import socket
import threading

SIZE_PACKET = 1024

class client_dns:
    """
    A simple DNS client simulation.

    This class implements basic functionality of a DNS client, capable of sending
    DNS query messages to a DNS server and receiving responses containing IP addresses.

    Attributes:
        socket (socket.socket): UDP socket for sending and receiving DNS queries.
        ip_dest (str): IP address of the DNS server.
        port_dest (int): The port number of the DNS server (default is 9998).
        connected (bool): Flag to indicate if the client is connected to the DNS server.
    """

    def __init__(self):
        """
        Initializes the DNS client with a UDP socket and sets up the destination IP and port.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
        self.ip_dest = socket.gethostbyname(socket.gethostname())  # DNS server IP address
        self.port_dest = 9998  # DNS server port
        self.connected = True  # Connection flag
        self.run()

    def get_req(self, data) -> str:
        """
        Sends a DNS query to the DNS server and waits for a response.

        Parameters:
            data (str): The domain name to query about.

        Returns:
            str: The IP address received from the DNS server as a response to the query.
        """
        self.socket.sendto(data.encode('utf-8'), (self.ip_dest, self.port_dest))
        print(f"Message sent: {data}")
        ip_address, addr = self.socket.recvfrom(SIZE_PACKET)  # Receive the response
        ip_address = ip_address.decode('utf-8')  # Decode the received IP address
        print(f"IP address received: {ip_address}")
        return ip_address

    def run(self):
        """
        Binds the client socket to its IP and port, and marks the client as connected to the server.
        """
        self.socket.bind((self.ip_dest, 9999))  # Client listening port
        print("The client is connected to the server.")

    def disconnect(self):
        """
        Closes the client socket and marks the client as disconnected from the server.
        """
        print("The client disconnected from the server.")
        self.socket.close()
