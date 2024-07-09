import argparse
import json
import logging
import os

from SASTScanner.SecretDetectionScanner import SecretDetectionScanner
from SASTScanner.InjectionScanner import InjectionScanner
import tools.logger.initLogger
import tools.setEnvironmentVariables

from DependencyScanner.DependencyScanner import DependencyScanner

class SecurityScanner(object):
    """
    Main class that initilizes and starts the security scans
    :type args: argparse.Namespace - the arguments that get entered on the command line
    """
    def __init__(self, args: argparse.Namespace) -> None:
        self.path                       = args.path
        self.enableDependenyScanner     = not args.disableDependenyScanner
        self.enableInjectionScanner     = not args.disableInjectionScanner
        self.enableSecretScanner        = not args.disableInjectionScanner
        self.requirementsFile           = args.requirementsFile or None
        self.configFile                 = args.configFile or "./securityScannerConfig.json"
        logging.info("SecurityScanner " + json.dumps(self.__dict__, indent=2))

        self.readConfig()

        if self.enableDependenyScanner:
            self.DependenyScanner   = DependencyScanner(self.path, self.requirementsFile, self.config.get("dependencyScanner", {}).get("db"),  self.config.get("dependencyScanner", {}).get("vulnerabilityFilter"))

        if self.enableInjectionScanner:
             self.DependenyScanner  = InjectionScanner(self.path, self.config.get("injectionsScanner", []))

        if self.enableSecretScanner:
             self.SecretDetectionScanner     = SecretDetectionScanner(self.path, self.config.get("secretDetectionScanner", []))
                   

    def readConfig(self) -> None:
        """
        method to read and parse the configFile of the security scanner
        """
        if self.configFile and not os.path.exists(self.configFile):
            raise Exception(f"ConfigFile for SecurityScanner dont exists - please create File {self.configFile}")
        try:
            with open(self.configFile) as configFile:
                self.config = json.load(configFile)
        except Exception as e:
            logging.warn(e, exc_info=True)
            raise Exception(f"Error while parsing config - please correct JSON of {self.configFile}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Security Scanner by Malte Schadow',
        description='Scans a Python Project for Security Vulnerabilities',
        epilog='For more help please contact me'
    )

    parser.add_argument(
        '-p', '--path',
        type=str,
        default=".",  # Optional project path argument with default value
        help='Specify the path to the Python project to scan. Defaults to current directory.'
    )

    parser.add_argument(
        '-c', '--configFile',
        type=str,
        help='Path to the configFile to configurate the Security Scanner (default="securityScannerConfig.json").'
    )

    parser.add_argument(
        '-d', '--disableDependenyScanner',
        action='store_true',
        default=False,
        help="Disables the Dependency Scanner (default: enabled)"
    )

    parser.add_argument(
        '-i', '--disableInjectionScanner',
        action='store_true',
        default=False,
        help="Disables the Injection Scanner (default: enabled)"
    )

    parser.add_argument(
        '-s', '--disableSecretScanner',
        action='store_true',
        default=False,
        help="Disables the Secret Scanner (default: enabled)"
    )

    parser.add_argument(
        '-r', '--requirementsFile',
        type=str,
        help='Path to the requirements.txt file containing project dependencies (optional, default="requirements.txt").'
    )

    args = parser.parse_args()
    security_scanner = SecurityScanner(args)