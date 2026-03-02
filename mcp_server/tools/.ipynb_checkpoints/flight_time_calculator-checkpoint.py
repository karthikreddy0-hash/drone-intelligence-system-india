# mcp_server/tools/flight_time_calculator.py

def flight_time_calculator(battery_capacity, drone_weight, payload_weight, weather):
    base_time = battery_capacity / 300
    weight_factor = drone_weight + payload_weight
    weather_factor = 1
    #whether check
    if weather == "windy":
        weather_factor = 0.8
    elif weather == "rainy":
        weather_factor = 0.7

    estimated_time = (base_time - weight_factor) * weather_factor
    range_km = estimated_time * 0.5

    #bettery capacity check
    if estimated_time < 15:
        recommendation = "Consider higher capacity battery"
    elif weather == "windy":
        recommendation = "Avoid flying in strong wind"
    else:
       recommendation = "Conditions suitable for operation"
        
    return {
        "Estimated Flight Time (min)": round(estimated_time, 2),
        "Estimated Range (km)": round(range_km, 2),"recommendation":recommendation
    }