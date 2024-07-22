#!/bin/sh -l

python /dist/SecurityScanner.py \
  --configFile "${INPUT_CONFIGFILE}" \
  --path "${INPUT_PATH}" \
  --disableDependenyScanner "${INPUT_DISABLEDEPENDENYSCANNER}" \
  --disableInjectionScanner "${INPUT_DISABLEINJECTIONSCANNER}" \
  --enableCustomScanner "${INPUT_ENABLECUSTOMSCANNER}" \
  --disableSecretScanner "${INPUT_DISABLESECRETSCANNER}" \
  --requirementsFile "${INPUT_REQUIREMENTSFILE}" \
  --logLevel "${INPUT_LOGLEVEL}" \
  --logDir "${INPUT_LOGDIR}"
