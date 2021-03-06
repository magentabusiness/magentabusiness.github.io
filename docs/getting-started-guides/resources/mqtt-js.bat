@echo off

REM Set IoT Hub host to "iothub.magenta.at" or "localhost"
set THINGSBOARD_HOST=iothub.magenta.at

REM Replace YOUR_ACCESS_TOKEN with one from Device details panel.
set ACCESS_TOKEN=YOUR_ACCESS_TOKEN

REM Read serial number and firmware version attributes
set /p ATTRIBUTES=<attributes-data.json

REM Read timeseries data as an object without timestamp (server-side timestamp will be used)
set /p TELEMETRY=<telemetry-data.json

REM publish attributes and telemetry data via mqtt client
node publish.js