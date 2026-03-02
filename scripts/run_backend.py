import os

print("Starting Backend Server...")
os.system("uvicorn api.main:app --reload")