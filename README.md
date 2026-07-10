# DevOps Assignment

## Overview

This project automates the deployment of a simple web application.

The deployment script performs the following tasks:

- Clone a GitHub repository
- Detect whether the application is HTML or PHP
- Generate a Dockerfile automatically
- Build a Docker image
- Deploy the application to Kubernetes
- Monitor the repository for new changes

---

## Project Structure

```
DevOps-test/
│
├── app/
│   └── index.html
│
├── scripts/
│   └── deploy.py
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── pvc.yaml
│   └── hpa.yaml
│
├── helm/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── Dockerfile
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- Git
- Docker
- Kubernetes
- Helm
- GitHub Actions

---

## Prerequisites

Before running the project, install:

- Python 3.x
- Git
- Docker Desktop
- Kubernetes (kubectl)
- Helm

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/SharmaRajat10/devops-assignment.git
```

Go to the project folder:

```bash
cd DevOps-test
```

Run the deployment script:

```bash
python scripts/deploy.py
```

---

## Kubernetes Files

The `k8s` folder contains:

- Deployment
- Service
- Ingress
- Persistent Volume Claim (PVC)
- Horizontal Pod Autoscaler (HPA)

---

## Helm Chart

The `helm` folder contains:

- Chart.yaml
- values.yaml
- Kubernetes templates

---

## GitHub Actions

GitHub Actions workflow is available in:

```
.github/workflows/deploy.yml
```

The workflow automatically runs when code is pushed to the `main` branch.

---

## Author

Rajat Sharma
