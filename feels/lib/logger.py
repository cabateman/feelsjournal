import logging
#from logging.handlers import SysLogHandler
from logging.handlers import SysLogHandler, TimedRotatingFileHandler
from os import path
from config import LOGGING_LEVEL, LOGGING_ADDRESS

LOGGING_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
LOGGING_DATEFMT = "%Y-%m-%d %H:%M:%S"


# this is for web server
def init_web_logging():
    root_logger = logging.getLogger()
    logging.basicConfig(
        level=LOGGING_LEVEL,
        format=LOGGING_FORMAT,
        datefmt=LOGGING_DATEFMT,
    )
    """
    if LOGGING_SYSLOG_ADDRESS and path.exists(LOGGING_SYSLOG_ADDRESS):
        try:
            syslog_handler = SysLogHandler(LOGGING_SYSLOG_ADDRESS)
        except Exception as e:
            syslog_handler = SysLogHandler()
        root_logger.addHandler(syslog_handler)
    """
    if LOGGING_ADDRESS and path.exists(LOGGING_ADDRESS):
        try:
           timed_handler = TimedRotatingFileHandler(LOGGING_ADDRESS+"/feelsjournal.access.log" ,when="d", interval=7, backupCount=5)
        except Exception as e:
           timed_handler = SysLogHandler()
        root_logger.addHandler(timed_handler)

# this is for scripts under script/
def init_script_logging():
    script_logger = logging.getLogger()
    logging.basicConfig(
        level=LOGGING_LEVEL,
        format=LOGGING_FORMAT,
        datefmt=LOGGING_DATEFMT,
    )

    if LOGGING_ADDRESS and path.exists(LOGGING_ADDRESS):
        try:
           timed_handler = TimedRotatingFileHandler(LOGGING_ADDRESS+"/feelsjournal.script.log" ,when="d", interval=7, backupCount=5)
        except Exception as e:
           timed_handler = TimedRotatingFileHandler()
        script_logger.addHandler(timed_handler)
