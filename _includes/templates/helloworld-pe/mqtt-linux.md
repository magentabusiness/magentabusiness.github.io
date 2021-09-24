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

**Access via public Internet**  

Replace $ACCESS_TOKEN with corresponding values.

```bash
mosquitto_pub -d -q 1 -h "iothub.magenta.at" -p "8883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25} --capath /etc/ssl/certs
```
{: .copy-code}

For access token is ABC123:

```bash
mosquitto_pub -d -q 1 -h "iothub.magenta.at" -p "8883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":25} --capath /etc/ssl/certs
```
{: .copy-code}

**Direct connected Device (with IoT Hub SIM-Card)**  
Replace $ACCESS_TOKEN with corresponding values.

```bash
mosquitto_pub -d -q 1 -h "172.31.64.64" -p "1883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25}  
```
{: .copy-code}

For access token is ABC123:

```bash
mosquitto_pub -d -q 1 -h "172.31.64.64" -p "1883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":25}  
```
{: .copy-code}

Successful output should look similar to this one:

```text
Client mosqpub|xxx sending CONNECT
Client mosqpub|xxx received CONNACK
Client mosqpub|xxx sending PUBLISH (d0, q1, r0, m1, 'v1/devices/me/telemetry', ... (16 bytes))
Client mosqpub|xxx received PUBACK (Mid: 1)
Client mosqpub|xxx sending DISCONNECT
```

**Note:** You are able to use basic MQTT credentials (combination of client id, user name and password ) 
and customize **topic names** and **payload type** using Device Profile. See more info [here](/docs/user-guide/device-profiles/#mqtt-transport-type).

<br/>
<br/>
  