# 📘 Drone Intelligence System – API Documentation

## 🔹 Base URL

Backend runs locally at:
http://localhost:8000

Swagger UI:
http://localhost:8000/docs


# 📌 Available API Endpoints



##1️⃣ Chat API

###Endpoint
POST /chat

##description
Allows users to interact with the AI assistant.

###Request Body
```json
{
  "message": "What is the best drone for agriculture?"
}
```

###Response
```json
{
  "response": "For agriculture, a drone with high payload capacity and long battery life is recommended."
}


## 2️⃣ Flight Time Calculator

### Endpoint
POST /calculate/flight-time

### Description
Calculates estimated drone flight time.

### Request Body
```json
{
  "battery_capacity": 50000,
  "drone_type": "Nano",
  "payload_weight": 2.0,
  "weather_condition": "Normal"
}


### Response
```json
{
  "estimated_flight_time_minutes": 45.5,
  "drone_weight": 0.25
}


## 3️⃣ ROI Calculator

### Endpoint
POST /calculate/roi

### Description
Calculates return on investment.

### Request Body
```json
{
  "use_case": "Agriculture",
  "initial_investment": 5000000,
  "operational_cost": 45000,
  "yearly_revenue": 670000
}


### Response
```json
{
  "roi_percentage": 12.5,
  "net_profit": 625000
}


## 4️⃣ Compliance Check

### Endpoint
POST /compliance/check

### Description
Validates drone compliance with regulations.

### Request Body
```json
{
  "drone_category": "Nano",
  "location": "India"
}

### Response
```json
{
  "compliant": true,
  "message": "Drone meets regulatory requirements."
}

##  5️⃣ Drone Recommendation

### Endpoint
POST /drone/recommend

### Description
Recommends suitable drone based on user input.

### Request Body
```json
{
  "budget": 1000000,
  "payload_requirement": 3.0,
  "use_case": "Delivery"
}


### Response
```json
{
  "recommended_drone": "X-Delivery Pro",
  "estimated_cost": 950000
}




## 6️⃣ File Upload

### Endpoint
POST /upload

### Description
Uploads dataset for processing.

### Request
Form-data file upload.

### Response
```json
{
  "status": "File uploaded successfully"
}


#🔄 Response Format

All APIs return JSON responses.

Success:
- HTTP 200 OK

Client Error:
- HTTP 400 (Invalid Input)

Server Error:
- HTTP 500 (Internal Server Error)




# 📌 Summary

The Drone Intelligence System API provides:

✔ AI Chat Support  
✔ Flight Time Estimation  
✔ ROI Calculation  
✔ Compliance Checking  
✔ Drone Recommendation  
✔ File Upload Support  

Built using FastAPI with JSON-based communication.