from ipapi.api import Api


def main():
    client = Api(ip="1.1.1.1")
    ip_info = client.get_ip_info()
    country = client.get_country()
    print(ip_info)
    print(country)

    print("\n\n")

    self_ip = client.get_self_ip()
    self_country = client.get_self_country()
    print(self_ip)
    print(self_country)


main()
