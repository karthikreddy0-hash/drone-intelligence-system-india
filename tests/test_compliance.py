from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_compliance():
    response = client.post("/calculate/compliance", json={
        "specifications": {
            "battery_capacity": 50000,
            "payload_weight": 5,
            "max_altitude": 120
        },
        "intended_use": "Agriculture",
        "location": "Hyderabad"
    })

    assert response.status_code == 200
    assert "status" in response.json()