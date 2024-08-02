import os
import json
import logging

import re
import requests

from DependencyScanner.Dependency import Dependency
from DependencyScanner.DependencyVulnerability import DependencyVulnerability


class Sonatype(object):
    """
    Sonatype class checks the dependency in the sonatype database
    It is free to use, but has a limit of 128 Packges get at checked at one
    """
    def __init__(self) -> None:
        self.apiUrl: str = 'https://ossindex.sonatype.org/api/v3/component-report'
        logging.info("Sonattype " + json.dumps(self.__dict__, indent=2))

    # calls the rest api of the db
    def getDependecies(self, dependencies: list[Dependency]) -> dict:
        if len(dependencies) == 0: return {}
        payload = {
            "coordinates": [
                f"pkg:pypi/{dependency.name}@{dependency.version}" for dependency in dependencies
            ]
        }
        # use for development
        # response = [{'coordinates': 'pkg:pypi/python-dotenv@1.0.1', 'description': 'Add .env support to your django/flask apps in development and deployments', 'reference': 'https://ossindex.sonatype.org/component/pkg:pypi/python-dotenv@1.0.1?utm_source=python-requests&utm_medium=integration&utm_content=2.32.3', 'vulnerabilities': []}, {'coordinates': 'pkg:pypi/requests@1.0.0', 'description': 'Python HTTP for Humans.', 'reference': 'https://ossindex.sonatype.org/component/pkg:pypi/requests@1.0.0?utm_source=python-requests&utm_medium=integration&utm_content=2.32.3', 'vulnerabilities': [{'id': 'CVE-2013-2099', 'displayName': 'CVE-2013-2099', 'title': '[CVE-2013-2099] CWE-399', 'description': 'Algorithmic complexity vulnerability in the ssl.match_hostname function in Python 3.2.x, 3.3.x, and earlier, and unspecified versions of python-backports-ssl_match_hostname as used for older Python versions, allows remote attackers to cause a denial of service (CPU consumption) via multiple wildcard characters in the common name in a certificate.', 'cvssScore': 4.3, 'cvssVector': 'AV:N/AC:M/Au:N/C:N/I:N/A:P', 'cwe': 'CWE-399', 'cve': 'CVE-2013-2099', 'reference': 'https://ossindex.sonatype.org/vulnerability/CVE-2013-2099?component-type=pypi&component-name=requests&utm_source=python-requests&utm_medium=integration&utm_content=2.32.3', 'externalReferences': ['http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2099', 'https://python-security.readthedocs.io/vuln/ssl-match_hostname-wildcard-dos.html#fixed-in', 'https://bugs.python.org/issue17980', 'https://pip.readthedocs.io/en/1.4/news.html', 'https://bugzilla.redhat.com/show_bug.cgi?id=963260']}, {'id': 'CVE-2014-1829', 'displayName': 'CVE-2014-1829', 'title': '[CVE-2014-1829] CWE-200: Information Exposure', 'description': 'Requests (aka python-requests) before 2.3.0 allows remote servers to obtain a netrc password by reading the Authorization header in a redirected request.', 'cvssScore': 5.0, 'cvssVector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N', 'cwe': 'CWE-200', 'cve': 'CVE-2014-1829', 'reference': 'https://ossindex.sonatype.org/vulnerability/CVE-2014-1829?component-type=pypi&component-name=requests&utm_source=python-requests&utm_medium=integration&utm_content=2.32.3', 'externalReferences': ['http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-1829', 'https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=733108', 'https://github.com/kennethreitz/requests/issues/1885']}, {'id': 'CVE-2014-1830', 'displayName': 'CVE-2014-1830', 'title': '[CVE-2014-1830] CWE-200: Information Exposure', 'description': 'Requests (aka python-requests) before 2.3.0 allows remote servers to obtain sensitive information by reading the Proxy-Authorization header in a redirected request.', 'cvssScore': 5.0, 'cvssVector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N', 'cwe': 'CWE-200', 'cve': 'CVE-2014-1830', 'reference': 'https://ossindex.sonatype.org/vulnerability/CVE-2014-1830?component-type=pypi&component-name=requests&utm_source=python-requests&utm_medium=integration&utm_content=2.32.3', 'externalReferences': ['http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-1830', 'https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=733108', 'https://github.com/kennethreitz/requests/issues/1885']}, {'id': 'CVE-2018-18074', 'displayName': 'CVE-2018-18074', 'title': '[CVE-2018-18074] CWE-522: Insufficiently Protected Credentials', 'description': "The Requests package before 2.20.0 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to discover credentials by sniffing the network.\n\nSonatype's research suggests that this CVE's details differ from those defined at NVD. See https://ossindex.sonatype.org/vulnerability/CVE-2018-18074 for details", 'cvssScore': 7.5, 'cvssVector': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N', 'cwe': 'CWE-522', 'cve': 'CVE-2018-18074', 'reference': 'https://ossindex.sonatype.org/vulnerability/CVE-2018-18074?component-type=pypi&component-name=requests&utm_source=python-requests&utm_medium=integration&utm_content=2.32.3', 'externalReferences': ['http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-18074', 'http://docs.python-requests.org/en/master/community/updates/#release-and-version-history', 'https://github.com/requests/requests/issues/4716', 'https://github.com/requests/requests/pull/4718']}, {'id': 'CVE-2024-35195', 'displayName': 'CVE-2024-35195', 'title': '[CVE-2024-35195] CWE-670: Always-Incorrect Control Flow Implementation', 'description': 'Requests is a HTTP library. Prior to 2.32.0, when making requests through a Requests `Session`, if the first request is made with `verify=False` to disable cert verification, all subsequent requests to the same host will continue to ignore cert verification regardless of changes to the value of `verify`. This behavior will continue for the lifecycle of the connection in the connection pool. This vulnerability is fixed in 2.32.0.', 'cvssScore': 5.6, 'cvssVector': 'CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:N', 'cwe': 'CWE-670', 'cve': 'CVE-2024-35195', 'reference': 'https://ossindex.sonatype.org/vulnerability/CVE-2024-35195?component-type=pypi&component-name=requests&utm_source=python-requests&utm_medium=integration&utm_content=2.32.3', 'externalReferences': ['http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2024-35195', 'https://github.com/advisories/GHSA-9wx4-h78v-vm56']}]}]
        # return response

        response = requests.post(self.apiUrl, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            logging.warn(response.status_code)
            raise Exception(f"Fehler bei der API-Anfrage: {response.status_code}, {response.text}")

    # checks if the contains a vulnerability of the libary
    def checkDependecies(self, dependencies: list[Dependency]) -> list[DependencyVulnerability]:
        response = self.getDependecies(dependencies)
        if not response: return []
        vulnerabilities = []
        for package in response:
            if len(package.get("vulnerabilities", [])) <= 0: 
                logging.info(f"{package['coordinates']}: No vulnerabilites found")
                continue
            else:
                logging.info(f"{package['coordinates']}: {str(len(package['vulnerabilities']))} vulnerabilites found")

            name = re.match(r"pkg:pypi/([^@]+)@", package['coordinates']).group(1) or package['coordinates']
            version = package['coordinates'].split("@")[1] or "Version not given"
            for vulnerability in package["vulnerabilities"]:
                vulnerabilities.append(DependencyVulnerability(
                    name, 
                    version,
                    vulnerability.get("id", "No id given"),
                    vulnerability.get("displayName", "No displayName given"),
                    vulnerability.get("title", "title id given"),
                    vulnerability.get("description", "No description given"),
                    vulnerability.get("cvssScore", "No cvssScore given"),
                    vulnerability.get("cvssVector", "No cvssVector given"),
                    vulnerability.get("cwe", "No cwe given"),
                    vulnerability.get("cve", "No cve given"),
                    vulnerability.get("reference", "No reference given"),
                    vulnerability.get("externalReferences", [])
                      )) 
        
        return vulnerabilities

