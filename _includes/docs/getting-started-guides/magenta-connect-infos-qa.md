* TOC
{:toc}

## Direct connected Devices (with IoT Hub SIM-Card)

| Network     | APN-Name      | RAT                     |
| ------------|---------------| ------------------------|
| E/// DCP    | myiot.tma.iot | NB-IoT,LTE-M,2G,3G,4G   |
| DT WBC      | myiot.m2m.at  | NB-IoT,LTE-M,2G,3G,4G   |
| TMA         | myiot.m2m.at  | LTE-M,2G,3G,4G                |

#### Protocol Endpoints  

| Protocol    | DNS-Name     | IP-Addresses                                    | Ports          | Encryption  | 
| ------------|---------------| -----------------------------------------------|----------------| ------------|
| LwM2M       | N/A           | 172.31.79.125<br>172.31.86.75<br>172.31.61.229 | **5685** / UDP | none |
| LwM2M       | N/A           | 172.31.79.125<br>172.31.86.75<br>172.31.61.229 | **5686** / UDP | DTLS |
| LwM2M<br>Bootstrap | N/A           | 172.31.79.125<br>172.31.86.75<br>172.31.61.229 | **5687** / UDP | none
| LwM2M<br>Bootstrap | N/A           | 172.31.79.125<br>172.31.86.75<br>172.31.61.229 | **5688** / UDP | DTLS |
| CoAP        | N/A           | 172.31.78.49<br>172.31.83.246<br>172.31.60.74  | **5683** / UDP | none |
| CoAP        | N/A           | 172.31.78.49<br>172.31.83.246<br>172.31.60.74  | **5684** / UDP | DTLS |
| MQTT        | N/A           | 172.31.64.64<br>172.31.59.135<br>172.31.81.102 | **1883** / TCP | none |
| MQTTS       | N/A           | 172.31.64.64<br>172.31.59.135<br>172.31.81.102 | **8883** / TCP | SSL/TLS  |
| HTTP        | N/A           | 172.31.64.64<br>172.31.59.135<br>172.31.81.102 | **80** / TCP   | none |
| HTTPS       | N/A           | 172.31.64.64<br>172.31.59.135<br>172.31.81.102 | **443** / TCP  | SSL/TLS  |
| NTP         | N/A           | 172.31.25.113                                  | **123** / UDP  | none  |



## Devices connected via public Internet  
Any access technology (public Internet, WIFI,LTE,5G,GPRS ..)
#### Protocol Endpoints  

| Protocol     | DNS-Name                     | IP-Addresses                                    | Ports          | Encryption  | 
| ------------|------------------------------| ------------------------------------------------|----------------| ------------|
| LwM2M       | lwm2m.iothub.test.magenta.at | 3.65.109.171<br>52.59.131.237<br>18.198.110.220 | **5686** / UDP | DTLS        |
| LwM2M<br>Bootstrap | lwm2m.iothub.test.magenta.at | 3.65.109.171<br>52.59.131.237<br>18.198.110.220 | **5688** / UDP | DTLS        |
| CoAP        | coap.iothub.test.magenta.at  | 3.66.107.91<br>18.198.148.101<br>3.68.173.175   | **5684** / UDP | DTLS        |
| MQTTS       | iothub.test.magenta.at       | 3.67.118.159<br>3.68.57.75<br>3.67.110.96       | **8883** / TCP | SSL/TLS     |
| HTTPS       | iothub.test.magenta.at       | 3.67.118.159<br>3.68.57.75<br>3.67.110.96       | **443**  / TCP | SSL/TLS     |


