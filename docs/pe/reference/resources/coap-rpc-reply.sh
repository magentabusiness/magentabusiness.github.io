# Publish response to RPC request. Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
coap-client -f rpc-response.json -m post coap://iothub.magenta.at/api/v1/$ACCESS_TOKEN/rpc/1
# For example, iothub.magenta.at reference your local installation, $ACCESS_TOKEN is ABC123:
coap-client -f rpc-response.json -m post coap://localhost/api/v1/ABC123/rpc/1