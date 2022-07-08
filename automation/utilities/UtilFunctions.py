import configparser
import os
from logging import config as c, getLogger
from automation.utilities import settings as s

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROPERTIES_PATH = os.path.join(ROOT_DIR, 'properties.ini')

class Utils:


    def get_config(self):
        config = configparser.RawConfigParser()
        config.read(PROPERTIES_PATH)
        return config

    def getLoggingConfig(self):
        c.dictConfig(s.LOGGING_DIC)
        log = getLogger('log_msg')
        return log

