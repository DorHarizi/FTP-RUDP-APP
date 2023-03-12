import server_dns as dns
import server_app as app
# import server_dhcp as dhcp


class server:
    def __init__(self):
        self.server_dns = dns.server_dns()
        self.server_app = app.server_app()
        # self.server_dhcp = dhcp.server_dhcp()
        self.run()

    def run(self):
        self.server_dns.run()
        self.server_app.run()
        # self.server_dhcp.run()