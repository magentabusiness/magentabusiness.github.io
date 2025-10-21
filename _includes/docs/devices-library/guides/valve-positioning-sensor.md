{% assign deviceName = page.title | remove: "How to connect " | remove: " to IoT Hub?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/valve-positioning-sensor/" %}
{% assign thingsboardHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [LoRaWAN Gateway](https://www.lansitec.com/products/outdoor-lorawan-gateway/){:target="_blank"}
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
- [Network Server account](https://www.chirpstack.io/){:target="_blank"}
'
%}

![{{deviceName}}](/images/devices-library/{{page.deviceImageFileName}}){: style="float: left; max-width: 200px; max-height: 200px; margin: 0px 10px 0px 0px"}
[Valve Positioning Sensor]({{deviceVendorLink}}){:target="_blank"} leverages LoRa technology and a built-in magnet sensor to track valve rotation angles with 1° accuracy.<br> 
This compact device measures both the direction and total number of turns, reporting real-time data to a LoRaWAN gateway.<br>
With configurable heartbeat intervals and operating modes, plus support for FOTA over Bluetooth, it delivers reliable performance and minimal maintenance in industrial or municipal environments.<br>

## Prerequisites

To continue with this guide we will need the following:
{{prerequisites}}
- [IoT Hub account]({{ thingsboardHost }}){: target="_blank"}

## Configuration

To create an integration with a network server please choose first one of the supported network servers:

{% assign targetIntegrationTypes = '
ChirpStack,
TheThingsStack,
TheThingsIndustries,
Loriot
' %}

{% include /docs/devices-library/blocks/integrations/external-platforms/add-device-through-integration-with-external-converter.liquid target-integration-types=targetIntegrationTypes %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/check-data-on-thingsboard-block.md %}

{% include /docs/devices-library/blocks/integrations/external-platforms/lansitec/conclusion-block.md %}
