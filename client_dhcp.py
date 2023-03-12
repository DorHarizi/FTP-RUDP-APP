
# import socket
#
#
# class client_dhcp:
#     def __init__(self):
#
#          #  Set up a socket
#     self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     self.server_socket.bind(('192.168.1.1', 4455))
#
# # Listen for DHCPDISCOVER messages
# while True:
#     message, client_address = server_socket.recvfrom(2048)
#     if message[0] == 1 and message[1] == 1 and message[2] == 6 and message[3] == 0:
#         # Send a DHCPOFFER message
#         offer_message = b'\x02\x01\x06\x00' + 236*b'\x00' + b'\x00\x00\x00\x00' + b'\xC0\xA8\x01\x64' + 192*b'\x00'
#         server_socket.sendto(offer_message, ('255.255.255.255', 68))
#
#         # Wait for a DHCPREQUEST message
#         message, client_address = server_socket.recvfrom(2048)
#         if message[0] == 1 and message[1] == 1 and message[2] == 6 and message[3] == 0:
#             # Send a DHCPACK message
#             ack_message = b'\x02\x01\x06\x00' + 236*b'\x00' + b'\x00\x00\x00\x00' + b'\xC0\xA8\x01\x64' + 192*b'\x00'
#             server_socket.sendto(ack_message, ('255.255.255.255', 68))


#############################################################################################################
import socket



class client_dhcp:

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 9999
    CODE_WORD = 'discovery'

    def send_message(message):
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('127.0.0.1', 6677))
            encoded_message = message.encode('utf-8')
            client_socket.sendall(encoded_message)
            ip_address = client_socket.recv(1024)
            return ip_address.decode('utf-8')

    if __name__ == '__main__':
        ip_address = send_message(CODE_WORD)
        print(f'Received IP address: {ip_address}')
    # def __init__(self):
    #     self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     self.ip_src = "0.0.0.0"
    #     self.port_dest = 9998
    #     self.run()
    #
    #
    #     def get_ip_add(self, data) -> str:
    #         self.socket.sendto(data.encode('utf-8'), (self.ip_src, self.port_dest))
    #         print(f"massege sent:{data}")
    #         ip_address, addr = self.socket.recvfrom(SIZE_PACKET)
    #         print(f"ip:{ip_address}")
    #         ip_address.decode('utf-8')
    #         print(f"ip:{ip_address}")
    #         return ip_address.decode('utf-8')
    #
    #     def run(self):
    #         self.socket.bind((self.ip_dest, 9999))
    #         print("the client is connected to the server")
    #
    #     def disconnect(self):
    #         print("the client disconnected from the server")
    #         self.socket.close()


