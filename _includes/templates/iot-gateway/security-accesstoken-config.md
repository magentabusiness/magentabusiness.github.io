
One type of security configuration is accessToken, 
to get it you should login into your IoT Hub platform instance, 
go to DEVICE tab, press the plus icon, 
fill the values and check the "Is gateway" option, 
open this device and press the "COPY ACCESS TOKEN" button and replace default with your value 


|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| accessToken              | **PUT_YOUR_GW_ACCESS_TOKEN_HERE**                     | Access token for the gateway from IoT Hub server.|
|---

Security subsection in configuration file will look like this: 

```yaml
...
  security:
    accessToken: PUT_YOUR_GW_ACCESS_TOKEN_HERE
...
```
