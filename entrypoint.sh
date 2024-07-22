#!/bin/sh -l

# Initialize the command to run the Python script
CMD="python /dist/SecurityScanner.py"

# Add the configFile argument
CMD="$CMD --configFile ${INPUT_CONFIGFILE}"

# Add the path argument
CMD="$CMD --path ${INPUT_PATH}"

# Conditionally add arguments based on input values
if [ "${INPUT_DISABLEDEPENDENYSCANNER}" = "true" ]; then
  CMD="$CMD --disableDependenyScanner"
fi

if [ "${INPUT_DISABLEINJECTIONSCANNER}" = "true" ]; then
  CMD="$CMD --disableInjectionScanner"
fi

if [ "${INPUT_ENABLECUSTOMSCANNER}" = "true" ]; then
  CMD="$CMD --enableCustomScanner"
fi

if [ "${INPUT_DISABLESECRETSCANNER}" = "true" ]; then
  CMD="$CMD --disableSecretScanner"
fi

# Add optional arguments with default values
CMD="$CMD --requirementsFile ${INPUT_REQUIREMENTSFILE}"
CMD="$CMD --logLevel ${INPUT_LOGLEVEL}"
CMD="$CMD --logDir ${INPUT_LOGDIR}"

# Output the final command for debugging purposes
echo "Running command: $CMD"

# Execute the constructed command
exec $CMD
