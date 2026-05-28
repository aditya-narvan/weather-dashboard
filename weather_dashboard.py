from dotenv import load_dotenv
from pathlib import Path
import os
import requests

load_dotenv(dotenv_path=Path(__file__).parent / ".env")
api_key = os.getenv("WEATHER_API_KEY")
while True:
    a = input("Enter city: ").strip().title()
    try:
        weather =requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={a}&appid={api_key}", timeout=5)
        weather.raise_for_status()
        show = weather.json()        
    except requests.exceptions.ConnectionError:
        print("No internet Connection")
    except requests.exceptions.Timeout:
        print("Request timeout -- try again")
    except requests.exceptions.TooManyRedirects:
        print("Something went wrong on our end -- try again later")   # Too many redirects
        break
    except requests.exceptions.HTTPError as e:
        if "404" in str(e):
            print("City not found")
        elif "401" in str(e):
            print("Something went wrong on our end -- try again later") # Invalid API
            break
        elif "429" in str(e):
            print("Something went wrong on our end -- try again later") # Too may requests
            break
        else:
            print(f"Something went wrong on our end -- try again later")
            break
    except KeyError:
        print("Something went wrong on our end -- try again later") # Unexpected data format from API key
        break
    except ValueError:
        print("Something went wrong on our end -- try again later") # Invalid response from server
        break
    else:        
        country = show['sys']['country']
        temp = round(show['main']['temp'] - 273.15, 0)
        feels_like = round(show['main']['feels_like'] - 273.15, 0)
        description = show['weather'][0]['description']
        humidity = round(show['main']['humidity'], 0)
        wind_speed = round(show['wind']['speed'], 0)
        visibility = show['visibility']        
        print(f"\n📍{a},{country}")
        print("-" * 40)
        print("|", int(temp),"°C", " " * 12,description)
        print("|"," " * 18, "Feels like", int(feels_like),"°C","\n|")
        print("-" * 40)
        print(f"ᰓ Humidity  |  ༄ Wind  |  𓁹 Visibility")
        if visibility >= 1000:
            visibility /= 1000
            print(f"    {int(humidity)}%     |    {int(wind_speed)}m/s  |      {int(visibility)}km")
        else:
            print(f"    {int(humidity)}%     |    {int(wind_speed)}m/s  |      {int(visibility)}m")
    agn = input("\nDo you want to try again: (yes/no) ").strip().lower()
    if agn == "yes":
        continue
    else:
        print("\nThanks for using")
        break