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

Replace $ACCESS_TOKEN with corresponding values.

```bash
echo -n '{"temperature": 25}' | coap post coap://172.31.78.49/api/v1/$ACCESS_TOKEN/telemetry
```
{: .copy-code}

For example access token is ABC123:

```bash
echo -n '{"temperature": 25}' | coap post coap://172.31.78.49/api/v1/ABC123/telemetry 
```
{: .copy-code}

<br/>
<br/>
