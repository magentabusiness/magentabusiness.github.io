{% assign deviceName = page.title | remove: "How to connect " | remove: " to IoT Hub?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/cat-1-container-tracker/" %}
{% assign thingsboardHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
'
%}

![{{deviceName}}](https://img.thingsboard.io/devices-library/{{page.deviceImageFileName}}){: style="float: left; max-width: 200px; max-height: 200px; margin: 0px 10px 0px 0px"}
[Cat-1 Container Tracker]({{deviceVendorLink}}){:target="_blank"} supports indoor and outdoor tracking, asset management with worldwide network coverage.<br>
It has 5-year battery life (30 minutes report interval) and IP68 enclosure and is perfect for tracking container, pallets, and assets in a wide area.<br>

## Prerequisites

To continue with this guide we will need the following:
{{prerequisites}}
- [ThingsBoard account]({{ thingsboardHost }}){: target="_blank"}

## Configuration

You will need to have access to IoT Hub.

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/create-device-on-thingsboard.md %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/check-data-on-thingsboard-cat-1-block.md %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/cat1/conclusion-cat-1-block.md %}