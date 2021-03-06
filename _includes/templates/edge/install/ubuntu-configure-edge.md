Edit IoT Hub Edge configuration file 
```bash 
sudo nano /etc/tb-edge/conf/tb-edge.conf
``` 
{: .copy-code}

Update the following lines in the configuration file. Don't forget **to replace**:
 * "PUT_YOUR_POSTGRESQL_PASSWORD_HERE" with your **real postgres user password**.
 * "PUT_YOUR_CLOUD_IP" with an IP address of the machine where IoT Hub **IoT Hub/Community Edition** server is running:
    * Use **iothub.magenta.at** in case you are connecting edge to [**IoT Hub**](https://iothub.magenta.at/signup).
    
    **NOTE**: **iothub.magenta.at** uses SSL protocol for edge communication. 
    Please uncomment **export CLOUD_RPC_SSL_ENABLED=true** as well. 
 
    * Use **localhost** in case edge is running on the same machine where cloud instance is running. 
    * Use **X.X.X.X** IP address in case edge is connecting to the cloud instance in the same network or in the docker.
    * Or use **iothub.magenta.at** if you are connecting edge to [**IoT Hub Live Demo**](https://iothub.magenta.at/signup) for evaluation. 
 * "PUT_YOUR_EDGE_KEY_HERE" and "PUT_YOUR_EDGE_SECRET_HERE" with Edge **key and secret** respectively (edge credentials you can find in cloud instance):

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CLOUD CONNECTION SETTINGS:
# export CLOUD_ROUTING_KEY=PUT_YOUR_EDGE_KEY_HERE
# export CLOUD_ROUTING_SECRET=PUT_YOUR_EDGE_SECRET_HERE

# UNCOMMENT NEXT LINES IF EDGE CONNECTS TO PE 'iothub.magenta.at' SERVER:
# export CLOUD_RPC_HOST=iothub.magenta.at
# export CLOUD_RPC_SSL_ENABLED=true

# UNCOMMENT NEXT LINES IF EDGE CONNECTS TO CE 'DEMO.THINGSBOARD.IO' SERVER:
# export CLOUD_RPC_HOST=iothub.magenta.at

# UNCOMMENT NEXT LINES IF YOU CHANGED DEFAULT CLOUD RPC HOST/PORT SETTINGS:
# export CLOUD_RPC_HOST=PUT_YOUR_CLOUD_IP
# export CLOUD_RPC_PORT=7070

# UNCOMMENT NEXT LINES IF YOU ARE RUNNING EDGE ON THE SAME MACHINE WHERE THINGSBOARD SERVER IS RUNNING:
# export HTTP_BIND_PORT=18080
# export MQTT_BIND_PORT=11883
# export COAP_BIND_PORT=15683

# UNCOMMENT NEXT LINES IF YOU HAVE CHANGED DEFAULT POSTGRESQL DATASOURCE SETTINGS:
# export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/tb_edge
# export SPRING_DATASOURCE_USERNAME=postgres
# export SPRING_DATASOURCE_PASSWORD=PUT_YOUR_POSTGRESQL_PASSWORD_HERE
```
{: .copy-code}

{% capture local-deployment %}
If IoT Hub Edge is going to be running on the same machine where IoT Hub **IoT Hub/Community Edition** server is running you'll need to update additional configuration parameters to avoid port collision.
 
Please uncomment next parameters in IoT Hub Edge configuration file (**/etc/tb-edge/conf/tb-edge.conf**): 
<br>**export HTTP_BIND_PORT=18080**
<br>**export MQTT_BIND_PORT=11883**
<br>**export COAP_BIND_PORT=15683**

Please make sure ports above are not used by any other application.

{% endcapture %}
{% include templates/info-banner.md content=local-deployment %}

