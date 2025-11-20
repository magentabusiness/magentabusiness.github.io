* TOC
{:toc}

## Direct connected Devices (with Magenta SIM-Card)

| Network     | APN-Name        | RAT                     |
| ------------|-----------------| ------------------------|
| DT WBC      | myiot.qa.m2m.at | NB-IoT,LTE-M,2G,3G,4G   |
| TMA         | myiot.qa.tma.at | LTE-M,2G,3G,4G                |

#### Protocol Endpoints  

| Protocol          | DNS-Name     | IP-Addresses                                      | Ports          | Encryption  | 
|-------------------|---------------|---------------------------------------------------|----------------| ------------|
| LwM2M             | N/A           | 172.31.26.104                                     | **5685** / UDP | none |
| LwM2M             | N/A           | 172.31.26.104                                     | **5686** / UDP | DTLS |
| LwM2M<br>Bootstrap | N/A           | 172.31.26.104                                     | **5687** / UDP | none
| LwM2M<br>Bootstrap | N/A           | 172.31.26.104                                     | **5688** / UDP | DTLS |
| CoAP              | N/A           | 172.31.26.104                                     | **5683** / UDP | none |
| CoAPs             | N/A           | 172.31.26.104                                     | **5684** / UDP | DTLS |
| MQTT              | N/A           | 172.31.48.249<br>172.31.64.249<br>172.31.80.249   | **1883** / TCP | none |
| MQTTS             | N/A           | 172.31.48.249<br>172.31.64.249<br>172.31.80.249   | **8883** / TCP | SSL/TLS  |
| HTTP              | N/A           | 172.31.48.249<br>172.31.64.249<br>172.31.80.249   | **80** / TCP   | none |
| HTTPS             | N/A           | 172.31.48.249<br>172.31.64.249<br>172.31.80.249   | **443** / TCP  | SSL/TLS  |
| NTP               | N/A           | 172.31.48.249<br>172.31.64.249<br>172.31.80.249   | **123** / UDP  | none  |



## Devices connected via public Internet  
Any access technology (public Internet, WIFI,LTE,5G,GPRS ..)
#### Protocol Endpoints  

| Protocol     | DNS-Name                     | IP-Addresses                                   | Ports          | Encryption  | 
| ------------|------------------------------|------------------------------------------------|----------------| ------------|
| LwM2M       | lwm2m.iothub.test.magenta.at | 3.67.146.165                                   | **5686** / UDP | DTLS        |
| LwM2M<br>Bootstrap | lwm2m.iothub.test.magenta.at | 3.67.146.165                                   | **5688** / UDP | DTLS        |
| CoAP        | coap.iothub.test.magenta.at  | 3.67.146.165                                   | **5684** / UDP | DTLS        |
| MQTTS       | iothub.test.magenta.at       | 3.76.108.3<br>18.157.231.197<br>18.199.114.20  | **8883** / TCP | SSL/TLS     |
| HTTPS       | iothub.test.magenta.at       | 3.76.108.3<br>18.157.231.197<br>18.199.114.20  | **443**  / TCP | SSL/TLS     |


