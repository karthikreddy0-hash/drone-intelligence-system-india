from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# -----------------------------
# MODELS
# -----------------------------

class FlightTimeRequest(BaseModel):
    battery_capacity: float
    drone_weight: float
    payload_weight: float
    weather: str


class ROIRequest(BaseModel):
    use_case: str
    initial_investment: float
    operational_cost: float
    yearly_revenue: float


class ComplianceRequest(BaseModel):
    specifications: dict
    intended_use: str
    location: str


class DroneSelectionRequest(BaseModel):
    use_case: str
    budget: float
    technical_requirements: dict


# -----------------------------
# FLIGHT TIME
# -----------------------------

@router.post("/calculate/flight-time")
def calculate_flight_time(data: FlightTimeRequest):

    total_weight = data.drone_weight + data.payload_weight

    if total_weight <= 0.25:
        category = "Nano"
    elif total_weight <= 2:
        category = "Micro"
    elif total_weight <= 25:
        category = "Small"
    else:
        category = "Medium"

    estimated_time = data.battery_capacity / (total_weight * 10)

    return {
        "drone_category": category,
        "drone_weight": data.drone_weight,
        "estimated_time": round(estimated_time, 2)
    }


# -----------------------------
# ROI
# -----------------------------

@router.post("/calculate/roi")
def calculate_roi(data: ROIRequest):

    net_profit = data.yearly_revenue - data.operational_cost
    roi_percentage = (net_profit / data.initial_investment) * 100
    break_even_years = data.initial_investment / net_profit

    return {
        "roi_percentage": round(roi_percentage, 2),
        "net_profit": net_profit,
        "break_even_years": round(break_even_years, 2)
    }


# -----------------------------
# COMPLIANCE
# -----------------------------

@router.post("/calculate/compliance")
def check_compliance(data: ComplianceRequest):

    permits = ["UIN Registration", "Operator Permit"]

    return {
        "status": "Compliant",
        "required_permits": permits
    }


# -----------------------------
# DRONE SELECTION
# -----------------------------

@router.post("/calculate/drone")
def select_drone(data: DroneSelectionRequest):

    best_drone = {
        "model": "AgriDrone X1",
        "flight_time": 40,
        "payload": 10,
        "camera": data.technical_requirements.get("high_res_camera", False)
    }

    return {
        "recommendation": best_drone
    }