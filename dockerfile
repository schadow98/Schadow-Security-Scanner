FROM alpine


Run mkdir /dist
COPY dist  /dist
RUN ls -alt /dist

Run mkdir /work
WORKDIR /work
RUN ls -alt /work

CMD ["/dist/SecurityScannerSchadow", "--configFile", "/dist/securityScannerConfig.json", "--work", "/work"]