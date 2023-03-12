import client_dns
import client_app
import client_dhcp


class client:

    def __init__(self):
        self.client_dns = client_dns.client_dns()
        self.client_dhcp = client_dhcp.client_dhcp()
        self.client_app = client_app.client_app()
