### Monitor the IoT Hub Java application

To monitor IoT Hub application we will use the [Visual VM](https://visualvm.github.io/)
The JMX have been enabled in `docker-compose.yml` with this line

```bash
JAVA_OPTS: " -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9999 -Dcom.sun.management.jmxremote.rmi.port=9999 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=127.0.0.1"
```

Let's **forward JMX port** from IoT Hub instance to the local machine

```bash
ssh -L 9999:127.0.0.1:9999 thingsboard 
```

Now we can connect with VisualVM to the IoT Hub application and discover the internals

![IoT Hub JMX overview with VisualVM](/images/reference/performance-aws-instances/method/chart-examples/performance_test_thingsboard_jmx_visual_vm_overview.png "IoT Hub JMX overview with VisualVM")

