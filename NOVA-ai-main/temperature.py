import speedtest
from jmespath import search
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from requests import get, request
import sys
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from pywikihow import search_wikihow
from geopy.distance import great_circle # pip install geopy
from geopy.geocoders import Nominatim # pip install geopy
import webbrowser # pip install webbrowser
from utils import GoogleMap # Import shared utility function from utils
import webbrowser as web
#from decouple import config

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                                           
        audio = r.listen(source,0,4)                                                                    

    try:                                                                    
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")

        return "None"
    return query

def get_weather_api(location="Chennai"):
    """Fetch comprehensive weather information using WeatherAPI.com."""
    try:
        speak(f"Fetching weather details for {location}.")
        print(f"Fetching weather details for: {location}")
        
        # It's better to store this in an environment variable or config file
        api_key = "1901c1f39cfc4480bbf152234251903"  # Replace with your actual API key
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=2&aqi=yes"
        
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            error_message = f"Error accessing weather API. Status code: {response.status_code}"
            print(error_message)
            speak("Sorry, I couldn't connect to the weather service.")
            return None
            
        data = response.json()
        
        # Check if the API returned an error
        if 'error' in data:
            error_message = f"API error: {data['error']['message']}"
            print(error_message)
            speak("Sorry, I couldn't find weather data for that location.")
            return None
        
        # Current weather information
        location_name = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        
        temperature_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        wind_dir = data["current"]["wind_dir"]
        
        # Air quality information
        air_quality = data["current"]["air_quality"]
        aqi = air_quality.get("us-epa-index", "Not available")
        aqi_text = ["Good", "Moderate", "Unhealthy for sensitive groups", "Unhealthy", 
                    "Very Unhealthy", "Hazardous"]
        aqi_description = aqi_text[aqi-1] if isinstance(aqi, int) and 1 <= aqi <= 6 else "Unknown"
        
        # Tomorrow's forecast
        tomorrow = data["forecast"]["forecastday"][1]["day"]
        tomorrow_max = tomorrow["maxtemp_c"]
        tomorrow_min = tomorrow["mintemp_c"]
        tomorrow_condition = tomorrow["condition"]["text"]
        tomorrow_chance_rain = tomorrow["daily_chance_of_rain"]
        
        # Format the result
        result = (
            f"Weather in {location_name}, {region}, {country}:\n"
            f"Local time: {local_time}\n"
            f"Temperature: {temperature_c}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind_kph} km/h, direction {wind_dir}\n"
            f"Air Quality Index: {aqi} - {aqi_description}\n\n"
            f"Tomorrow's forecast:\n"
            f"Temperature: {tomorrow_min}°C to {tomorrow_max}°C\n"
            f"Condition: {tomorrow_condition}\n"
            f"Chance of rain: {tomorrow_chance_rain}%"
        )
        print(result)
        
        # Create a shorter, more natural speaking version
        speak_text = (
            f"The current weather in {location_name} is {temperature_c} degrees Celsius with {condition}. "
            f"Humidity is {humidity} percent, wind speed is {wind_kph} kilometers per hour. "
            f"The air quality is {aqi_description}. "
            f"Tomorrow's forecast shows temperatures between {tomorrow_min} and {tomorrow_max} degrees with {tomorrow_condition}."
        )
        speak(speak_text)
        return result
        
    except requests.exceptions.ConnectionError:
        error_message = "Sorry, I couldn't connect to the weather service. Please check your internet connection."
        print(error_message)
        speak(error_message)
        return None
    except KeyError as e:
        error_message = f"Error processing weather data: Missing expected data field {e}"
        print(error_message)
        speak("Sorry, I couldn't process the weather information correctly.")
        return None
    except Exception as e:
        error_message = f"Sorry, I couldn't fetch the weather details. Error: {str(e)}"
        print(f"Error: {e}")
        speak("Sorry, I couldn't fetch the weather details. Please try again.")
        return None