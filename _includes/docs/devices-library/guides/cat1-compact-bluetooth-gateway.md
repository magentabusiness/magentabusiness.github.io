{% assign deviceName = page.title | remove: "How to connect " | remove: " to IoT Hub?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/cat-1-badge-tracker/" %}
{% assign thingsboardHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
'
%}

![{{deviceName}}](/images/devices-library/{{page.deviceImageFileName}}){: style="float: left; max-width: 200px; max-height: 200px; margin: 0px 10px 0px 0px"}
[Cat-1 Compact Bluetooth Gateway](https://www.lansitec.com/products/cat-1-compact-bluetooth-gateway/){:target="_blank"} receives nearby Bluetooth beacons, sensors, or controllers&#39; data, restructure, and forward it to a server via Cat-1.<br>
It supports iBeacon, Eddystone, private protocols, and the scan and response feature.<br>
The integrated 600mAh lithium-ion rechargeable battery provides an operational duration of approximately 10 hours of operation when no external power source is available.<br>

## Prerequisites

To continue with this guide we will need the following:
{{prerequisites}}
- [ThingsBoard account]({{ thingsboardHost }}){: target="_blank"}

## Configuration

You will need to have access to IoT Hub. 

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/create-device-on-thingsboard.md %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/check-data-on-thingsboard-cat-1-block.md %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/conclusion-cat-1-block.md %}