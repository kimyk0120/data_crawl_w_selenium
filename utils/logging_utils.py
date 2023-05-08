import logging
import os
import os.path
import sys
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'logs')

def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(LOG_DIR, "debug_"+datetime.today().strftime("%Y%m%d")+".log")),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging