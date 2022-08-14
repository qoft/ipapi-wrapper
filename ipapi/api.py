import httpx


class Api:
    def __init__(self, ip: str = None):
        self.ip = ip
        self.url = f"https://ipapi.co/{ip}/"
        self.client = httpx.Client(base_url=self.url)

    def get_ip_info(self):
        return self.client.get("json").json()

    def get_country(self):
        return self.client.get("country").text

    def get_self_ip(self):
        return httpx.get("https://ipapi.co/ip").text

    def get_self_country(self):
        return httpx.get("https://ipapi.co/country").text