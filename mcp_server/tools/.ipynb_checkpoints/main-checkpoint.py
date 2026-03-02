from fastapi import FastAPI
from pydantic import BaseModel

from tools.flight_time_calculator import calculate_flight_time
from tools.roi_calculator import calculate_roi
from tools.compliance_checker import check_compliance
from tools.drone_selector import select_drone

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Drone Intelligence MCP Server Running"}

# 1️⃣ Flight Time
@app.post("/flight-time")
def flight_time(data: dict):
    return calculate_flight_time(
        data["battery_capacity"],
        data["drone_weight"],
        data["payload_weight"],
        data["weather"]
    )

# 2️⃣ ROI
@app.post("/roi")
def roi(data: dict):
    return calculate_roi(
        data["initial_investment"],
        data["monthly_cost"],
        data["monthly_revenue"]
    )

# 3️⃣ Compliance
@app.post("/compliance")
def compliance(data: dict):
    return check_compliance(
        data["weight"],
        data["location"],
        data["use_case"]
    )

# 4️⃣ Drone Selection
@app.post("/select-drone")
def drone_select(data: dict):
    return select_drone(
        data["use_case"],
        data["budget"]
    )