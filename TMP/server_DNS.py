import logging
import socket
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Define the IP address and port number for the server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 53

# Define a dictionary of domain names and IP addresses
DNS_TABLE = {
    'example.com': '192.168.1.1',
    'google.com': '8.8.8.8',
    'app.local': '54.239.26.128'
}


def run():

    # Create a socket object for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP address and port number
    server_socket.bind((SERVER_IP, SERVER_PORT))

    while True:
        data, client_address = server_socket.recvfrom(1024)

        # Decode the data and extract the domain name
        domain_name = data.decode(encoding='utf-8').split('\x00')[0][12:]

        # Check if the domain name is in the DNS table
        if domain_name in DNS_TABLE:
            # Construct the DNS response packet
            response_packet = bytes.fromhex(' '.join([
                '00 00 81 80 00 01 00 01 00 00 00 00',
                ' '.join([f'{len(label):02x} {"".join([f"{ord(c):02x}" for c in label])}' for label in
                          domain_name.split('.')]),
                '00 00 01 00 01',
                ' '.join(['c0 0c 00 01 00 01 00 00 00 3c 00 04'] + [f'{int(part)}' for part in
                                                                    DNS_TABLE[domain_name].split('.')])
            ]))
        else:
            # Construct a response indicating that the domain name was not found
            response_packet = bytes.fromhex(' '.join([
                '00 00 81 83 00 01 00 00 00 00 00 00',
                ' '.join([f'{len(label):02x} {"".join([f"{ord(c):02x}" for c in label])}' for label in
                          domain_name.split('.')]),
                '00 00 01 00 01',
                'c0 0c 00 01 00 01 00 00 00 3c 00 04 0a 00 00 01'
            ]))

        # Send the DNS response packet back to the client
        server_socket.sendto(response_packet, client_address)


if __name__ == "__main__":

    logger.info('running dns server')
    run()