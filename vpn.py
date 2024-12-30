import os
from http.client import responses

import requests


def enable_vpn(proxy_host="164.92.82.207", proxy_port="28131"):
    os.environ["HTTP_PROXY"] = f"socks5h://{proxy_host}:{proxy_port}"
    os.environ["HTTPS_PROXY"] = f"socks5h://{proxy_host}:{proxy_port}"


def disable_vpn():
   os.environ.pop("HTTP_PROXY", None)
   os.environ.pop("HTTPS_PROXY", None)


def send_requests():
    response = requests.get("https://httpbin.org/ip", timeout=20)
    print(response.json())


send_requests()
enable_vpn()
send_requests()
disable_vpn()
send_requests()