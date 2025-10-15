## Prerequisites

You will need to have IoT Hub server up and running. 
The easiest way is to use [Live Demo](https://iothub.magenta.at/signup) server.

The alternative option is to install IoT Hub using the [installation guide](/docs/user-guide/install/installation-options/){:target="_blank"}:
- **Windows** users should follow this [guide](/docs/user-guide/install/docker-windows/){:target="_blank"}
- **Linux** users with Docker installed can execute the following commands:

```
mkdir -p ~/.mytb-data && sudo chown -R 799:799 ~/.mytb-data
mkdir -p ~/.mytb-logs && sudo chown -R 799:799 ~/.mytb-logs
docker run -it -p 8080:9090 -p 7070:7070 -p 1883:1883 -p 5683-5688:5683-5688/udp -v ~/.mytb-data:/data \
-v ~/.mytb-logs:/var/log/thingsboard --name mytb --restart always thingsboard/tb-postgres
``` 
{: .copy-code}

These commands install IoT Hub and load demo data and accounts.

IoT Hub UI will be available at: **http://localhost:8080**.

