# mcp_server/main.py

from fastapi import FastAPI
from mcp_server.tools.flight_time_calculator import flight_time_calculator
from mcp_server.tools.roi_calculator import roi_calculator
from mcp_server.tools.compliance_checker import check_compliance
from mcp_server.tools.drone_selector import select_drone

app = FastAPI(title="Drone Intelligence MCP Server")


# -----------------------------
# Flight Time Endpoint
# -----------------------------
@app.post("/calculate/flight-time")
def calculate_flight_time(data: dict):
    return flight_time_calculator(
        battery_capacity=data["battery_capacity"],
        drone_weight=data["drone_weight"],
        payload_weight=data["payload_weight"],
        weather=data["weather"]
    )


# -----------------------------
# ROI Calculator Endpoint
# -----------------------------
@app.post("/calculate/roi")
def calculate_roi(data: dict):
    return roi_calculator(
        use_case=data["use_case"],
        initial_investment=data["initial_investment"],
        operational_cost=data["operational_cost"],
        yearly_revenue=data["yearly_revenue"]
    )


# -----------------------------
# Compliance Checker Endpoint
# -----------------------------
@app.post("/check/compliance")
def compliance(data: dict):
    return check_compliance(
        specifications=data["specifications"],
        intended_use=data["intended_use"],
        location=data["location"]
    )


# -----------------------------
# Drone Recommendation Endpoint
# -----------------------------
@app.post("/recommend/drone")
def recommend_drone(data: dict):
    return select_drone(
        use_case=data["use_case"],
        budget=data["budget"]
    )


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "Drone Intelligence MCP Server Running Successfully 🚀"}