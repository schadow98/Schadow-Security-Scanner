# Import the SASTScanner class from the SASTScanner module
from SASTScanner.SASTScanner import SASTScanner

class InjectionScanner(SASTScanner):
    def __init__(self, workingDir=".", patterns=None) -> None:
        """
        Initialize the InjectionScanner class.

        Args:
            workingDir (str): The working directory where the scanner will operate. Default is the current directory.
            patterns (list): A list of patterns to scan for. Default is None, which will be converted to an empty list.
        """
        # If patterns is None, initialize it as an empty list
        if patterns is None:
            patterns = []

        super().__init__(workingDir, patterns)
