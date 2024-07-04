import argparse
import json
import logging

import Tools.Logger
import Tools.setEnvironmentVariables

from DependencyScanner.DependencyScanner import DependencyScanner

class SecurityScanner(object):
    def __init__(self, args: argparse.Namespace) -> None:
        self.path                       = args.path
        self.enableDependenyScanner     = args.disableDependenyScanner or True
        self.enableSQLInjectionScanner  = args.disableSQLInjectionScanner or True
        self.requirementsFile           = args.requirementsFile or None
        logging.info("SecurityScanner " + json.dumps(self.__dict__, indent=2))

        if self.enableDependenyScanner:
            self.DependenyScanner = DependencyScanner(self.path, self.requirementsFile)

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
        '-d', '--disableDependenyScanner',
        action='store_true',
        default=False,
        help="Disables the Dependency Scanner (default: enabled)"
    )

    parser.add_argument(
        '-s', '--disableSQLInjectionScanner',
        action='store_true',
        default=False,
        help="Disables the SQL Injection Scanner (default: enabled)"
    )

    parser.add_argument(
        '-r', '--requirementsFile',
        type=str,
        help='Path to the requirements.txt file containing project dependencies (optional, default="requirements.txt").'
    )

    args = parser.parse_args()
    security_scanner = SecurityScanner(args)