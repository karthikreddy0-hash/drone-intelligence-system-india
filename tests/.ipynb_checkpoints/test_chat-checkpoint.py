from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_chat_drone():
    response = client.post("/chat", json={"query": "drone"})
    assert response.status_code == 200
    assert "response" in response.json()