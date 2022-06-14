## Aks-engine Task
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#creating">Creating the cluster</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br /> 


<!-- ABOUT THE PROJECT -->
## About The Project

<br/>

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

To install the cluster on azure, run the following:

```bash
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

```bash
export KUBECONFIG=<Project_path>/_output/<Cluster_Name><Generated_suffix>/kubeconfig/kubeconfig.<location>.json
```

Now, lets ensure the cluster is running and kubectl is configured with the right context:
```bash
kubectl cluster-info
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Installing the Ingress Controller
Install the Nginx ingress controller with a simple command:

```bash
helm install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

Kubectl:
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.0/deploy/static/provider/cloud/deploy.yaml
```

### Deploying the project:
to deploy the project, run a simple helm command:
```bash
helm install aks-task ./Helm -n aks-task --create-namespace -f Helm/values.yaml 
```

Ensure evrything is working currectly:

kubectl get pods -n micproject
```

##General Documentation:


