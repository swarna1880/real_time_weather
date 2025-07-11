# 🌤️ Real-Time Weather App

A simple and interactive real-time weather dashboard built using **Python**, **Streamlit**, and the **OpenWeatherMap API**. The app allows users to view the current weather and 5-day forecast for any city in the world.

---

## 📌 Features

- 🔍 Search weather by city name
- 🌡️ Toggle between Celsius and Fahrenheit
- ☁️ View current temperature, humidity, weather condition
- 🌅 See sunrise and sunset time
- 📈 5-Day forecast displayed using line chart (3-hour intervals)
- 📦 Built with clean and modular Python code using `requests` and `matplotlib`
- 🌐 Runs locally via Streamlit UI

---

## 🚀 Live Demo

> Run locally on: `http://localhost:8501`

---

## 🛠️ Tech Stack

- **Python**
  
- **Streamlit** — for interactive UI
  
- **OpenWeatherMap API** — for weather data
  
- **Requests** — for API calls
  
- **Matplotlib** — for plotting forecast chart

---

## 📸 Screenshots

| Weather Search | Forecast Chart |

|----------------|----------------|

| ![weather](screenshots/search.png) | ![chart](screenshots/forecast.png) |

> (Add your own screenshots inside a `screenshots/` folder)

---

## 📄 How to Run

1. **Clone the repository**
   
   ```bash
   
   git clone https://github.com/your-username/real-time-weather-app.git
   
   cd real-time-weather-app
   
2. Install dependencies

   pip install -r requirements.txt

3. Set your API key

   Replace this in app.py:

   API_KEY = "your_actual_key"

4. Run the app

   streamlit run app.py

📂 Project Structure

real-time-weather-app/

│

├── app.py                # Main Streamlit app

├── requirements.txt      # List of Python dependencies

├── README.md             # Project documentation

└── screenshots/          # (Optional) Add your screenshots here

✨ Author

Swarna Ch

Python Intern | Elavate Labs
