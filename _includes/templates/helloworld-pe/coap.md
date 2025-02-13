Install coap-cli. Assuming you have Node.js and NPM installed on your Windows/Linux/MacOS machine, execute the following command:


**Access via public Internet**   
Install CoAP Client
```bash
sudo apt install autoconf automake libtool libssl-dev
git clone https://github.com/obgm/libcoap --recursive
cd libcoap/
./autogen.sh 
./configure --with-openssl --disable-doxygen --disable-manpages --disable-shared
make
sudo make install
``` 
Send telemetry data  
Replace $ACCESS_TOKEN with corresponding values.
```bash

coap-client   -m post coaps://coap.iothub.magenta.at/api/v1/$ACCESS_TOKEN/telemetry -e '{"temperature":25}'

``` 
{: .copy-code}


**Direct connected Device (with IoT Hub SIM-Card)**  

```bash
npm install coap-cli -g
```

{: .copy-code}

{% if docsPrefix contains 'paas/' %}

Replace $ACCESS_TOKEN with corresponding value.

```bash
echo -n '{"temperature": 25}' | coap post coap://{{coapHostName}}/api/v1/$ACCESS_TOKEN/telemetry
```
{: .copy-code}

For example, $ACCESS_TOKEN is ABC123:

```bash
echo -n '{"temperature": 25}' | coap post coap://{{coapHostName}}/api/v1/ABC123/telemetry
```
{: .copy-code}

{% else %}

Replace $THINGSBOARD_HOST_NAME and $ACCESS_TOKEN with corresponding values.

```bash
echo -n '{"temperature": 25}' | coap post coap://$THINGSBOARD_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```
{: .copy-code}

For example, $THINGSBOARD_HOST_NAME reference your local installation, $ACCESS_TOKEN is ABC123:

```bash
echo -n '{"temperature": 25}' | coap post coap://localhost/api/v1/ABC123/telemetry
```
{: .copy-code}

{% endif %}

<br>
<br>
