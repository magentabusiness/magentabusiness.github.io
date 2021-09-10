#### Prerequisites
##### IoT Hub server 
To start using IoT Hub **Edge** you need to have IoT Hub CE/PE server that supports edge functionality up and running.

{% capture contenttogglespec %}
Community Edition%,%ce%,%templates/edge/obtain-ce-cloud.md%br%
IoT Hub%,%pe%,%templates/edge/obtain-pe-cloud.md{% endcapture %}

{% include content-toggle.html content-toggle-id="edgeInstallCloud" toggle-spec=contenttogglespec %} 
 
##### Edge provision on cloud
Additionally, you will need to provision IoT Hub **Edge** on cloud server. Please visit this guide [Provision edge on CE server](/docs/edge/provision-edge-on-server-ce/) or [Provision edge on PE server](/docs/edge/provision-edge-on-server-pe/) respectively.

Once IoT Hub **Edge** provisioned on cloud server please follow installation steps below.