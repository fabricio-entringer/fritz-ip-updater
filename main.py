from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzConnectionException
from fritzconnection.lib.fritzstatus import FritzStatus

import config
from duck_dns import duck_dns_update

from log_config import logger

def get_fritzbox_status(host, user, password):
    try:
        fc = FritzConnection(address=host, user=user, password=password)
        fs = FritzStatus(fc)

        return {
            'bytes_sent': fs.bytes_sent,
            'bytes_received': fs.bytes_received,
            'device_uptime': fs.device_uptime,
            'external_ip': fs.external_ip
        }
    except FritzConnectionException as e:
        return {'error': str(e)}
    

def get_last_ip():
    try:
        with open("./data/last_ip.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
    

def save_last_ip(ip):
    with open("./data/last_ip.txt", "w") as file:
        file.write(ip)


if __name__ == "__main__":
    logger.info("Starting Fritz IP Updater...")
    host = config.FRITZBOX_HOST
    user = config.FRITZBOX_USER
    password = config.FRITZBOX_PASSWORD

    try:
        fritzbox_status = get_fritzbox_status(host, user, password)
        external_ip = fritzbox_status.get('external_ip')
        last_ip = get_last_ip()

        if external_ip != last_ip:
            logger.info(f"IP change detected: {last_ip} -> {external_ip}")
            if duck_dns_update(external_ip):
                save_last_ip(external_ip)
                logger.info("DuckDNS updated successfully.")
            else:
                logger.error("Failed to update DuckDNS.")
            # Here you would add the logic to update your dynamic DNS service
        else:
            logger.info(f"No IP change detected. Current IP is still {external_ip}.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
