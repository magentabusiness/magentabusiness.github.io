Install mqtt client for **Ubuntu**:

```bash
sudo apt-get install mosquitto-clients
```
{: .copy-code}

Install cURL for **macOS**:

```bash
brew install mosquitto-clients
```
{: .copy-code}

{% if docsPrefix contains 'paas/' %}

Replace $ACCESS_TOKEN with corresponding value.

```bash
mosquitto_pub -d -q 1 -h "{{mqttHostName}}" -p "1883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25}
```
{: .copy-code}

For example, $ACCESS_TOKEN is ABC123:

```bash
mosquitto_pub -d -q 1 -h "{{mqttHostName}}" -p "1883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":25}
```
{: .copy-code}

{% else %}

<<<<<<< HEAD
Replace $ACCESS_TOKEN with corresponding values.

```bash
mosquitto_pub -d -q 1 -h "iothub.magenta.at" -p "8883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25} --capath /etc/ssl/certs
```
{: .copy-code}

For access token is ABC123:

```bash
mosquitto_pub -d -q 1 -h "mqtt.thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":25} 
```
{: .copy-code}

**Direct connected Device (with IoT Hub SIM-Card)**  
Replace $ACCESS_TOKEN with corresponding values.
=======
Replace $THINGSBOARD_HOST_NAME and $ACCESS_TOKEN with corresponding values.

```bash
mosquitto_pub -d -q 1 -h "$THINGSBOARD_HOST_NAME" -p "1883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25}
```
{: .copy-code}

For example, $THINGSBOARD_HOST_NAME reference your local installation, $ACCESS_TOKEN is ABC123:
>>>>>>> ad368c0ed5d3799cf901e3e0c5e84bf8564eb1c6

```bash
mosquitto_pub -d -q 1 -h "172.31.64.64" -p "1883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25}  
```
{: .copy-code}

For access token is ABC123:

```bash
mosquitto_pub -d -q 1 -h "172.31.64.64" -p "1883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":25}  
```
{: .copy-code}

{% endif %}

Successful output should look similar to this one:

```text
Client mosqpub|xxx sending CONNECT
Client mosqpub|xxx received CONNACK
Client mosqpub|xxx sending PUBLISH (d0, q1, r0, m1, 'v1/devices/me/telemetry', ... (16 bytes))
Client mosqpub|xxx received PUBACK (Mid: 1)
Client mosqpub|xxx sending DISCONNECT
```

<<<<<<< HEAD
**Note:** You are able to use basic MQTT credentials (combination of client id, user name and password ) 
and customize **topic names** and **payload type** using Device Profile. See more info [here](/docs/user-guide/device-profiles/#mqtt-transport-type).

<br/>
<br/>
=======
{% capture difference %}
**Note:** Since ThingsBoard 3.2, you are able to use basic MQTT credentials (combination of client id, username and password)
and customize **topic names** and **payload type** using Device Profile. See more info [here](/docs/user-guide/device-profiles/#mqtt-transport-type).
{% endcapture %}
{% include templates/info-banner.md content=difference %}
>>>>>>> ad368c0ed5d3799cf901e3e0c5e84bf8564eb1c6
