FROM alpine


RUN mkdir /dist
COPY dist /dist
RUN chmod -R 777 /dist
RUN ls -alt /dist


RUN mkdir /work
WORKDIR /work
RUN ls -alt /work

# Starte das Programm
CMD ["/dist/SecurityScannerSchadow", "--configFile", "/dist/securityScannerConfig.json", "--work", "/work"]
