import streamlit as st
import requests
from datetime import datetime
import matplotlib.pyplot as plt

# ✅ Your working API key
API_KEY = "499452c5ea41dbc66b60877e0034858b"

# Format sunrise/sunset time
def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M')

# Fetch weather data from OpenWeatherMap
def get_weather_data(city, units="metric"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"cod": "error", "message": "Invalid JSON response"}

# Streamlit app setup
st.set_page_config(page_title="Real-Time Weather App", page_icon="⛅")
st.title("🌤️ Real-Time Weather App")

# User input
city = st.text_input("Enter City Name:", "Hyderabad")
unit = st.radio("Select Temperature Unit", ["Celsius", "Fahrenheit"])
units = "metric" if unit == "Celsius" else "imperial"

# Get weather data on button click
if st.button("Get Weather"):
    data = get_weather_data(city, units)

    if data.get("cod") != "200":
        st.error(f"Error: {data.get('message', 'Unknown error')}")
    else:
        # Current weather
        current = data['list'][0]
        st.subheader(f"📍 {data['city']['name']}, {data['city']['country']}")
        st.write(f"**Temperature:** {current['main']['temp']}°{unit[0]}")
        st.write(f"**Weather:** {current['weather'][0]['description'].title()}")
        st.write(f"**Humidity:** {current['main']['humidity']}%")
        st.write(f"**Sunrise:** {format_time(data['city']['sunrise'])}")
        st.write(f"**Sunset:** {format_time(data['city']['sunset'])}")

        # 5-day forecast chart
        st.subheader("📈 5-Day Forecast (Every 3 Hours)")
        temps = [entry['main']['temp'] for entry in data['list']]
        times = [entry['dt_txt'] for entry in data['list']]

        plt.figure(figsize=(10, 4))
        plt.plot(times, temps, marker='o', linestyle='-', color='tab:blue')
        plt.xticks(rotation=45)
        plt.xlabel("Date-Time")
        plt.ylabel(f"Temp (°{unit[0]})")
        plt.title(f"Temperature Forecast for {city}")
        plt.tight_layout()
        st.pyplot(plt)
