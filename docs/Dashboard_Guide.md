# 📊 Drone Intelligence System Dashboard Guide

## 1️⃣ Introduction

The Drone Intelligence System Dashboard is built using Streamlit.

It provides multiple tools for drone analysis and business evaluation.

The dashboard connects to the FastAPI backend using API calls.

Dashboard URL:
http://localhost:8501



## 2️⃣ Sidebar Menu Options

The left sidebar contains the following tools:

- Chat with AI
- Flight Time
- ROI
- Compliance
- Drone Selection
- Upload
- Analytics

Users can select any tool from the dropdown menu.


## 3️⃣ Flight Time Calculator

This tool estimates drone flight time.

### Inputs:
- Battery Capacity (mAh)
- Drone Type
- Payload Weight (kg)
- Weather Condition

### Process:
1. Enter required values
2. Click "Calculate Flight Time"
3. Data is sent to backend endpoint:
   POST /calculate/flight-time
4. Backend calculates flight time
5. Result is displayed on dashboard


## 4️⃣ ROI Calculator

This tool calculates Return on Investment.

### Inputs:
- Use Case
- Initial Investment
- Operational Cost
- Yearly Revenue

### Process:
1. Enter values
2. Click "Calculate ROI"
3. Data sent to backend:
   POST /calculate/roi
4. ROI result displayed



## 5️⃣ Chat with AI

This tool allows users to interact with the AI assistant.

### Process:
1. Type a question
2. Click send
3. Ai is not fully developed 



## 6️⃣ Compliance

This section checks drone regulatory compliance rules.

User selects drone category and requirements.
Backend validates based on rules.

---

## 7️⃣ Drone Selection

This tool helps recommend suitable drones based on:
- Payload
- Budget
- Use case

Backend processes recommendation logic.

---

## 8️⃣ Upload

Allows users to upload datasets or files.
Used for analysis or model processing.

---

## 9️⃣ Analytics

Displays:
- Performance metrics
- Data visualization
- Insights

---

## 🔄 Backend Communication Flow

User Input  
↓  
Streamlit Frontend  
↓  
FastAPI Backend  
↓  
Business Logic  
↓  
JSON Response  
↓  
Dashboard Display  



## ⚙️ Technical Details

- Frontend: Streamlit
- Backend: FastAPI
- Port: 8501 (Frontend)
- Port: 8000 (Backend)
- Connected via Docker Composoe

## ✅ Summary

The dashboard provides:

✔ Financial analysis (ROI)  
✔ Operational analysis (Flight Time)  
✔ AI assistance  
✔ Compliance checking  
✔ Drone recommendation  
✔ File upload  
✔ Data analytics  

This demonstrates a complete full-stack drone intelligence system.