# ML Model Serving Infrastructure

This project implements a complete local infrastructure to deploy, monitor, and manage a simple HuggingFace model-serving API using FastAPI, Docker, Kubernetes (via Minikube), Prometheus, and Grafana. CI/CD is handled via GitHub Actions.

---

## 📁 Project Structure

```
.
├── iac/                    # Infrastructure as code (Terraform for local Kubernetes setup)
│   └── main.tf             # Creates local Kubernetes namespace using ~/.kube/config
├── serving/                # Model serving application
│   └── app/                # FastAPI app with 4 key endpoints
│       └── main.py
│       └── Dockerfile
│       └── requirements.txt
├── k8s/                    # Kubernetes manifests
│   └── deployment.yml
│   └── service.yml
├── monitoring/             # Monitoring configs
│   └── servicemonitor.yml
│   └── setup-monitoring.sh
├── tests/                  # Unit tests
│   └── test_api.py
├── .github/workflows/      # CI/CD pipeline
│   └── ci-cd.yml
└── README.md
```

---

##  How to Run the Project

### Prerequisites

- Docker
- Python 3.10+
- Minikube (for local Kubernetes)
- kubectl
- helm (for Prometheus & Grafana)

---

###  Run Locally (No Kubernetes)

```bash
cd serving
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Or with Docker:

```bash
docker build -t ml-serving-app .
docker run -p 8000:8000 ml-serving-app
```

---

###  Run on Minikube (Recommended)

```bash
Deploy local infra with Terraform
cd iac
terraform init
terraform apply
cd ..

# Start minikube
minikube start --cpus 4 --memory 8g

# Deploy FastAPI app
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

# Deploy monitoring
kubectl apply -f monitoring/servicemonitor.yml
./monitoring/setup-monitoring.sh  # (optional script for Helm install)
```

---

###  Unit Tests

```bash
pytest tests/
```

---

##  API Endpoints

| Endpoint       | Method | Description                                |
|----------------|--------|--------------------------------------------|
| `/completion`  | POST   | Submits a chat request                     |
| `/status`      | GET    | Returns model deployment status            |
| `/model`       | GET    | Returns current model ID                   |
| `/model`       | POST   | Deploys a new model from HuggingFace       |

### Example `POST /model` request:

```json
{
  "model_id": "test-model"
}
```

### Example `POST /completion` request:

```json
{
  "messages": [ {"role": "user", "content": "Hi"} ]
}
```

---

##  GitHub Actions CI/CD

GitHub Actions pipeline includes:
- ✅ Dependency installation
- ✅ Lint and unit tests
- ✅ Docker image build
- ✅ Optional Kubernetes deployment (via `kubectl`)

---

##  Monitoring Setup

Metrics are exposed at `/metrics` using `prometheus-fastapi-instrumentator`.

- Prometheus scrapes this endpoint.
- Grafana dashboards are available at:
  - `localhost:<grafana-port>` (via Minikube service tunnel)
- Custom dashboard `fastapi_dashboard` visualizes:
  - Number of requests
  - Latency
  - Garbage collection
  - Uptime

---

##  System Design Highlights

- Built for local testability on a 1-node Minikube cluster.
- Fulfills p95 deployment latency under 3 minutes.
- Easily extendable to cloud using Terraform or Helm.
- Prometheus + Grafana integration enables rich observability.
- Fault-tolerant model state transitions using in-memory thread simulation.

---

##  Local Resource Limits (p99)

- 1 node
- 12 GB RAM
- 6 CPU cores
- 10 GB HDD

---

## ✅ Status Summary (Test Checklist)

| Requirement                          | Completed |
|--------------------------------------|-----------|
| Infrastructure as Code               | ✅         |
| CI/CD via GitHub Actions             | ✅         |
| REST API with 4 endpoints            | ✅         |
| Dockerized FastAPI app               | ✅         |
| Metrics exposed at `/metrics`        | ✅         |
| Prometheus + Grafana monitoring      | ✅         |
| Unit tests for public APIs           | ✅         |
| Minikube local deployment            | ✅         |
| Visual dashboard created             | ✅         |
