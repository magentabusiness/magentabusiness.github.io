{% capture tb_3_7_0_upgrade_note %}
**Important note before upgrading to IoT Hub 3.7**

IoT Hub backend was migrated to Java 17. Install JDK 17 and ensure that system's default Java version is set to 17.

{% endcapture %}
{% include templates/warn-banner.md content=tb_3_7_0_upgrade_note %}