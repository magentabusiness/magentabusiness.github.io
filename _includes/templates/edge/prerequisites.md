##### IoT Hub server 

To start using IoT Hub **Edge** you need to have {{currentIoT HubVersion}} server that supports edge functionality up and running. 

{% if currentIoT HubVersion == "IoT Hub" %}
{% include templates/edge/obtain-pe-cloud.md %}
{% endif %}
{% if currentIoT HubVersion == "IoT Hub Community Edition" %}
{% include templates/edge/obtain-ce-cloud.md %}
{% endif %}