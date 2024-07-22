import logging
import logging.config
import os

"""
init the loggers
create the logging dir
"""


def initLoggers(logDir):
    if not logDir:
        logDir = 'logs'

    os.environ["LOG_DIR"] = logDir
    if not os.path.exists(logDir):
        os.makedirs(logDir)

    loggingConfigPath = os.path.join(os.path.dirname(__file__), "logging.config")

    logging.config.fileConfig(loggingConfigPath)

def changeDefaultLogLevel(level):
    logging.getLogger("root").setLevel(level.upper())