FROM alpine


Run mkdir /dist
COPY /dist  /dist

Run mkdir /work
WORKDIR /work

RUN ls -alt /work

CMD ["/dist/SecurityScannerSchadow.exe", "--configFile", "/dist/securityScannerConfig.json", "--work", "/work"]