
# for IoT Hub

# Subscribes to attribute updates
mosquitto_sub -d -h "iothub.magenta.at" -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN"

# for local IoT Hub

# Subscribes to attribute updates
mosquitto_sub -d -h "127.0.0.1" -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN"
