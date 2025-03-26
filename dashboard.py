import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="AI Traffic Management Dashboard", layout="wide")

# Custom CSS for Neon Theme
st.markdown("""
    <style>
        body { background-color: #111; color: #0ff; font-family: 'Orbitron', sans-serif; }
        .css-1d391kg { background-color: #222; }
        .stButton>button { background-color: #00ccff; color: #111; border-radius: 8px; padding: 10px; }
        .stButton>button:hover { background-color: #0ff; box-shadow: 0px 0px 15px #00ccff; }
        .stTextInput>div>div>input { background-color: #222; color: #0ff; }
        .stMarkdown { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; text-shadow: 0px 0px 10px #00ffff;'>🚦 AI Traffic Management System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Real-Time Traffic Monitoring & Analysis</h3>", unsafe_allow_html=True)

# Fetch Traffic Data from API
def get_traffic_data():
    query = '{ trafficStatus(location: "Highway 24") { location congestionLevel vehicleCount signalTime } }'
    response = requests.post("http://localhost:5000/graphql", json={"query": query})
    
    if response.status_code == 200:
        return response.json()["data"]["trafficStatus"]
    else:
        return None

# Display Traffic Data
traffic_data = get_traffic_data()

if traffic_data:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h4 style='text-align: center;'>🚗 Total Vehicles</h4>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #0ff;'>{traffic_data['vehicleCount']}</h2>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h4 style='text-align: center;'>🛣️ Congestion Level</h4>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #0ff;'>{traffic_data['congestionLevel']}</h2>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<h4 style='text-align: center;'>⏳ Signal Time Adjusted</h4>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #0ff;'>{traffic_data['signalTime']} sec</h2>", unsafe_allow_html=True)
    
    # Visualization - Vehicle Count Over Time
    vehicle_data = pd.DataFrame({
        "Time (Seconds)": [10, 20, 30, 40, 50],
        "Vehicle Count": [10, 25, traffic_data["vehicleCount"], 20, 15]
    })

    fig = px.line(vehicle_data, x="Time (Seconds)", y="Vehicle Count",
                  title="📊 Traffic Flow Over Time",
                  markers=True, line_shape='spline',
                  template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("⚠️ Unable to fetch traffic data. Please check your API connection.")

# Refresh Button
if st.button("🔄 Refresh Data"):
    st.experimental_rerun()
