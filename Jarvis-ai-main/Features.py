import speedtest
from jmespath import search
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import smtplib
from requests import get, request
import sys
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from pywikihow import search_wikihow
from geopy.distance import great_circle # pip install geopy
from geopy.geocoders import Nominatim # pip install geopy
import webbrowser # pip install webbrowser
import geocoder # pip install geocoder
from keyboard import press, press_and_release
from utils import GoogleMap # Import shared utility function from utils
import webbrowser as web
from email.message import EmailMessage
import smtplib
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


import requests
import pycountry  # pip install pycountry

def My_Location():
    speak("Fetching your location...")

    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        city = data.get("city", "Chennai")  # Default to Chennai
        region = data.get("region", "Tamil Nadu")  # Default to Tamil Nadu
        country_code = data.get("country", "IN")  # Default to IN (India)

        # Convert country code (e.g., "IN") to full name ("India")
        country = pycountry.countries.get(alpha_2=country_code).name if pycountry.countries.get(alpha_2=country_code) else "India"

    except Exception as e:
        print(f"Location detection failed: {e}")
        city, region, country = "Chennai", "Tamil Nadu", "India"

    location = f"{city}, {region}, {country}"
    print(location)
    speak(f"Your current location is {location}")
    return location












import speech_recognition as sr

def listen():########################### new ############################
    """Captures user input through speech and returns it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            return query.lower()  # Return the recognized text in lowercase
        except sr.UnknownValueError:
            speak("Sorry, sir I couldn't understand you. Please repeat.")
            return ""
        except sr.WaitTimeoutError:
            speak("I didn't hear anything sir. Please try again.")
            return ""


    
def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    webbrowser.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)

    speak(target)
    speak(f'{Place} is {distance} kilometres away from you sir')


def Dateconverter(Query):

    Date = Query.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)
    
# def Temp():
#         search = "temperature in my current location"
#         url = f"https://www.google.com/search?q={search}"
#         r = requests.get(url)
#         data = BeautifulSoup(r.text,"html.parser")
#         temperature = data.find("div",class_ = "BNeawe").text
#         speak(f"The Temperature in your current location Is {temperature} sir")

        # speak("Do I Have To Tell You Another Place Temperature ?")
        # next = takeCommand()

        # if 'yes' in next:
        #     speak("Tell Me The Name Of tHE Place ")
        #     name = takeCommand()
        #     search = f"temperature in {name}"
        #     url = f"https://www.google.com/search?q={search}"
        #     r = requests.get(url)
        #     data = BeautifulSoup(r.text,"html.parser")
        #     temperature = data.find("div",class_ = "BNeawe").text
        #     speak(f"The Temperature in {name} is {temperature} celcius")

        # else:
        #     speak("no problem sir")


#******************************************* working *******************************************

import pyttsx3
import requests
import json

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech rate (lower value = slower speed)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to fetch news articles
def fetch_news(api_key, country="us"):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        return news_data.get("articles", [])
    else:
        speak("Sorry, I couldn't fetch the news. Please check your API key or internet connection.")
        return []

# Main function to read news
def read_news():
    # Replace with your News API key
    api_key = "e3069d485c0844dfa0f74935985f0d05"

    speak("Fetching the latest news for you.")
    articles = fetch_news(api_key)

    if not articles:
        speak("No news articles are available at the moment.")
        return

    for index, article in enumerate(articles[:5], start=1):
        title = article.get("title", "No title available")
        description = article.get("description", "No description available")

        speak(f"News {index}: {title}")
        if description:
            speak(f"Description: {description}")

        speak("Moving to the next news.")

    speak("That's all for now. Have a great day!")

if __name__ == "__main__":
    read_news()

#_________________________________ e mail ____________________________


EMAIL = " "
PASSWORD = " pass key"

def send_email(receiver_add,subject,message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From'] = EMAIL

        email.set_content(message)
        s= smtplib.SMTP("smtp.gmail.com",587)
        s.starttls
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


