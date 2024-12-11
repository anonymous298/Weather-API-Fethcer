import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Weather Forecast App",
        page_icon="🌤️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def apply_custom_css():
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stApp {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        .weather-card {
            background: linear-gradient(135deg, rgba(32, 32, 32, 0.9), rgba(45, 45, 45, 0.9));
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            margin: 20px auto;
            border: 1px solid rgba(255, 255, 255, 0.1);
            max-width: 1200px;
            width: 90%;
        }
        .weather-info {
            min-width: 180px;
            padding: 20px;
        }
        .weather-info p {
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .stTextInput > div > div {
            background-color: rgba(45, 45, 45, 0.9) !important;
            border-radius: 10px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            padding: 2px 10px;
            color: white !important;
        }
        .stTextInput > label {
            color: #ffffff !important;
        }
        .stButton > button {
            width: 100%;
            border-radius: 10px !important;
            background: linear-gradient(135deg, #00B4DB, #0083B0) !important;
            color: white !important;
            border: none !important;
            padding: 10px 20px !important;
            font-weight: bold !important;
        }
        div[data-testid="metric-container"] {
            background: rgba(45, 45, 45, 0.9);
            border-radius: 15px;
            padding: 20px !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
            min-width: 200px;
            margin: 10px;
        }
        div[data-testid="metric-container"] > div {
            color: #ffffff !important;
        }
        div[data-testid="stMarkdownContainer"] > h1 {
            color: #ffffff;
            text-align: center;
            padding: 20px 0;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        div[data-testid="stMarkdownContainer"] > h4 {
            color: #cccccc;
            text-align: center;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            padding: 20px;
            color: #888888;
        }
        .metrics-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def display_weather_card(city, weather, temperature, wind):
    weather_icons = {
        "clear sky": "☀️",
        "few clouds": "🌤️",
        "scattered clouds": "☁️",
        "broken clouds": "☁️",
        "shower rain": "🌧️",
        "rain": "🌧️",
        "thunderstorm": "⛈️",
        "snow": "🌨️",
        "mist": "🌫️"
    }
    
    icon = weather_icons.get(weather.lower(), "🌡️")
    
    st.markdown(f"""
        <div class="weather-card">
            <h2 style="text-align: center; margin-bottom: 30px; font-size: 2.2em; color: #ffffff;">
                {city.title()} {icon}
            </h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px; text-align: center;">
                <div class="weather-info">
                    <p style="font-size: 1.1em; color: #888888;">CONDITION</p>
                    <p style="font-size: 1.4em; margin: 10px 0; color: #ffffff;">{weather.title()}</p>
                </div>
                <div class="weather-info">
                    <p style="font-size: 1.1em; color: #888888;">TEMPERATURE</p>
                    <p style="font-size: 1.4em; margin: 10px 0; color: #ffffff;">{temperature}°C</p>
                </div>
                <div class="weather-info">
                    <p style="font-size: 1.1em; color: #888888;">WIND SPEED</p>
                    <p style="font-size: 1.4em; margin: 10px 0; color: #ffffff;">{wind} m/s</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
