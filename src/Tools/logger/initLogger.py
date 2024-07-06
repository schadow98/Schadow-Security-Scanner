import logging.config
import os
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.config.fileConfig("./src/Tools/logger/logging.config")