Install cURL for **Ubuntu**:

```bash
sudo apt-get install curl
```
{: .copy-code}


Install cURL for **macOS**:

```bash
brew install curl
```
{: .copy-code}

Install cURL for **Windows**:

Starting Windows 10 b17063, cURL is available by default. 
More info is available in this MSDB blog [post](https://blogs.msdn.microsoft.com/commandline/2018/01/18/tar-and-curl-come-to-windows/).
If you are using older version of Windows OS, you may find official installation guides [here](https://curl.haxx.se/).

<br/>

This command works for Windows, Ubuntu and macOS, assuming the cURL tool is already installed. 

**Access via public Internet** 
For example, access token is ABC123: 

```bash
curl -v -X POST -d "{\"temperature\": 25}" https://device.iothub.magenta.at/api/v1/ABC123/telemetry --header "Content-Type:application/json" 
```
{: .copy-code}

**Direct connected Device (with IoT Hub SIM-Card)** 
For example, access token is ABC123: 

```bash
curl -v -X POST -d "{\"temperature\": 25}" http://172.31.64.64/api/v1/ABC123/telemetry --header "Content-Type:application/json" 
```
{: .copy-code}



<br/>
<br/>
