import logging
import json

class Dependency(object):
    """
    Dependency class contains all information for a thrid party libary.

    Args:
            name (str): name of third party libary
            version (str): version of third party libary
            extra (str): extra of third party libary
    """
    def __init__(self, name: str, version: str=None, extra: str=None):
        self.name       = name
        self.version    = version
        self.extra      = extra
        logging.debug("Dependency " + json.dumps(self.__dict__, indent=2))

    def __str__(self) -> str:
        return f"Name: {self.name} - Version: {self.version} - Extra: {self.extra}"