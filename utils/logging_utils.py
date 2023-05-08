import logging
import os
import os.path
import sys
from datetime import datetime

class Logger:
    def __init__(self, *args, **kwargs):
        self.LOG_DIR = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'logs')
        self.logging = self.set_logger()
    def set_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(os.path.join(self.LOG_DIR, "debug_"+datetime.today().strftime("%Y%m%d")+".log")),
                logging.StreamHandler(sys.stdout)
            ]
        )
        return logging

    def get_logger(self) -> logging:
        return self.logging
