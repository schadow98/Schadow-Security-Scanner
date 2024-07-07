import logging
import datetime

class ReportLogger(logging.FileHandler):
    def __init__(self, filename="", mode='a', encoding=None, delay=False, errors=None):
        #filename = datetime.datetime.now().strftime("./logs/SecurityReport_%Y%m%d_%H%M.log")
        filename = "report.log"
        super().__init__(filename, mode, encoding, delay, errors)