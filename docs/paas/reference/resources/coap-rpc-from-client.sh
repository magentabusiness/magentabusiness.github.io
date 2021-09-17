
# for IoT Hub

# Post client-side rpc request
cat rpc-client-request.json | coap post coap://coap-device.iothub.magenta.at/api/v1/$ACCESS_TOKEN/rpc

# for local IoT Hub

# Post client-side rpc request
cat rpc-client-request.json | coap post coap://localhost/api/v1/$ACCESS_TOKEN/rpc