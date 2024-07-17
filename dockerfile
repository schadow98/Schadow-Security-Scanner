FROM alpine


RUN mkdir /dist
COPY dist /dist
RUN chmod -R 777 /dist
RUN ls -alt /dist

RUN mkdir /work
RUN ls -alt /work
WORKDIR /work
# Starte das Programm
COPY entrypoint.sh /entrypoint.sh
RUN chmod -R 777 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
# ENTRYPOINT ["/dist/SecurityScannerSchadow", "--configFile", "/dist/securityScannerConfig.json", "--work", "."]
