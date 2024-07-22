import logging
import datetime
import os

class CustomFileHandler(logging.FileHandler):
    """
    a class that allows to log to a file and contains the date in the filename
    """
    def __init__(self, filename: str="", mode: str='a', encoding:str| None=None, delay:bool=False, errors: str| None=None):
        filename = datetime.datetime.now().strftime( os.environ["LOG_DIR"] + "/process_%Y%m%d_%H%M.log")
        #filename = os.environ["LOG_DIR"] + "/process.log"
        mode="w+"
        super().__init__(filename, mode, encoding, delay, errors)