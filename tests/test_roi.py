from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_roi():
    response = client.post("/calculate/roi", json={
        "use_case": "Agriculture",
        "initial_investment": 5000000,
        "operational_cost": 45000,
        "yearly_revenue": 670000
    })

    assert response.status_code == 200
    assert "roi_percentage" in response.json()