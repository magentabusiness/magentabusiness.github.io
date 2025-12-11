{% capture update_server_first %}
**Please make sure that IoT Hub Server version is {{serverVersion}} or above before updating IoT Hub Edge to this version**.

If the **IoT Hub Server** version is below {{serverVersion}}, please follow the upgrade instructions first.
{% endcapture %}
{% include templates/warn-banner.md content=update_server_first %}