
# for IoT Hub

# Publish client-side attributes update
cat new-attributes-values.json | coap post coap://coap-device.iothub.magenta.at/api/v1/$ACCESS_TOKEN/attributes

# for local IoT Hub

# Publish client-side attributes update
cat new-attributes-values.json | coap post coap://localhost/api/v1/$ACCESS_TOKEN/attributes
