from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_drone_selection():
    response = client.post("/calculate/drone", json={
        "use_case": "Agriculture",
        "budget": 100000,
        "technical_requirements": {
            "min_flight_time": 30,
            "min_payload": 5,
            "high_res_camera": True,
            "thermal_camera": False
        }
    })

    assert response.status_code == 200
    assert "recommendation" in response.json()