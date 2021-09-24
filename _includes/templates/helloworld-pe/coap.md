Install coap-cli. Assuming you have Node.js and NPM installed on your Windows/Linux/MacOS machine, execute the following command:


**Access via public Internet**   
Work in progress...


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
