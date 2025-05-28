from fastapi import FastAPI, Request
from pydantic import BaseModel
import time
from threading import Thread

app = FastAPI()

state = {
    "status": "NOT_DEPLOYED",
    "model_id": None,
    "model": None
}

class Message(BaseModel):
    role: str
    content: str

class CompletionRequest(BaseModel):
    messages: list[Message]

class ModelRequest(BaseModel):
    model_id: str

@app.post("/completion")
async def completion(request: CompletionRequest):
    if state["status"] != "RUNNING":
        return {"status": "error", "message": "Model not running"}
    return {"status": "success", "response": [{"role": "assistant", "message": "This is a response"}]}

@app.get("/status")
async def get_status():
    return {"status": state["status"]}

@app.get("/model")
async def get_model():
    return {"model_id": state["model_id"]}

@app.post("/model")
async def deploy_model(model_request: ModelRequest):
    if state["status"] == "RUNNING":
        return {"status": "error", "message": "Model already running"}
    state["status"] = "PENDING"
    state["model_id"] = model_request.model_id

    def simulate_deploy():
        time.sleep(10)
        state["status"] = "RUNNING"

    Thread(target=simulate_deploy).start()
    return {"status": "success", "model_id": model_request.model_id}
