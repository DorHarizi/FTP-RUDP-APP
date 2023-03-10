import os
import socket
import threading

class Server:

    def __init__(self, address='local host', tcp_port=50020, udp_port=50030 ):
        """
                Initialize the server.
                :param address: Server address
                :param tcp_port: TCP socket port
                :param udp_port: UDP socket ports
                :param num_of_streams: Number of UDP parallel streams
                """
        self.disable = []
        # AF_inet = IPv4 address family and SOCK_STREAM = TCP
        self.socket = socket(AF_INET, SOCK_STREAM)
        # UDP streams (sockets) list
        self.streams = []
        # UDP availability to download list
        self.available = []
        # Is the UDP stream transmitting
        self.streams_send = []
        self.funcs = []

        # self explanatory
        self.udp_port = udp_port
        self.num_of_streams = num_of_streams
        # file dicts for streams to send
        self.streams_download = []
        for _ in range(self.num_of_streams):
            self.available.append(True)
            self.streams_send.append(True)
            self.streams.append(socket(AF_INET, SOCK_DGRAM))
            self.streams_download.append({})
        # global locks
        self.lock = Lock()
        self.address = address
        # download queue (only one can download)
        self.download_queue = {}
        # bind the socket to the port number and host address (localhost) and listen for connections (5) at max,
        # at a time
        self.socket.bind((self.address, tcp_port))
        self.socket.listen(5)
        # create a list of clients to store the clients connected to the server
        self.clients = {}
        self.window_size = 5
        self.server_is_active = True
        # for tests
        self.last_msg = None