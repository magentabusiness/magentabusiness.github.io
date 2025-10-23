{% capture cassandra-in-beta %}
Please note that Cassandra 4.x is still in beta. IoT Hub is compatible with Cassandra 3.x as well. 
However, since IoT Hub 3.2.2+ requires Java 11 and Cassandra 3.x is [not compatible](https://cassandra.apache.org/doc/latest/new/java11.html) with Java 8, you **can't launch IoT Hub 3.2.2+ and Cassandra 3.x on the same machine without separate docker containers for both.**.
{% if docsPrefix == "pe/" %}
Please consider using docker compose or other cluster setup 
to avoid issues with beta version of Cassandra.
{% else %}
Please consider using docker compose or other cluster setup
to avoid issues with beta version of Cassandra.
{% endif %}
{% endcapture %}
{% include templates/info-banner.md content=cassandra-in-beta %}
