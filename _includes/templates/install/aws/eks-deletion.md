## Cluster deletion

Execute the following command to delete all IoT Hub pods:

```bash
./k8s-delete-resources.sh
```
{: .copy-code}

Execute the following command to delete all IoT Hub pods and configmaps:

```bash
./k8s-delete-all.sh
```
{: .copy-code}

Execute the following command to delete EKS cluster (you should change the name of the cluster and zone):

```bash
eksctl delete cluster -r us-east-1 -n thingsboard -w
```
{: .copy-code}
