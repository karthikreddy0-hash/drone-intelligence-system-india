from fastapi import APIRouter
from api.models.schemas import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    query = request.query.lower()

    if "drone" in query:
        return {
            "response": (
                "Drones are unmanned aerial vehicles (UAVs) used in agriculture, "
                "medical supply delivery, defense surveillance, disaster management, "
                "mining surveys, and mapping. "
                "They are classified as Nano, Micro, Small, Medium, or Large "
                "based on weight and capability."
            )
        }

    elif "flight time" in query:
        return {
            "response": (
                "Flight time depends on battery capacity, drone weight, "
                "payload weight, and weather conditions."
            )
        }

    elif "roi" in query:
        return {
            "response": (
                "ROI (Return on Investment) measures profitability. "
                "It is calculated using initial investment, operational cost, "
                "and yearly revenue."
            )
        }

    elif "compliance" in query:
        return {
            "response": (
                "Drone compliance ensures that altitude limits, safety regulations, "
                "and regional aviation rules are followed."
            )
        }

    else:
        return {
            "response": "I can help with drones, flight time, ROI, compliance, or drone selection."
        }