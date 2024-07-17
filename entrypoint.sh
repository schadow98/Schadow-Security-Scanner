#!/bin/sh -l

pwd
ls -alt
echo "~"
ls -alt ~
echo "dist"
ls -alt /dist
echo "work"
ls -alt /work

/dist/SecurityScannerSchadow --configFile /dist/securityScannerConfig.json --work /work