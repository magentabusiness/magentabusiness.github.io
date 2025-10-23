# Send rpc request with 20 seconds timeout. Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
curl -v -X GET http://iothub.magenta.at/api/v1/$ACCESS_TOKEN/rpc?timeout=20000
# For example, iothub.magenta.at reference live demo server, $ACCESS_TOKEN is ABC123:
curl -v -X GET https://demo.thingsboard.io/api/v1/ABC123/rpc?timeout=20000