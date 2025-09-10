


import config
import requests
from log_config import logger

def duck_dns_update(ip):
    DUCKDNS_TOKEN = config.DUCKDNS_TOKEN
    DUCKDNS_DOMAIN = config.DUCKDNS_DOMAIN

    url = f"https://www.duckdns.org/update?domains={DUCKDNS_DOMAIN}&token={DUCKDNS_TOKEN}&ip={ip}"
    response = requests.get(url)
    if response.status_code == 200 and "OK" in response.text:
        return True
    
    return False