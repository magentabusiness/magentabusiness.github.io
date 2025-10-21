{% capture postgresql-info %}
The IoT Hub team recommends using **PostgreSQL** for development and production environments with **moderate load (less than 5000 msg/sec)**.
Many cloud providers offer managed **PostgreSQL** services, making it a cost-effective solution for most IoT Hub deployments.
{% endcapture %}
{% include templates/info-banner.md content=postgresql-info %}

IoT Hub Edge uses **PostgreSQL** database as a local storage.

{% include templates/edge/install/postgres-install-rhel.md %}

{% include templates/edge/create-tb-db-rhel.md %}