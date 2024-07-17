FROM alpine


RUN mkdir /dist
COPY dist /dist
RUN chmod -R 777 /dist
RUN ls -alt /dist

RUN mkdir /work
RUN ls -alt /work
WORKDIR /work

ENTRYPOINT ["/dist/SecurityScannerSchadow", "--configFile", "/dist/securityScannerConfig.json", "--work", "/work"]
