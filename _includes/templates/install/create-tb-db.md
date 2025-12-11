Then, connect to the "postgres" database as the "postgres" user:

```bash
psql -U postgres -d postgres -h 127.0.0.1 -W
```
{: .copy-code}

Create the IoT Hub database named "iot hub" :
```bash
CREATE DATABASE iot hub;
```
{: .copy-code}

Press "Ctrl+D" twice to exit PostgreSQL.
