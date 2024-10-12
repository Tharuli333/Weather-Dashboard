import streamlit as st
import requests 
import pandas as pd
st.title('THARULIS WEATHER DASHBOARD')
st.sidebar.header("Input Location")
latitude = st.sidebar.text_input("Latitude", "37.7749")
longitude = st.sidebar.text_input("Longitude", "-122.4194")
if st.sidebar.button("Get Weather Data"):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["hourly"]["temperature_2m"]
        time_series = range(len(temperature))
        
        # Convert to DataFrame for better visualization
        df = pd.DataFrame({"Time": time_series, "Temperature": temperature})
        
        st.write("Hourly Temperature Data:")
        st.line_chart(df.set_index("Time"))  # Plot temperature as a line chart
    else:
        st.error("Failed to retrieve data. Please check your inputs.")
st.subheader('Asia/Colombo')
st.image('colombo.jpeg')
st.video('https://youtu.be/u3M9-jHfWGE?si=hF85ZVc1-99CF-QF')
option = st.sidebar.selectbox(
    "What do you need to know?",
    ("Temperature min", "Temperature max", "Sunrise", "Sunset", "Precipitation"),
)