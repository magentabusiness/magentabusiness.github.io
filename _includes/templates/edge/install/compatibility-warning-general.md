{% if page.url contains 'upgrade-instructions' %}
Before upgrading **IoT Hub Edge**, ensure that **IoT Hub Server** is [updated to the latest version](/docs/user-guide/install/{{docsPrefix}}upgrade-instructions/){: target="_blank"}.

Additionally, verify that the **IoT Hub Edge** and **IoT Hub Server** versions **are compatible**.
{% else %}
Before installing **IoT Hub Edge**, ensure that **IoT Hub Server** is [installed](/docs/user-guide/install/{{peDocsPrefix}}installation-options/){: target="_blank"} and [updated](/docs/user-guide/install/{{peDocsPrefix}}upgrade-instructions/){: target="_blank"} to the latest version.

Additionally, verify that the **IoT Hub Edge** and **IoT Hub Server** versions **are compatible**.
{% endif %}

{% capture update_server_first %}
## **Version Compatibility Rules:**
* **IoT Hub Edge version X.Y.Z** works with the **IoT Hub Server version X.Y.Z** and the next <span style="color:blue">**two**</span> versions.

_**IoT Hub Edge 3.8.0** works with **IoT Hub Server 3.8.0** and two later versions (3.9.0 and 3.9.1). You can view the **IoT Hub Server Release Notes** [here](/docs/{{peDocsPrefix}}reference/releases/){: target="_blank"}._

* **IoT Hub Edge version X.Y.Z** <span style="color:red">**does not work**</span> with **older** IoT Hub Server versions.

_**IoT Hub Edge 3.9.1** does not support **IoT Hub Server 3.8.0** or any **earlier versions**. In such cases, the **IoT Hub Server** must be [upgraded to the latest version](/docs/user-guide/install/{{peDocsPrefix}}upgrade-instructions/){: target="_blank"} first._

{% endcapture %}
{% include templates/warn-banner.md content=update_server_first %}

{% capture note %}
_If you run an **older version of IoT Hub Edge** (e.g., version 3.6.0), the IoT Hub team cannot guarantee the availability or proper functioning of all features._
{% endcapture %}
{% include templates/info-banner.md content=note %}


