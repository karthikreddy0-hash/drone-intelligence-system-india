from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_flight_time():
    response = client.post("/calculate/flight-time", json={
        "battery_capacity": 50000,
        "drone_weight": 0.25,
        "payload_weight": 2,
        "weather": "Normal"
    })

    assert response.status_code == 200
    assert "estimated_time" in response.json()