To provision dashboard to edge we need to open edge dashboards on **{{currentIoT HubVersion}}** server and assign the newly created dashboard. Once this dashboard is assigned we are going to open IoT Hub **Edge** UI to see the same dashboard on the edge.

Please open **{{currentIoT HubVersion}}** using the URL **http://SERVER_URL**.

{% if currentIoT HubVersion == "IoT Hub" %}
{% include images-gallery.html imageCollection="step6PE" showListImageTitles="true" %}{% endif %}
{% if currentIoT HubVersion == "IoT Hub Community Edition" %}
{% include images-gallery.html imageCollection="step6CE" showListImageTitles="true" %}{% endif %}

Let's open IoT Hub **Edge** UI using the URL **http://EDGE_URL**. to verify that dashboard was provisioned.

{% include images-gallery.html imageCollection="step6Edge" showListImageTitles="true" %}

Congratulations! Dashboard has been provisioned to the edge. Now you can send new telemetry reading, and it will immediately appear in the chart on the edge.
