import logging.config
import os

"""
init the loggers
create the logging dir
"""

if not os.path.exists('logs'):
    os.makedirs('logs')
logging.config.fileConfig("./src/Tools/logger/logging.config")

def changeDefaultLogLevel(level):
    logging.getLogger("root").setLevel(level.upper())