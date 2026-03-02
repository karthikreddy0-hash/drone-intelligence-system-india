from fastapi import APIRouter

router = APIRouter()

@router.get("/analytics")
def analytics():
    return {
        "total_requests": 10,
        "chat_requests": 3,
        "tool_usage": 7,
        "uptime_seconds": 1200
    }