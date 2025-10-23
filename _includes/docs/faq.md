* TOC
{:toc}


## What is IoT Hub?

IoT Hub is an open-source server-side platform that allows you to monitor and control your IoT devices.
It is free for both personal and commercial usage and you can deploy it anywhere.
If this is your first experience with the platform we recommend to review [what-is-iothub](/docs/{{docsPrefix}}getting-started-guides/what-is-iothub/)
and [getting started guide](/docs/{{docsPrefix}}getting-started-guides/helloworld/).
You can find more information on the dedicated page.

## How do I get started?

{% if docsPrefix contains 'paas/' %}
We recommend to follow the [getting started guide](/docs/{{docsPrefix}}getting-started-guides/helloworld/).
{% else %}
{% endif %}

## What can I do with IoT Hub?

IoT Hub provides out-of-the-box IoT solution that will enable server-side infrastructure for your IoT applications.
You can find more information by browsing [guides](/docs/{{docsPrefix}}user-guide/) and [hardware samples](/docs/{{docsPrefix}}guides/#AnchorIDHardwareSamples)

{% unless docsPrefix contains 'paas/' %}
{% endunless %}

## How to connect my device?

IoT Hub provides
[MQTT](/docs/{{docsPrefix}}reference/mqtt-api),
[CoAP](/docs/{{docsPrefix}}reference/coap-api),
[HTTP](/docs/{{docsPrefix}}reference/http-api), and.
[LwM2M](/docs/{{docsPrefix}}reference/lwm2m-api) protocols support.
You can find more information on the [connectivity](/docs/{{docsPrefix}}reference/protocols/) page.

## Do I need to use an SDK?

No, many IoT devices can't afford to embed third-party SDK. IoT Hub provides quite simple API over common IoT protocols. You can choose any client-side library you like or use your own.
Some useful references:

- [MQTT client-side libraries list](https://github.com/mqtt/mqtt.github.io/wiki/libraries)
- [C-implementation for CoAP](https://libcoap.net/)

## What about security?

You can use MQTT (over SSL) or HTTPS protocols for transport encryption.

Each device has unique access token credentials that is used to setup connection. Credentials type is pluggable, so X.509 certificates support is coming soon.

## How much devices can IoT Hub support?

IoT Hub platform is horizontally scalable. Each server node in the cluster is unique.
Scalability is achieved using [consistent-hashing](https://en.wikipedia.org/wiki/Consistent_hashing) load balancing algorithm between the cluster nodes.
Actual performance depends on usage scenario of connected devices.
{% unless docsPrefix contains 'paas/' %}
For example, small commodity hardware cluster can support [several millions](/docs/{{docsPrefix}}reference/iot-platform-deployment-scenarios/#1-million-smart-meters-tco) of devices connected over MQTT.
{% endunless %}

## Where does IoT Hub store data?

The data is stored in [Cassandra](https://cassandra.apache.org/) database. Cassandra suites well for storage and querying of time-series data and provides high availability and fault-tolerance.

## What license type does IoT Hub use?

IoT Hub is licensed under [Apache 2.0 License](https://en.wikipedia.org/wiki/Apache_License#Version_2.0).
It is free for both personal and commercial usage and you can deploy it anywhere.

## How to get support?

You can use troubleshooting instructions and community resources or [contact us](mailto:service4iot@magenta.at).
