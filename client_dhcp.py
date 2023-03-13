
# import socket
#
#
#
# class client_dhcp:

    #   def __init__(self, port_dhcp):
    #
    #     self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     self.ip = "0.0.0.0"
    #     self.port = port_dhcp
    #     self.ip_table = {}
    #     self.ip_rcv = ""
    #     self.is_connected = True
    #     self.run()
    #
    #
    #
    #
    #  def send_message(self, message):
    #
    #      message = message.encode('utf-8')
    #      print(f"massege sent:{message}")
    #      self.socket.sendto(message, (self.ip, self.port))
    #      while i < 2:
    #         data = self.socket.recv(1024).decode('utf-8')
    #             if data == "ACK":
    #                  print(f"The IP of the client from the dhcp server is: {self.ip_rcv}")
    #                  print("the connection is done")
    #                  i=1
    #             else:
    #                 self.ip = data
    #                 print(f"this is the chosen ip{self.ip}")
    #                 i=2
    #
    #
    # def disconnect(self):
    #             print("the client disconnected from the server")
    #             self.socket.close()
    #
    #
    #
