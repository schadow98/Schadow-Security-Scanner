import logging
import datetime

class ReportLogger(logging.FileHandler):
    """
    a class that allows to log to a file and contains the date in the filename
    """
    def __init__(self, filename: str="", mode: str='a', encoding:str| None=None, delay:bool=False, errors: str| None=None):
        #filename = datetime.datetime.now().strftime("./logs/SecurityReport_%Y%m%d_%H%M.log")
        filename = "logs/report.log"
        mode="w+"
        super().__init__(filename, mode, encoding, delay, errors)