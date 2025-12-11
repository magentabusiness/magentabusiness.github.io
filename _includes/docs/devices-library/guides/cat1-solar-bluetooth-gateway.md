{% assign deviceName = page.title | remove: "How to connect " | remove: " to IoT Hub?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/cat-1-solar-bluetooth-gateway/" %}
{% assign thingsboardHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
'
%}

![{{deviceName}}](/images/devices-library/{{page.deviceImageFileName}}){: style="float: left; max-width: 200px; max-height: 200px; margin: 0px 10px 0px 0px"}
[Cat-1 Solar Bluetooth Gateway]({{deviceVendorLink}}){:target="_blank"} receives data from nearby [Bluetooth beacons](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}, sensors, or controllers, restructures it, and forwards it to a server via Cat-1 connectivity.<br>
It supports iBeacon, Eddystone, private protocols, and both scan and response features.<br>
Equipped with a solar panel and a low-temperature rechargeable battery, the gateway is maintenance-free, even in harsh environmental conditions.<br>

## Prerequisites

To continue with this guide we will need the following:
{{prerequisites}}
- [IoT Hub account]({{ thingsboardHost }}){: target="_blank"}

## Configuration

You will need to have access to IoT Hub. 

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/create-device-on-thingsboard.md %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/check-data-on-thingsboard-cat-1-block.md %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/conclusion-cat-1-block.md %}