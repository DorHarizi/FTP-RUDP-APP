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
        Initializes the client with a UDP socket and binds to the DHCP
