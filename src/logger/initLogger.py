import logging
import logging.config
import os

"""
init the loggers
create the logging dir
"""

if not os.path.exists('logs'):
    os.makedirs('logs')

loggingConfigPath = os.path.join(os.path.dirname(__file__), "logging.config")
logging.config.fileConfig(loggingConfigPath)

def changeDefaultLogLevel(level):
    logging.getLogger("root").setLevel(level.upper())