
import os
import logging
from logging.handlers import TimedRotatingFileHandler

def configura_logger():
    os.makedirs("log", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="|%(levelname)s| [%(asctime)s] %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )
    handler = TimedRotatingFileHandler(
        filename="log/tp_link.log",
        when="midnight",
        interval=1,
        backupCount=0,
        encoding="utf-8",
        utc=False,
    )
    handler.setFormatter(logging.Formatter("|%(levelname)s| [%(asctime)s] %(message)s"))
    logging.getLogger().addHandler(handler)
