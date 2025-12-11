Send GET request with Observe option to the following URL:

{% if docsPrefix == null or docsPrefix == "pe/"%}
```shell
coap://iothub.magenta.at/api/v1/attributes
```
{: .copy-code}

Where **iothub.magenta.at** is your localhost, or the platform address.

{% endif %}
{% if docsPrefix == null %}

If you use live demo server, the command will look like this:

```shell
coap://iothub.magenta.at/api/v1/attributes
```
{: .copy-code}
{% endif %}
{% if docsPrefix == "paas/" or docsPrefix == "paas/eu/"%}
```shell
coap://{{coapHostName}}/api/v1/attributes
```
{: .copy-code}

{% endif %}