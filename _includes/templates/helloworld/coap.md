Install coap-cli. Assuming you have Node.js and NPM installed on your Windows/Linux/MacOS machine, execute the following command:

```bash
npm install coap-cli -g
```
{: .copy-code}

Replace $THINGSBOARD_HOST_NAME and $ACCESS_TOKEN with corresponding values.

```bash
echo -n '{"temperature": 25}' | coap post coap://$THINGSBOARD_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```
{: .copy-code}

For example, $THINGSBOARD_HOST_NAME reference live demo server, $ACCESS_TOKEN is ABC123:

```bash
<<<<<<< HEAD
echo -n '{"temperature": 25}' | coap post coap://iothub.magenta.at/api/v1/ABC123/telemetry 
=======
echo -n '{"temperature": 25}' | coap post coap://demo.thingsboard.io/api/v1/ABC123/telemetry
>>>>>>> ad368c0ed5d3799cf901e3e0c5e84bf8564eb1c6
```
{: .copy-code}

For example, $THINGSBOARD_HOST_NAME reference your local installation, $ACCESS_TOKEN is ABC123:

```bash
echo -n '{"temperature": 25}' | coap post coap://localhost/api/v1/ABC123/telemetry
```
{: .copy-code}

<br>
<br>
