
import logging
from logging.handlers import TimedRotatingFileHandler
import config

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = TimedRotatingFileHandler(
    filename='./data/fritz_ip_updater.log',
    when='D',  # Rotate daily
    interval=1,
    backupCount=config.LOG_RETENTION_DAYS,  # Retain logs for specified days
    encoding='utf-8'
)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        file_handler,
        stream_handler
    ]
)

logger = logging.getLogger(__name__)
