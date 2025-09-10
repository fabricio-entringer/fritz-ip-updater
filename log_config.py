
import logging
import config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('./data/fritz_ip_updater.log'),
        logging.StreamHandler()  # This keeps console output too
    ]
)

logger = logging.getLogger(__name__)
