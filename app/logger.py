# logger.py

import logging
import os
from logging.handlers import RotatingFileHandler
from .context import correlation_id

# Folder exists
os.makedirs("logs", exist_ok=True)


class CorrelationIdFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = correlation_id.get()
        return True


logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

# ROTATION CONFIG
file_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=10_000,
    backupCount=3 
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s [corr_id=%(correlation_id)s] %(message)s"
)

file_handler.setFormatter(formatter)
file_handler.addFilter(CorrelationIdFilter())

logger.addHandler(file_handler)
