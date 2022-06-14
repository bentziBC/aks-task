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
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>
<br />

## About The Project
<br/>

## General Documentation

The project consists of two main api's:

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
aks-engine deploy --dns-prefix <AKS_Cluster_name> \
                    --resource-group <RG_name> \
                    --api-model aks-engine/ClusterDefinition.json \
                    --location <location>  \
                    --auto-suffix \ 
                    --subscription-id <subscription id>
```

<br/>

To avoid complications, temporarily configure the newly created Kubeconfig file as an environment variable:

```console
export KUBECONFIG=<Project_path>/_output/<Cluster_Name><Generated_suffix>/kubeconfig/kubeconfig.<location>.json
```

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

Kubectl:

```console
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.0/deploy/static/provider/cloud/deploy.yaml
```

### Deploying the project

to deploy the project, run a simple helm command:

```console
helm install aks-task ./Helm -n aks-task --create-namespace -f Helm/values.yaml 
```

Ensure evrything is working currectly:

```console
kubectl get pods -n aks-task
```

## Contact

Ben Touitou - bentzi259@gmail.com