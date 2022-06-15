## Aks-engine Task
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#general-documentation">General Documentation</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#creating-the-cluster">Creating the cluster</a></li>
    <li><a href="#deploying-the-project">Deploy the project</a></li>
    <li><a href="#to-improve">To improve</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

### Infrastructure

* Created a ClusterDefinition file following the [Documentation](https://github.com/Azure/aks-engine/blob/master/docs/topics/clusterdefinitions.md)


* Provisioned a kubernetes cluster using aks-engine with  , as the task required

For cluster upgrade and maintenance - see [Guide](https://github.com/Azure/aks-engine/blob/master/docs/topics/upgrade.md)


## General Documentation

The project consists of two main APIs:

## BitcoinApi

### GET "/btc/USD"

Should return HTTP/200 with the current bitcoin price in USD, upon uri request to "/btc/USD"  

### GET "/btc/average"

Should return HTTP/200 with the last 10 minutes average bitcoin USD price, upon uri request to "/btc/average"  

### GET "/readiness"

Should return HTTP/200 with the string "OK", for readiness probes.

### GET "/liveness"

Should return HTTP/200 with the string "OK", for liveness probes.

<br/>

## RestApi

### GET "/"

Should return HTTP/200 with the following json: {'result' : 'OK'}

### GET "/readiness"

Should return HTTP/200 with the string "OK", for readiness probes.

### GET "/liveness"

Should return HTTP/200 with the string "OK", for liveness probes.

<p align="right">(<a href="#top">back to top</a>)</p>

## Prerequisites

* [Azure Subscription](https://azure.microsoft.com/en-us/)

Please install the following to run the project :

1. [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
2. [Aks-engine CLI](https://github.com/Azure/aks-engine/blob/master/docs/tutorials/quickstart.md#install-the-aks-engine-command-line-tool)
3. [Kubectl](https://kubernetes.io/docs/tasks/tools/)
4. [Helm](https://helm.sh/docs/intro/install/)

<br/>

### Built With

* [python-3.10](https://python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/quickstart/)

<br/>

### Creating the cluster

<br/>

To install the cluster on azure, run the following:
```console
az login
```
```console
aks-engine deploy --dns-prefix <AKS_Cluster_name> \
                    --resource-group <RG_name> \
                    --api-model aks-engine/ClusterDefinition.json \
                    --location <location>  \
                    --auto-suffix \ 
                    --subscription-id <subscription id>
```

<br/>

A new kubeconfig file is created at the _output folder, append the kubeconfig values to your context.
Optionally with this [guide](https://medium.com/@jacobtomlinson/how-to-merge-kubernetes-kubectl-config-files-737b61bd517d)



Now, lets ensure the cluster is running and kubectl is configured with the right context:

```console
kubectl cluster-info
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Installing the Ingress Controller

Install the Nginx ingress controller with a simple command:

```console
helm install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Deploying the project

to deploy the project, run a simple helm command:

```console
helm install aks-task ./Helm -n aks-task --create-namespace -f Helm/values.yaml 
```

Ensure evrything is working currectly:

```console
kubectl get pods -n aks-task
```

### Upgrading the project

After updating the code/chart, make sure to bump the version at Chart.yaml and in the chart defaults, when done - run :
what means bump ? give a guide or something
```console
helm upgrade aks-task ./Helm -n aks-task -f Helm/values.yaml 
```

### To improve
* `Monitoring` - Implement custom application metrics for production monitoring such as success rate, request rate, etc...
* `Logs` - Implement logging infra and application logs with severities.
* `TLS` - Configure the SSL-Offload at ingress level (with the helm chart)
* `Tests`
  * `Unit tests` - Integrate simple unit tests for the code .
  * `load test` - Integrate some kind of load tests as a part of the build process, using locust, siege, jmeter. alternatively i would develop a custom load tests tools.
* `Robustness`: Better handle api exceptions using mirror url's as backup or generating from a list on request initiation.
* `DB` - Integrate a simple DB (HA enabled) to calculate the average, and to save historical data.
* `GitOps` - Ideally add an automated workflow for continuous build and deployment.
* `Gunicorn optimizations`: I will try to take flask to the limit by tuninnig flask and gunicorn performance to ideally use its resources(procceses, handles, threads, etc..).  
* `Service mesh` - Maybe integrate service mesh to improve load balancing at scale, secure in-cluster communication with mTLS, and improve general network observability.
* `Projects seperation` - I would seperate the projects to a different repo's and helm charts, for much more comfortable and simpler versioning and workflow.
* `Helm chart documentation` - Write a full helm chart doc table. 

## Contact

Ben Touitou - bentzi259@gmail.com


<p align="right">(<a href="#top">back to top</a>)</p>


