{% include templates/edge/prerequisites.md %}

##### Provisioning edge on cloud and installation

Additionally, you will need to have IoT Hub **Edge** up and running and connected to the {{currentIoT HubVersion}} server.

{% if currentIoT HubVersion == "IoT Hub" %}
To provision IoT Hub **Edge** on {{currentIoT HubVersion}} server please visit this guide [Provision IoT Hub Edge on {{currentIoT HubVersion}} server](/docs/edge/provision-edge-on-server-pe/).
{% endif %}
{% if currentIoT HubVersion == "IoT Hub Community Edition" %}
To provision IoT Hub **Edge** on {{currentIoT HubVersion}} server please visit this guide [Provision IoT Hub Edge on {{currentIoT HubVersion}} server](/docs/edge/provision-edge-on-server-ce/).
{% endif %}

Once IoT Hub **Edge** provisioned on {{currentIoT HubVersion}} server please follow [Installation Guide](/docs/edge/install/installation-options/) - this guide will help you to install IoT Hub **Edge** and connect it to {{currentIoT HubVersion}} server.

{% if currentIoT HubVersion == "IoT Hub" %}
{% capture contenttogglespec %}
Cloud<br/><small>Connect edge to https://iothub.magenta.at</small>%,%ce%,%templates/edge/pe-cloud.md%br%
On-premise server<br/><small>Connect edge to on-premise instance</small>%,%pe%,%templates/edge/on-premise-cloud.md{% endcapture %}
{% include content-toggle.html content-toggle-id="cloudType" toggle-spec=contenttogglespec %}
{% endif %}
{% if currentIoT HubVersion == "IoT Hub Community Edition" %}
{% capture contenttogglespec %}
Live Demo<br/><small>Connect edge to https://iothub.magenta.at</small>%,%ce%,%templates/edge/ce-cloud.md%br%
On-premise server<br/><small>Connect edge to on-premise instance</small>%,%pe%,%templates/edge/on-premise-cloud.md{% endcapture %}
{% include content-toggle.html content-toggle-id="cloudType" toggle-spec=contenttogglespec %}
{% endif %}

{% include templates/edge/bind-port-changed-banner.md %} 

We are going to refer to this URL as **http://EDGE_URL** below in tutorial.