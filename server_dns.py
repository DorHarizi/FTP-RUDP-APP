import socket
import threading

SIZE_PACKET = 1024

class server_dns:
    """
    A simple DNS server implementation that resolves domain names to IP addresses.
    
    Attributes:
        socket (socket.socket): The UDP socket for receiving and sending data.
        dns_table (dict): A dictionary mapping domain names to their IP addresses.
        ip (str): The IP address of the server.
        port (int): The port on which the server listens for incoming DNS queries.
        connected (bool): Flag indicating if the server is currently running.
    """

    def __init__(self):
        """
        Initializes the DNS server with a UDP socket and binds it to a specified port.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
        self.dns_table = {}  # Initialize the DNS table as an empty dictionary
        self.ip = socket.gethostbyname(socket.gethostname())  # Get the local host IP
        self.port = 9998  # Define the port number for DNS queries
        self.connected = True  # Set the connected flag to True
        self.run()  # Start the server

    def run(self):
        """
        Binds the socket to the server IP and port, then listens for incoming DNS queries.
        
        For each query received, the server attempts to resolve the domain name. If the domain name
        is found in the internal DNS table or can be resolved using socket.gethostbyname, it sends back
        the corresponding IP address. Otherwise, it responds with an error message.
        """
        self.socket.bind((self.ip, self.port))  # Bind the socket to the server IP and port
        print(f"[LISTENING] Server is listening on IP:{self.ip} PORT:{self.port}")

        while self.connected:
            data, addr = self.socket.recvfrom(SIZE_PACKET)  # Receive DNS query
            domain_name = data.decode('utf-8')  # Decode the domain name from the query

            # Check if the domain name is in the internal DNS table
            if domain_name in self.dns_table:
                # Send the corresponding IP address back to the client
                self.socket.sendto(self.dns_table[domain_name].encode('utf-8'), addr)
                print(f"in if: domain_name:{domain_name}, ip domain_name:{self.dns_table[domain_name]}")
            else:
                try:
                    # Attempt to resolve the domain name externally
                    ip_address = socket.gethostbyname(domain_name)
                    self.dns_table[domain_name] = ip_address  # Add the resolved IP to the DNS table
                except:
                    # Handle the case where the domain name cannot be resolved
                    ip_address = "NO VALUE, PLEASE TRY AGAIN"
                # Send the resolved IP address or error message back to the client
                self.socket.sendto(ip_address.encode('utf-8'), addr)
                print(f"domain_name:{domain_name}, ip with port:{addr}")
        
        print("Server DNS close")
        self.socket.close()  # Close the socket when the server stops running

if __name__ == "__main__":
    server_dns().run()  # Instantiate and run the server
