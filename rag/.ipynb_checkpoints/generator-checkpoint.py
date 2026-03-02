# rag/generator.py

import requests
import json

API_KEY = "AIzaSyC_YmP3smtHzW4Ub7UBQDo8JTMjSa_iiqw"

def generate_with_gemini(prompt):
    
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    result = response.json()
    
    return result
