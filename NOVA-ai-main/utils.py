# Shared utility functions like GoogleMap
def GoogleMap(location):
    import webbrowser
    url = f"https://www.google.com/maps/place/{location.strip().replace(' ', '+')}"
    webbrowser.open(url)

import requests
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Adjust speaking rate if needed
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen to the user's voice command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Please tell me the location for weather information.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")  # Print the user's input
        speak(f"You said {command}.")
        return command
    except sr.UnknownValueError:
        error_message = "Sorry, I didn't catch that. Please try again."
        print(error_message)
        speak(error_message)
        return ""
    except sr.RequestError:
        error_message = "There was an issue with the voice recognition service."
        print(error_message)
        speak(error_message)
        return ""

def get_detailed_weather(location):
    """Fetch weather information for the given location."""
    try:
        # Format the search query for Google
        search_query = f"weather in {location}"
        url = f"https://www.google.com/search?q={search_query}"

        # Set headers to mimic a browser visit
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Send an HTTP request to the Google search URL
        response = requests.get(url, headers=headers)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the weather information
        location_name = soup.find("div", class_="BNeawe tAd8D AP7Wnd")
        temperature = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
        details = soup.find_all("div", class_="BNeawe tAd8D AP7Wnd")

        # Check if the elements were found
        if not location_name or not temperature or len(details) < 2:
            raise ValueError("Could not extract weather details from the page.")

        # Process the data
        location_name = location_name.text
        temperature = temperature.text
        weather_condition = details[1].text.split("\n")[0]  # e.g., "Sunny"
        wind_and_humidity = details[1].text.split("\n")[1:]  # e.g., "Wind: 10 km/h"

        # Format the result
        result = (
            f"The weather in {location_name} is as follows:\n"
            f"Temperature: {temperature}.\n"
            f"Condition: {weather_condition}.\n"
            f"Details: {'; '.join(wind_and_humidity)}."
        )
        print(result)
        speak(result)

    except Exception as e:
        error_message = "Sorry, I couldn't fetch the weather details. Please try again."
        print(f"Error: {e}")
        speak(error_message)

# Main Function
if __name__ == "__main__":
    speak("Hello! I can tell you the weather. Please say the location.")
    location = listen_command()
    if location:
        print(f"Fetching weather details for: {location}")  # Confirm the location input
        get_detailed_weather(location)
    else:
        speak("I couldn't hear the location. Please try again.")


import requests
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr

def speak(text):
    """Speak the given text."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Capture voice command from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting. Please try again later.")
            return ""

