#!/bin/sh -l

ls -alt
cwd
ls -alt ~
ls -alt /dist
ls -alt /work

/dist/SecurityScannerSchadow --configFile /dist/securityScannerConfig.json --work /work