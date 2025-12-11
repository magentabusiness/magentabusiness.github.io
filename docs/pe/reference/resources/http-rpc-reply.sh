# Publish response to RPC request. Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
curl -v -X POST -d @rpc-response.json http://iothub.magenta.at/api/v1/$ACCESS_TOKEN/rpc/1 --header "Content-Type:application/json"
# For example, iothub.magenta.at reference your local installation, $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @rpc-response.json http://localhost:8080/api/v1/ABC123/rpc/1 --header "Content-Type:application/json"