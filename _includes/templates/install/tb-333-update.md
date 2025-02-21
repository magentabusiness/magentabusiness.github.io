{% capture tb_3_3_3_upgrade_note %}
**Important note before upgrading to IoT Hub 3.3.3**

IoT Hub UI was migrated to Angular 12. You need to re-build your custom widgets and rule nodes (which use UI) on Angular 12.

{% endcapture %}
{% include templates/info-banner.md content=tb_3_3_3_upgrade_note %}