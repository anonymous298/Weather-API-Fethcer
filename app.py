import streamlit as st
from weather import WeatherFetcher
from utils import set_page_config, apply_custom_css, display_weather_card

def main():
    # Set page configuration and apply custom CSS
    set_page_config()
    apply_custom_css()
    
    # Create header with spacing
    st.title("☁️ Weather Forecast App")
    st.markdown("#### Get real-time weather updates for any city!")
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Initialize weather fetcher
    weather_fetcher = WeatherFetcher()
    
    # Create container for better organization
    with st.container():
        # Create search input with better proportions
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            city = st.text_input("Enter City Name", value="London", 
                                placeholder="Type a city name...",
                                help="Enter the name of the city to get weather information")
            
            if st.button("Get Weather", type="primary"):
                if city:
                    try:
                        with st.spinner("Fetching weather data..."):
                            # Get weather data
                            data = weather_fetcher.fetch_json_from_response(city)
                            
                            if data:
                                weather = data['weather'][0]['description']
                                temperature = round(data['main']['temp'] - 273.15, 2)
                                wind = data['wind']['speed']
                                
                                # Add spacing before weather card
                                st.markdown("<br>", unsafe_allow_html=True)
                                
                                # Display weather information
                                display_weather_card(city, weather, temperature, wind)
                                
                                # Add spacing before additional metrics
                                st.markdown("<br>", unsafe_allow_html=True)
                                
                                # Create a container for metrics with custom styling
                                st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
                                
                                # Additional weather details
                                col1, col2, col3 = st.columns(3)
                                with col1:
                                    st.metric("Humidity", f"{data['main']['humidity']}%")
                                with col2:
                                    st.metric("Pressure", f"{data['main']['pressure']} hPa")
                                with col3:
                                    feels_like = round(data['main']['feels_like'] - 273.15, 2)
                                    st.metric("Feels Like", f"{feels_like}°C")
                                
                                st.markdown('</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"Unable to fetch weather data for {city}. Please check the city name and try again.")
                else:
                    st.warning("Please enter a city name!")
    
    # Footer with spacing
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p class="footer">Made with ❤️ using Streamlit and OpenWeatherMap API By Talha</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()