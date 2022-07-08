
import os
import time
import datetime

# Time format
timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
log_timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%H-%M-%S')
## Get the current running path of the project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_PATH = os.path.join(ROOT_DIR, f'Logs/{log_timestamp}.logs')
LOG_FORMAT = '%(asctime)s: %(levelname)s: %(message)s:'


PROPERTIES_PATH = os.path.join(ROOT_DIR, 'properties.ini')

#PROJECT SETTINGS

# LOGGING
standard_format = '[%(asctime)s][%(filename)s][%(funcName)20s():%(lineno)d]' \
                  '[%(levelname)s]%(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d][%(funcName)20s() ]%(message)s'

test_format = '[%(asctime)s] %(message)s'

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    'handlers': {
        # Print to the log
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # Print to the screen
            'formatter': 'simple'
        },

        # Print to the log, collect the log of Info and above
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # Save to file, log wheel
            'formatter': 'standard',
            'filename': LOG_PATH,  # Log file
            'maxBytes': 1024 * 1024 * 5,  # 5m
            'backupCount': 5,
            'encoding': 'utf-8',  # , no need to worry about Chinese log garbled
        },
    },
    'loggers': {
        # Logging.getlogger (__ name__) Logger configuration
        'log_msg': {
            'handlers': ['default', 'console'],
            # He is here to add the two handles defined above, that is, the log data writes to the file and prints to the screen.
            'level': 'DEBUG',  # Loggers (First Layer Log Level Limit) ---> Handlers (Layer Log Level Tips)
            'propagate': False,
            # TRUE, the up (higher LEVEL logger) passed, usually set to false, otherwise a log will be transferred upward
        },
    },
}