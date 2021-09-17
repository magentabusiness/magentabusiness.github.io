
# for IoT Hub

# Send HTTP attributes request
curl -v -X GET "https://iothub.magenta.at/api/v1/$ACCESS_TOKEN/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2"

# for local IoT Hub

# Send HTTP attributes request
curl -v -X GET http://localhost:8080/api/v1/$ACCESS_TOKEN/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2