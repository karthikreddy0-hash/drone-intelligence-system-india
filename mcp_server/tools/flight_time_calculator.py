

def flight_time_calculator(battery_capacity, drone_weight, payload_weight, weather):

    # -----------------------------
    # 1️⃣ Detect Drone Category
    # -----------------------------
    if 0 <= drone_weight <= 0.25:
        drone_category = "Nano"
    elif 0.25 < drone_weight <= 2:
        drone_category = "Micro"
    elif 2 < drone_weight <= 25:
        drone_category = "Small"
    elif 25 < drone_weight <= 150:
        drone_category = "Medium"
    else:
        drone_category = "Large"

    # -----------------------------
    # 2️⃣ Base Flight Time
    # -----------------------------
    base_time = battery_capacity / 300

    total_weight = drone_weight + payload_weight

    # -----------------------------
    # 3️⃣ Weather Impact
    # -----------------------------
    weather_factor = 1

    if weather == "windy":
        weather_factor = 0.8
    elif weather == "rainy":
        weather_factor = 0.7
    elif weather == "stormy":
        weather_factor = 0.6
    elif weather == "foggy":
        weather_factor = 0.85

    # -----------------------------
    # 4️⃣ Final Flight Time
    # -----------------------------
    estimated_time = (base_time - total_weight) * weather_factor

    if estimated_time < 10:
        recommendation = "Battery too low for safe operation"
    elif weather == "stormy":
        recommendation = "Avoid flying in stormy weather"
    else:
        recommendation = "Conditions suitable for flight"

    # -----------------------------
    # 5️⃣ Return Response
    # -----------------------------
    return {
        "drone_category": drone_category,
        "drone_weight": drone_weight,
        "payload_weight": payload_weight,
        "estimated_flight_time_minutes": round(estimated_time, 2),
        "weather_condition": weather,
        "recommendation": recommendation
    }