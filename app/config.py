import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration for Fritz IP Updater
FRITZBOX_HOST = os.getenv("FRITZBOX_HOST", "fritz.box")
FRITZBOX_USER = os.getenv("FRITZBOX_USER", "user")
FRITZBOX_PASSWORD = os.getenv("FRITZBOX_PASSWORD", "password")

# DuckDNS Configuration
DUCKDNS_TOKEN = os.getenv("DUCKDNS_TOKEN", "token")
DUCKDNS_DOMAIN = os.getenv("DUCKDNS_DOMAIN", "domain")  # e.g., "entringer"

# Update Interval in minutes
UPDATE_INTERVAL_MINUTES = int(os.getenv("UPDATE_INTERVAL_MINUTES", "5"))

# Ensure data directory exists
os.makedirs("./data", exist_ok=True)