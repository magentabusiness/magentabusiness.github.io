
# for IoT Hub

# Send HTTP attributes request
curl -v -X GET https://iothub.magenta.at/api/v1/$ACCESS_TOKEN/rpc?timeout=20000

# for local IoT Hub

# Send rpc request with 20 seconds timeout
curl -v -X GET http://localhost:8080/api/v1/$ACCESS_TOKEN/rpc?timeout=20000