### synthetic drone flight data
import pandas as pd
import random
import os

os.makedirs("data/synthetic", exist_ok=True)

drone_types = {"Nano": 0.25, "Micro": 2, "Small": 10, "Medium": 25, "Large": 50}
weather_types = ["Normal", "Windy", "Rainy", "Summer", "Stormy"]
use_cases = ["Agriculture", "Medical", "Defense", "Survey", "Disaster"]

data = [
    [
        random.choice(use_cases),
        drone := random.choice(list(drone_types.keys())),
        battery := random.randint(15000, 60000),
        payload := round(random.uniform(1, 20), 2),
        weather := random.choice(weather_types),
        max(10, round(
            ((battery / 1000)
             - (drone_types[drone] * 0.5)
             - (payload * 0.8))
            * {"Normal":1,"Summer":0.9,"Rainy":0.8,"Windy":0.7,"Stormy":0.6}[weather],
            2
        ))
    ]
    for _ in range(1000)
]

df = pd.DataFrame(data, columns=[
    "use_case",
    "drone_type",
    "battery_capacity_mAh",
    "payload_weight_kg",
    "weather_condition",
    "estimated_flight_time_minutes"
])

df.to_csv("data/synthetic/drone_flight_data.csv", index=False)

df.head()




####business synthetic data
import pandas as pd
import random
import os

os.makedirs("data/synthetic", exist_ok=True)

use_cases = ["Agriculture", "Medical", "Defense", "Disaster", "Mining"]
regions = ["Telangana", "Karnataka", "Maharashtra", "Delhi", "Tamil Nadu"]
scales = ["Small", "Medium", "Large"]

data = [
    [
        random.choice(use_cases),
        random.choice(regions),
        random.choice(scales),
        random.randint(5, 50),            # manpower
        random.randint(1, 20),            # drones
        revenue := random.randint(5_00_000, 50_00_000),
        cost := random.randint(2_00_000, 20_00_000),
        revenue - cost,                   # profit
        round(random.uniform(5, 25), 2)   # market growth %
    ]
    for _ in range(200)
]

df = pd.DataFrame(data, columns=[
    "use_case",
    "region",
    "project_scale",
    "manpower_required",
    "drones_required",
    "expected_revenue",
    "operational_cost",
    "estimated_profit",
    "market_growth_percent"
])

df.to_csv("data/synthetic/business_scenarios.csv", index=False)

df.head()





#cost -benfit data
import pandas as pd
import random
import os

os.makedirs("data/synthetic", exist_ok=True)

data = [
    [
        manual := random.randint(300000, 1000000),
        drone := random.randint(100000, 500000),
        savings := manual - drone,
        round((savings / manual) * 100, 2)
    ]
    for _ in range(500)
]

df = pd.DataFrame(data, columns=[
    "manual_operation_cost",
    "drone_operation_cost",
    "cost_savings",
    "efficiency_improvement_percent"
])

df.to_csv("data/synthetic/cost_benefit_data.csv", index=False)

df.head()