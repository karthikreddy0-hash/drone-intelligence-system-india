

def select_drone(use_case, budget, technical_requirements):

    min_flight_time = technical_requirements.get("min_flight_time", 0)
    min_payload = technical_requirements.get("min_payload", 0)
    camera_required = technical_requirements.get("camera_required", False)
    thermal_required = technical_requirements.get("thermal_required", False)

    drones = [
        {
            "model": "AgriDrone X1",
            "flight_time": 40,
            "payload": 10,
            "price": 90000,
            "camera": True,
            "thermal": False
        },
        {
            "model": "RescueDrone Pro",
            "flight_time": 60,
            "payload": 15,
            "price": 150000,
            "camera": True,
            "thermal": True
        }
    ]

    recommended = []

    for drone in drones:
        if (
            drone["price"] <= budget and
            drone["flight_time"] >= min_flight_time and
            drone["payload"] >= min_payload and
            (not camera_required or drone["camera"]) and
            (not thermal_required or drone["thermal"])
        ):
            recommended.append(drone)

    return recommended