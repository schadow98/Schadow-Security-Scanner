FROM python:3.11

RUN mkdir /dist
COPY src /dist
COPY securityScannerConfig.json /dist
COPY requirements.txt /requirements.txt
RUN pip install -r /dist/requirements.txt
RUN chmod -R 777 /dist
RUN ls -alt /dist

RUN mkdir /work
RUN ls -alt /work
WORKDIR /work

ENTRYPOINT ["python", "/dist/SecurityScanner.py", "--configFile", "/dist/securityScannerConfig.json", "--work", "/work"]
