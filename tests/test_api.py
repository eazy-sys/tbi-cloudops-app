from fastapi.testclient import TestClient
from serving.app.main import app

client = TestClient(app)

def test_model_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "status" in response.json()

def test_model_deploy():
    response = client.post("/model", json={"model_id": "test-model"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_completion_before_ready():
    response = client.post("/completion", json={"messages": [{"role": "user", "content": "Hi"}]})
    assert response.status_code == 200
    assert response.json()["status"] == "error"
