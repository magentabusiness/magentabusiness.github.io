{% capture redis-notice %}
If you use Redis for caching, you need to flush all stored keys before starting the IoT Hub.

Connect to your Redis instance (or container/pod, depending on your setup) and run the command: 

`redis-cli flushall`

Please note that this command is applicable only if you use Redis exclusively for IoT Hub. If other applications use Redis, you need to locate the IoT Hub database and flush only that. The default database index is 0, configurable with REDIS_DB IoT Hub environment value.

`redis-cli`

`select 0`

`flushdb`
 
{% endcapture %}
{% include templates/info-banner.md content=redis-notice %}

