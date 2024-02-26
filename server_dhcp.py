import socket
import threading

# Server configuration constants
SERVER_IP = '127.0.0.1'  # Loopback address for local testing
SERVER_PORT = 68  # Standard port number for DHCP server
IP_ADDRESS_PREFIX = '192.168.0.'  # Prefix for the IP addresses to be assigned
IP_ADDRESS_SUFFIX = 1  # Starting suffix to generate unique IP addresses

# A dictionary to map client addresses to their assigned IP addresses
client_ip_map = {}

class server_dhcp:
    """
    A simple DHCP server simulation.

    This server assigns unique IP addresses to clients upon receiving a DHCP discovery message
    and keeps track of the assigned IP addresses to avoid duplicates.
    """

    def __init__(self):
        """
        Initializes the DHCP server with a UDP socket.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
        self.ip = socket.gethostbyname(socket.gethostname())  # Server's IP address
        self.port = SERVER_PORT  # DHCP server port
        self.connected = True  # Server's running state

    def assign_ip_address(self, client_address):
        """
        Assigns a unique IP address to a client or retrieves an existing assignment.

        Parameters:
        - client_address: The address of the client requesting an IP.

        Returns:
        - The assigned or existing IP address for the client.
        """
        global IP_ADDRESS_SUFFIX
        if client_address in client_ip_map:
            # Client already has an assigned IP
            print(f'{client_address} already has an IP address of {client_ip_map[client_address]}')
            return client_ip_map[client_address]
        else:
            # Assign a new IP address to the client
            ip_address = IP_ADDRESS_PREFIX + str(IP_ADDRESS_SUFFIX)
            IP_ADDRESS_SUFFIX += 1  # Increment the suffix for the next assignment
            client_ip_map[client_address] = ip_address
            print(f'{client_address} has been assigned IP address {ip_address}')
            return ip_address

    def run(self):
        """
        Binds the server to its IP and port, then listens for and processes DHCP messages.
        """
        self.socket.bind((self.ip, self.port))
        print(f"[LISTENING] Server is listening on IP:{self.ip} PORT:{self.port}")

        while self.connected:
            msg, addr = self.socket.recvfrom(1024)  # Wait for a message from a client
            if msg.decode() == "discovery":
                # Assign a new IP address upon DHCP discovery message
                new_ip = self.assign_ip_address(addr[0])
                self.socket.sendto(new_ip.encode(), addr)
            elif msg.decode('utf-8') == "ACK":
                # Log receipt of ACK message (confirmation of IP address acceptance)
                print(f"Received ACK for {addr[0]}")

if __name__ == "__main__":
    server_dhcp().run()  # Instantiate and run the DHCP server
