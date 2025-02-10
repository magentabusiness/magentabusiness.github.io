<<<<<<< HEAD

# for IoT Hub

# Send HTTP attributes request
curl -v -X GET https://iothub.magenta.at/api/v1/$ACCESS_TOKEN/rpc?timeout=20000

# for local IoT Hub

# Send rpc request with 20 seconds timeout
curl -v -X GET http://localhost:8080/api/v1/$ACCESS_TOKEN/rpc?timeout=20000
=======
# Send rpc request with 20 seconds timeout. Replace $ACCESS_TOKEN with corresponding value.
curl -v -X GET {{httpsUrl}}/api/v1/$ACCESS_TOKEN/rpc?timeout=20000
# For example, $ACCESS_TOKEN is ABC123:
curl -v -X GET {{httpsUrl}}/api/v1/ABC123/rpc?timeout=20000
>>>>>>> ad368c0ed5d3799cf901e3e0c5e84bf8564eb1c6
