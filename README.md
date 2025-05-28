# ML Model Serving Infrastructure

This project sets up a local infrastructure using FastAPI, Docker, and optionally Kubernetes, to deploy a machine learning model and expose REST APIs.

## Project Structure

- `iac/`: Infrastructure as Code (placeholder for cloud infra like AKS).
- `serving/`: FastAPI-based ML model serving application.
- `tests/`: Unit tests for API.
- `.github/workflows/`: GitHub Actions CI/CD pipeline.

## How to Run

### Prerequisites

- Docker
- Python 3.10+
- (Optional) Minikube or Kind for local Kubernetes

### Run Locally

```bash
cd serving
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Build and Run with Docker

```bash
docker build -t ml-serving-app .
docker run -p 8000:8000 ml-serving-app
```

### Run Tests

```bash
pytest tests/
```

### API Endpoints

- `POST /completion` – Chat model interaction
- `GET /status` – Model status
- `GET /model` – Get deployed model ID
- `POST /model` – Deploy a model

## CI/CD

This project uses GitHub Actions to:
- Install dependencies
- Run tests
- Build the Docker image
