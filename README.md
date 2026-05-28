# Weather Dashboard

A terminal-based weather dashboard built with Python that fetches 
live weather data for any city worldwide.

## Features
- Current temperature in Celsius
- Feels like temperature
- Weather description
- Humidity, wind speed, and visibility
- Proper error handling for network and API errors
- Secure API key storage with .env

## Setup
1. Clone this repository
2. Install dependencies:
   pip install requests python-dotenv
3. Create a .env file in the project folder
4. Add your OpenWeatherMap API key:
   WEATHER_API_KEY=your_key_here
5. Get a free API key at openweathermap.org
6. Run:
   python weather_dashboard.py
