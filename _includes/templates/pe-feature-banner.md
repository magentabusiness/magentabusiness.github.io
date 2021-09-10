{% capture peFeatureContent %}
Only [**IoT Hub**](/products/thingsboard-pe/) supports **{{ feature }}** feature.<br>
Use [**IoT Hub**](https://thingsboard.cloud/signup) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.
{% endcapture %}
{% include templates/info-banner.md title="IoT Hub Feature" content=peFeatureContent %}
