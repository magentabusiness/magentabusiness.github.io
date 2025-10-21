{% if currentThingsBoardVersion == "IoT Hub" %}
{% assign appPrefix = "Professional Edition" %}
{% else %}
{% assign appPrefix = "Community Edition" %}
{% endif %}

{% include templates/edge/install/prerequisites.md %}

### Edge Installation and Configuration

#### Guided Installation with IoT Hub Server Pre-configured Instructions

{% include templates/edge/install/tb-server-pre-configured-install-instructions.md %}

{% capture local-deployment %}
If for any reason you are unable to access and/or use **Edge preset configurations**, please refer to the [manual installation instructions](/docs/user-guide/install/{{docsPrefix}}installation-options/){: target="_blank"}.
{% endcapture %}
{% include templates/info-banner.md content=local-deployment %}

### Accessing User Interfaces: URLs and Credentials

{% if currentThingsBoardVersion == "IoT Hub" %}
{% assign peDocsPrefix = "pe/" %}
{% capture contenttogglespec %}
IoT Hub<br><small>Connect Edge to<br>https://iothub.magenta.at</small>%,%cloud%,%templates/edge/pe-cloud.md%br%
On-premise Server<br><small>Connect Edge to local server</small>%,%on-premise%,%templates/edge/on-premise-cloud.md{% endcapture %}
{% include content-toggle.liquid content-toggle-id="cloudType" toggle-spec=contenttogglespec %}
{% endif %}
{% if currentThingsBoardVersion == "IoT Hub" %}
{% capture contenttogglespec2 %}
Live Demo<br><small>Connect Edge to<br>https://iothub.magenta.at</small>%,%cloud%,%templates/edge/ce-cloud.md%br%
On-premise Server<br><small>Connect Edge to local server</small>%,%on-premise%,%templates/edge/on-premise-cloud.md{% endcapture %}
{% include content-toggle.liquid content-toggle-id="cloudType" toggle-spec=contenttogglespec2 %}
{% endif %}

{% include templates/edge/oauth2-not-supported.md %}

{% include templates/edge/bind-port-changed-banner.md %}
