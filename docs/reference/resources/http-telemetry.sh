# Publish data as an object without timestamp (server-side timestamp will be used). Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
curl -v -X POST --data "{"temperature":42,"humidity":73}" http://iothub.magenta.at/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
# For example, iothub.magenta.at reference live demo server, $ACCESS_TOKEN is ABC123:
curl -v -X POST --data "{"temperature":42,"humidity":73}" https://demo.thingsboard.io/api/v1/ABC123/telemetry --header "Content-Type:application/json"

# Publish data as an object without timestamp (server-side timestamp will be used) using data from file. Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
curl -v -X POST -d @telemetry-data-as-object.json http://iothub.magenta.at/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
# For example, iothub.magenta.at reference live demo server, $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @telemetry-data-as-object.json https://demo.thingsboard.io/api/v1/ABC123/telemetry --header "Content-Type:application/json"

# Publish data as an array of objects without timestamp (server-side timestamp will be used)  using data from file. Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
curl -v -X POST -d @telemetry-data-as-array.json http://iothub.magenta.at/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
# For example, iothub.magenta.at reference live demo server, $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @telemetry-data-as-array.json https://demo.thingsboard.io/api/v1/ABC123/telemetry --header "Content-Type:application/json"

# Publish data as an object with timestamp (telemetry timestamp will be used)  using data from file. Replace iothub.magenta.at and $ACCESS_TOKEN with corresponding values.
curl -v -X POST -d @telemetry-data-with-ts.json http://iothub.magenta.at/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
# For example, iothub.magenta.at reference live demo server, $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @telemetry-data-with-ts.json https://demo.thingsboard.io/api/v1/ABC123/telemetry --header "Content-Type:application/json"