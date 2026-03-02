import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# Process flight data
flight = pd.read_csv("data/synthetic/drone_flight_data.csv")
flight["battery_category"] = flight["battery_capacity_mAh"].apply(
    lambda x: "High" if x > 40000 else "Medium" if x > 20000 else "Low"
)
flight.to_csv("data/processed/processed_flight_data.csv", index=False)
# Process Business Scenario Data


business = pd.read_csv("data/synthetic/business_scenarios.csv")

# Add revenue scale category
business["revenue_scale"] = business["expected_revenue"].apply(
    lambda x: "Enterprise" if x > 3000000 
    else "Mid-Level" if x > 1500000 
    else "Startup"
)

# Add profitability margin %
business["profit_margin_percent"] = (
    business["estimated_profit"] / business["expected_revenue"] * 100
).round(2)

business.to_csv(
    "data/processed/processed_business_data.csv",
    index=False
)

print("Business data processed successfully!")
# Process cost data
cost = pd.read_csv("data/synthetic/cost_benefit_data.csv")
cost["profit_flag"] = cost["cost_savings"].apply(
    lambda x: "Profitable" if x > 0 else "Loss"
)
cost.to_csv("data/processed/processed_cost_data.csv", index=False)

print("Preprocessing completed successfully!")