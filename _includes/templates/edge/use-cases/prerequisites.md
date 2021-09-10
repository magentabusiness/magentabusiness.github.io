We assume you have completed the following guides and reviewed the articles listed below:

{% if currentIoT HubVersion == "IoT Hub" %}
* [Getting Started](/docs/edge/getting-started/getting-started-pe) guide.{% endif %}
{% if currentIoT HubVersion == "IoT Hub Community Edition" %}
* [Getting Started](/docs/edge/getting-started/getting-started-ce) guide.{% endif %}
* [Rule Engine Overview](/docs/user-guide/rule-engine-2-0/overview/) article.
* [IoT Hub Edge Getting Started](/docs/edge/getting-started/) article.
* [Edge Rule Engine Overview](/docs/edge/rule-engine/general/) guide.

Please make sure that you have **{{currentIoT HubVersion}}** server up and running. Additionally, IoT Hub **Edge** must be up, running and connected to the cloud.

If you have these prerequisites in place let's go to next steps.

{% if currentIoT HubVersion == "IoT Hub" %}
In other case please visit this link to provision edge on server [Provision Edge on {{currentIoT HubVersion}} server](/docs/edge/provision-edge-on-server-pe/).
{% endif %}
{% if currentIoT HubVersion == "IoT Hub Community Edition" %}
In other case please visit this link to provision edge on server [Provision Edge on {{currentIoT HubVersion}} server](/docs/edge/provision-edge-on-server-ce/).
{% endif %}

Once Edge provisioned on a server, please install it and connect to server using this [guide](/docs/edge/install/installation-options/).

{% include templates/edge/ui-url-aliases-banner.md %} 
