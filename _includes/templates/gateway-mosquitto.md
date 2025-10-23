We will use Mosquitto MQTT broker for the demonstration purposes. See Mosquitto [downloads page](https://mosquitto.org/download/) for instructions how to install this broker.

**NOTE:** Mosquitto and IoT Hub use the same port (1883) for MQTT service by default. If you want to use IoT Hub and Mosquitto on the same host, you need to change the mqtt port in one of the servers.

Since we use IoT Hub [demo instance](https://iothub.magenta.at/signup) hosted in the cloud, we will install Mosquitto MQTT broker locally and use the default service configuration.

If you decide to use other MQTT broker that is deployed to the external host or has specific security configuration, please edit **mqtt-config.json** file and modify connection parameters.
See MQTT extension [configuration guide](/docs/iot-gateway/mqtt/) for more details.
