import streamlit as st
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Drone Intelligence System", layout="wide")
st.title("🚁 Drone Intelligence System Dashboard")

# ==============================
# Sidebar
# ==============================
tool = st.sidebar.selectbox(
    "Select Tool",
    [
        "Chat with AI",
        "Flight Time",
        "ROI",
        "Compliance",
        "Drone Selection",
        "Upload",
        "Analytics"
    ]
)

# =====================================================
# 1️⃣ CHAT WITH AI
# =====================================================
if tool == "Chat with AI":

    st.header("💬 Chat with AI Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask something about drones:")

    if st.button("Send"):
        payload = {"query": user_input}

        response = requests.post(
            f"{API_BASE_URL}/chat",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("AI", result["response"]))
        else:
            st.error(response.text)

    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")


# =====================================================
# 2️⃣ FLIGHT TIME
# =====================================================
elif tool == "Flight Time":

    st.header("✈ Flight Time Calculator")

    battery_capacity = st.number_input("Battery Capacity (mAh)", value=50000.0)

    drone_type = st.selectbox(
        "Drone Type",
        ["Nano", "Micro", "Small", "Medium", "Large"]
    )

    drone_weight_map = {
        "Nano": 0.25,
        "Micro": 2,
        "Small": 10,
        "Medium": 25,
        "Large": 50
    }

    drone_weight = drone_weight_map[drone_type]

    payload_weight = st.number_input("Payload Weight (kg)", value=2.0)

    weather = st.selectbox(
        "Weather Condition",
        ["Normal", "Summer", "Rainy", "Windy", "Stormy"]
    )

    st.info(f"Selected Drone Weight: {drone_weight} kg")

    if st.button("Calculate Flight Time"):

        payload = {
            "battery_capacity": battery_capacity,
            "drone_weight": drone_weight,
            "payload_weight": payload_weight,
            "weather": weather
        }

        response = requests.post(
            f"{API_BASE_URL}/calculate/flight-time",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success("Flight Time Calculated Successfully")
            st.write("Drone Category:", result["drone_category"])
            st.write("Estimated Time (minutes):", result["estimated_time"])
        else:
            st.error(response.text)


# =====================================================
# 3️⃣ ROI
# =====================================================
elif tool == "ROI":

    st.header("💰 ROI Calculator")

    use_case = st.selectbox(
        "Use Case",
        ["Agriculture", "Medical", "Defense", "Disaster", "Mining Survey"]
    )

    initial_investment = st.number_input("Initial Investment", value=5000000.0)
    operational_cost = st.number_input("Operational Cost", value=45000.0)
    yearly_revenue = st.number_input("Yearly Revenue", value=670000.0)

    if st.button("Calculate ROI"):

        payload = {
            "use_case": use_case,
            "initial_investment": initial_investment,
            "operational_cost": operational_cost,
            "yearly_revenue": yearly_revenue
        }

        response = requests.post(
            f"{API_BASE_URL}/calculate/roi",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success("ROI Calculated Successfully")
            st.write("ROI Percentage:", result["roi_percentage"], "%")
            st.write("Net Profit:", result["net_profit"])
            st.write("Break Even Years:", result["break_even_years"])
        else:
            st.error(response.text)


# =====================================================
# 4️⃣ COMPLIANCE
# =====================================================
elif tool == "Compliance":

    st.header("📋 Compliance Checker")

    battery_capacity = st.number_input("Battery Capacity (mAh)", value=50000.0)
    payload_weight = st.number_input("Payload Weight (kg)", value=5.0)
    max_altitude = st.number_input("Max Altitude (m)", value=120.0)

    intended_use = st.selectbox(
        "Intended Use",
        ["Agriculture", "Medical", "Defense", "Disaster", "Mining Survey"]
    )

    location = st.text_input("Location", "Hyderabad")

    if st.button("Check Compliance"):

        payload = {
            "specifications": {
                "battery_capacity": battery_capacity,
                "payload_weight": payload_weight,
                "max_altitude": max_altitude
            },
            "intended_use": intended_use,
            "location": location
        }

        response = requests.post(
            f"{API_BASE_URL}/calculate/compliance",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success("Compliance Checked")
            st.write("Status:", result["status"])

            st.write("Required Permits:")
            for permit in result["required_permits"]:
                st.write("-", permit)
        else:
            st.error(response.text)


# =====================================================
# 5️⃣ DRONE SELECTION
# =====================================================
elif tool == "Drone Selection":

    st.header("🤖 Drone Selection Assistant")

    use_case = st.selectbox(
        "Use Case",
        ["Agriculture", "Medical", "Defense", "Disaster", "Mining Survey"]
    )

    budget = st.number_input("Budget", value=100000.0)
    min_flight_time = st.number_input("Minimum Flight Time (minutes)", value=30.0)
    min_payload = st.number_input("Minimum Payload Capacity (kg)", value=5.0)

    high_res_camera = st.checkbox("High Resolution Camera Required")
    thermal_camera = st.checkbox("Thermal Camera Required")

    if st.button("Find Best Drone"):

        payload = {
            "use_case": use_case,
            "budget": budget,
            "technical_requirements": {
                "min_flight_time": min_flight_time,
                "min_payload": min_payload,
                "high_res_camera": high_res_camera,
                "thermal_camera": thermal_camera
            }
        }

        response = requests.post(
            f"{API_BASE_URL}/calculate/drone",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            drone = result["recommendation"]

            st.success("Drone Recommended")
            st.write("Model:", drone["model"])
            st.write("Flight Time:", drone["flight_time"])
            st.write("Payload:", drone["payload"])
            st.write("Camera:", drone["camera"])
        else:
            st.error(response.text)


# =====================================================
# 6️⃣ UPLOAD
# =====================================================
elif tool == "Upload":

    st.header("📂 Upload Drone Data File")

    uploaded_file = st.file_uploader(
        "Upload CSV or JSON file",
        type=["csv", "json"]
    )

    if uploaded_file is not None:

        files = {"file": uploaded_file}

        response = requests.post(
            f"{API_BASE_URL}/upload",
            files=files
        )

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error(response.text)


# =====================================================
# 7️⃣ ANALYTICS
# =====================================================
elif tool == "Analytics":

    st.header("📊 System Analytics")

    response = requests.get(f"{API_BASE_URL}/analytics")

    if response.status_code == 200:
        result = response.json()

        st.metric("Total Requests", result.get("total_requests", 0))
        st.metric("Chat Queries", result.get("chat_queries", 0))
        st.metric("Most Used Tool", result.get("most_used_tool", "N/A"))
    else:
        st.error("Analytics endpoint not available")