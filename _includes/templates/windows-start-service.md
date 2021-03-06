Now let's start the IoT Hub service!
Open the command prompt as an Administrator and execute the following command:

```shell
net start thingsboard
```

Expected output:

```text
The IoT Hub Server Application service is starting.
The IoT Hub Server Application service was started successfully.
```

In order to restart the IoT Hub service you can execute following commands:

```shell
net stop thingsboard
net start thingsboard
```

Once started, you will be able to open Web UI using the following link:

```bash
http://localhost:8080/
```

The following default credentials are available if you have specified *--loadDemo* during execution of the installation script:

- **System Administrator**: sysadmin@thingsboard.org / sysadmin
- **Tenant Administrator**: tenant@thingsboard.org / tenant
- **Customer User**: customer@thingsboard.org / customer

You can always change passwords for each account in account profile page.