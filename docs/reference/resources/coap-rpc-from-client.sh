# Post client-side rpc request. Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
cat rpc-client-request.json | coap post coap://iothub.magenta.at/api/v1/$ACCESS_TOKEN/rpc
# For example, iothub.magenta.at reference live demo server, $ACCESS_TOKEN is ABC123:
cat rpc-client-request.json | coap post coap://demo.thingsboard.io/api/v1/ABC123/rpc