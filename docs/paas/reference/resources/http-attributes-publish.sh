
# for IoT Hub

# Publish client-side attributes update
curl -v -X POST --data "{"attribute1": "value1", "attribute2":true, "attribute3": 43.0}" https://iothub.magenta.at/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
# Publish client-side attributes update from file
curl -v -X POST -d @new-attributes-values.json https://iothub.magenta.at/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"

# for local IoT Hub

# Publish client-side attributes update
curl -v -X POST --data "{"attribute1": "value1", "attribute2":true, "attribute3": 43.0}" http://localhost:8080/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
# Publish client-side attributes update from file
curl -v -X POST -d @new-attributes-values.json http://localhost:8080/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"