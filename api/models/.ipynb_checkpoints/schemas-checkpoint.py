from pydantic import BaseModel
from typing import Dict

class ChatRequest(BaseModel):
    query: str

class FlightRequest(BaseModel):
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
    specifications: Dict
    intended_use: str
    location: str

class DroneRequest(BaseModel):
    use_case: str
    budget: float
    technical_requirements:Dict