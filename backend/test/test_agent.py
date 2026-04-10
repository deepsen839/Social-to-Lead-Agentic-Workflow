from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_full_lead_flow():
    session = "test1"

    client.post("/chat", json={"session_id": session, "message": "I want to buy"})
    client.post("/chat", json={"session_id": session, "message": "John"})
    client.post("/chat", json={"session_id": session, "message": "john@gmail.com"})
    res = client.post("/chat", json={"session_id": session, "message": "YouTube"})

    assert "captured" in res.json()["response"].lower()