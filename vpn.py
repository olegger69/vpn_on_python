import os
import requests

def enable_vpn(proxy_host="", proxy_port=""):
    os.environ["HTTP_PROXY"] = f"socks5h://{proxy_host}:{proxy_port}"
    os.environ["HTTPS_PROXY"] = f"socks5h://{proxy_host}:{proxy_port}"