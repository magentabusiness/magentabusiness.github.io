To connect "In-vehicle monitoring system" to the IoT Hub Edge you need to get device credentials first.
IoT Hub supports different device credentials. We recommend to use default auto-generated credentials which is access token for this guide.

Please open IoT Hub **Edge** UI using the URL: **http://EDGE_URL**.

{% include images-gallery.html imageCollection="copyAccessTokenDevice" showListImageTitles="true" %}

We will use simple commands to generate random telemetry for the device **In-vehicle monitoring system** and publish to the IoT Hub **Edge** by the MQTT protocol.

Please download following script to your local folder:
- [**mqtt-generator.py**](/docs/edge/use-cases/resources/data-filtering-traffic-reduce/mqtt_generator.py)

Before running the scripts, please modify **mqtt-generator.py** accordingly:

- Replace **YOUR_ACCESS_TOKEN** with **In-vehicle monitoring system** device access token copied from the steps above. 

- Replace **YOUR_TB_EDGE_HOST** with your IoT Hub Edge host. For example, **localhost**.

- Replace **YOUR_TB_EDGE_MQTT_PORT** with your IoT Hub Edge MQTT port. For example, **11883** or **1883**.

Open the terminal and install MQTT Python library:
```bash
sudo pip install paho-mqtt
```

Go to the folder that contains Python script and launch an application by this command:

```bash
python mqtt-generator.py
```

Open IoT Hub **Edge** UI and verify that device successfully receives telemetry:

{% include images-gallery.html imageCollection="verifyDeviceTelemetryEdge" showListImageTitles="true" %}

Open IoT Hub **{{currentIoT HubVersion}}** UI and verify that edge successfully pushes data to the cloud:

{% include images-gallery.html imageCollection="verifyDeviceTelemetry" showListImageTitles="true" %}