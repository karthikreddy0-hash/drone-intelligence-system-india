from fastapi import FastAPI
from api.routes import chat, calculations, analytics,upload

app = FastAPI(title="Drone Intelligence System")

app.include_router(chat.router)
app.include_router(calculations.router)
app.include_router(upload.router)
app.include_router(analytics.router)
