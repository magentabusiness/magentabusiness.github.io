{% if currentThingsBoardVersion == "IoT Hub" %}
{% assign peDocsPrefix = "pe/" %}
{% endif %}

You can install the **IoT Hub {{appPrefix}}** local server. For this, please refer to the [IoT Hub installation guide](/docs/user-guide/install/{{peDocsPrefix}}installation-options/){:target="_blank"}. 

The local server can be accessed via [http://localhost:8080](http://localhost:8080){:target="_blank"}. Throughout this tutorial, we will refer to this URL as **SERVER_URL.** Log in with:
* **Username:** tenant@thingsboard.org
* **Password:** tenant
