# from sqlite3 import Date
# import pyttsx3  # pip install pyttsx3
# import speech_recognition as sr  # pip install speechRecognition
# import datetime
# import wikipedia  # pip install wikipedia
# import webbrowser
# import pywhatkit
# import pyjokes
# import os
# from requests import get
# import sys
# import requests
# from bs4 import BeautifulSoup
# from playsound import playsound
# from pywikihow import search_wikihow
# from keyboard import press, press_and_release
# from sympy import sympify, SympifyError
# from jarvisUi import Ui_jarvisUi
# from YT import YouTubeAuto
# import wikipediaapi
# from WindowsAuto import WindowsAuto
# from internet_speed_test import check_internet_speed
# from Features import My_Location
# from Features import GoogleMaps
# from Features import listen
# from Features import Temp
# #from app_handler import open_app
# #from on_off import speak, listen_command, control_wifi, control_bluetooth, adjust_brightness, adjust_volume
# from on_off import process_command
# import pyautogui
# from app_handler import open_application,close_application,type_in_app,save_file,send_message
# from game import games
# from utils import get_weather
# from Features import read_news
# from Nasa import latest_space_news
# from scrool_system import perform_scroll_action,scroll_up,scroll_down,scroll_to_top,scroll_to_bottom
# from scrool_system import perform_browser_action
# from Web_Open import open_website            # new
# import threading    # new      
# import psutil           # new
# import imdb
# from Features import send_email
# import sys
# # from PyQt6.QtWidgets import (
# #     QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog,
# #     QScrollArea, QFrame
# # )
# # from PyQt6.QtGui import QPixmap, QMovie, QFont
# # from PyQt6.QtCore import Qt, QTimer
# from desktop_1 import InfoDialog,JarvisGUI
# from PyQt6.QtWidgets import QApplication
# import subprocess
# from PyQt6 import QtWidgets, QtCore, QtGui
# from PyQt6.QtCore import QThread


# # Initialize pyttsx3 engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 175)
# engine.setProperty('voice', engine.getProperty('voices')[0].id)

# def speak(text):
#     """Speak the given text."""
#     engine.say(text)
#     engine.runAndWait()

# def listen_command():
#     """Listen for a voice command from the user."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening for command...")
#         speak("Listening for command.")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
    
#     try:
#         command = recognizer.recognize_google(audio,language='en-in').lower()
#         print(f"You said: {command}\n")
#         return command
#     except sr.UnknownValueError:
#         speak("Sorry, I couldn't understand that.")
#         return ""
#     except sr.RequestError:
#         speak("Sorry, there was an issue with the speech recognition service.")
#         return ""
# command=listen_command().lower


#                 #////////////////////////////// new ///////////////////////////////////
                
# # Sleep and Wake-up functions
# active = True                                                   

# def sleep_mode():                                                    # working
#     global active
#     active = False
#     speak("I am going to sleep mode. Say 'Wake up nova' to reactivate me.")

# def wake_up_mode():                                            # working
#     global active
#     active = True
#     speak("I am back and ready to assist you.")

# def weather_command():                                              #new        # not working
#     """Handle the weather command."""
#     speak("Please tell me the location for weather information.")
#     location = listen_command()
#     if location:
#         get_weather(location)
#     else:
#         speak("I couldn't hear the location. Please try again.")


# def battery_percentage_query():
#     """Responds with the current battery percentage."""
#     battery = psutil.sensors_battery()
#     if battery:
#         percent = battery.percent
#         speak(f"The battery is at {percent}% charge.")
#     else:
#         speak("Battery information is not available.")



# def list_running_apps():
#     """List all running applications."""
#     speak("Checking running applications.")
#     running_apps = []
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             app_name = proc.info['name']
#             if app_name:
#                 running_apps.append(app_name)
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             continue

#     if running_apps:
#         speak(f"I found {len(running_apps)} running applications.")
#         for app in running_apps[:10]:  # Limit output to 10 apps
#             speak(app)
#     else:
#         speak("No running applications found.")


# def handle_how_are_you():
#     """Respond to 'How are you' query and process the user's response."""
#     speak("I am absolutely fine, sir. What about you?")
#     user_response = listen_command()  # Get the user's response
    
#     if 'good' in user_response or 'i am fine' in user_response or 'fine' in user_response:
#         speak("I'm glad to hear that!")
#     else:
#         speak("Sorry to hear that. Soon, it will get better!")
        

#            #////////////////////////////// new over ///////////////////////////////////

    

# # Initialize pyttsx3 engine for voice
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 175)


# # Speak function
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# # Startup
# def startup():                                                   # working  
#     # speak("Initializing the cloud...")
#     # speak("Starting all systems applications")
#     # speak("Installing and checking all drivers")
#     # speak("Caliberating and examining all the core processors")
#     # speak("Checking the internet connection")
#     # speak("Wait a moment sir")
#     # speak('Updating the cloud configuration')
#     # speak("All drivers are up and running")
#     speak("All systems have been activated.")


# # Wish the user
# def wishMe():                                            # working
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         print("Good morning sir!")
#         speak("Good morning sir!")
#     elif hour >= 12 and hour < 17:
#         print("Good afternoon sir!")
#         speak("Good afternoon sir!")
#     elif hour >= 12 and hour < 17:
#         print("Good evening sir!")
#         speak("Good evening sir!")
#     else:
#         print("Good night sir!")
#         speak("Good night sir!")
#     speak("Please tell me how may I help you.")

#    # WIKIPEDIA FUNCTION

# def tell_me_about(self):                                # working
#     try:
#         # Removing the trigger phrase
#         speak('Searching Wikipedia...please wait')
#         self.query = self.query.replace("tell me about", "").strip()
#         print(f"Query: {self.query}")

#         # Searching for the topic
#         results = wikipedia.summary(self.query, sentences=2)
        
#         # Speaking the result
#         speak("According to wikipedia...")
#         print(results)
#         speak(results)

#     except wikipedia.DisambiguationError as e:
#         # Handle multiple results found for the query
#         speak("There are multiple topics matching your query. Please be more specific.")
#         print(f"DisambiguationError: {e.options}")

#     except wikipedia.PageError:
#         # Handle the case where no results are found
#         speak("Sorry, I could not find any information on Wikipedia for that topic.")
#         print("PageError: No results found for the query.")

#     except Exception as e:
#         # Catch all other exceptions
#         speak("Sorry, an error occurred while searching Wikipedia.")
#         print(f"Error: {e}")




# # Main Task Execution Class
# class MainThread(QtCore.QThread):
    
#     def __init__(self):
#         super(MainThread, self).__init__()

#     def run(self):
#         self.TaskExecution()

#     def takeCommand(self):
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Listening...")
#             r.pause_threshold = 1
#             audio = r.listen(source, 0, 4)

#         try:
#             print("Recognizing...")
#             self.query = r.recognize_google(audio, language='en-in')
#             print(f"User said: {self.query}\n")
#         except Exception as e:
#             print("Say that again please...")

#             return "None"
#         return self.query


#     def TaskExecution(self):
#         startup()
#         wishMe()
#         while True:
#             if not active:  # Check if NOVA is in sleep mode                      # working
#                 self.query = self.takeCommand().lower()
#                 if 'wake up' in self.query or 'wakeup' in self.query or 'activate wake up mode' in self.query:
#                     wake_up_mode()
#                 continue

#             self.query = self.takeCommand().lower()

       
#             if 'tell me about' in self.query:           # working
#                 tell_me_about(self)

#         # new__________************************************************************************

#             elif 'open' in self.query:
#                 if 'instagram' in self.query:
#                     open_application('Instagram')
#                 elif 'youtube' in self.query:
#                     open_application('YouTube')
#                 elif 'facebook' in self.query:
#                     open_application('Facebook')
#                 else:
#                     app_name = self.query.replace('open ', '').strip()
#                     open_application(command)

#             elif 'close' in self.query:
#                 if 'instagram' in self.query:
#                     close_application('Instagram')
#                 elif 'youtube' in self.query:
#                     close_application('YouTube')
#                 elif 'facebook' in self.query:
#                     close_application('Facebook')
#                 else:
#                     app_name = self.query.replace('close ', '').strip()
#                     close_application(app_name)

#             elif 'type' in self.query or 'start typing' in self.query:
#                 speak("Please tell me what should I type. Say 'exit typing' to stop.")
#                 while True:
#                     text_to_type = listen_command()
#                     if 'exit typing' in text_to_type or 'stop typing' in text_to_type:
#                         speak("Exiting typing mode.")
#                         break
#                     elif text_to_type:
#                         type_in_app(text_to_type)
#                     else:
#                         speak("I didn't catch that. Please try again.")

#             elif 'save file' in self.query or 'save this file' in self.query:
#                 speak("Saving the current file.")
#                 save_file()

#             elif 'send message' in self.query or 'send a message' in self.query:
#                 speak("Who should I send the message to?")
#                 recipient = listen_command()
#                 speak("What is the message?")
#                 message = listen_command()
#                 if recipient and message:
#                     send_message(recipient, message)
#                 else:
#                     speak("I couldn't get the recipient or message. Please try again.")



        

#         # new over____________************************************************************************


#             elif "calculate" in self.query or "what is" in self.query or "multiply" in self.query or "times" in self.query:         # working
#                 try:
#                     question = self.query.replace("calculate", "").replace("what is", "").replace("multiply", "").replace("times", "").strip()
#                     expression = sympify(question)
#                     result = expression.evalf()

#                     if float(result).is_integer():
#                         answer = int(result)
#                     else:
#                         answer = round(float(result), 6)
#                     print(f"The answer is {answer}")
#                     speak(f"The answer is {answer}")
#                 except SympifyError:
#                     speak("I couldn't understand the mathematical expression. Please try again.")
#                 except Exception as e:
#                     speak("An error occurred while performing the calculation. Please try again.")

#             elif 'play' in self.query:                          # working
#                 speak('Surfing the browser.... Hold on sir')
#                 self.query = self.query.replace('play', '')
#                 speak('Playing' + self.query)
#                 speak('Enjoy the music')
#                 pywhatkit.playonyt(self.query)

#             elif any(keyword in self.query for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
#                                                            'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
#                                                             'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
#                                                            'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
#                 command = self.query
#                 YouTubeAuto(command)
#                 #speak(f"Performing the {command} action.")

#             elif 'joke' in self.query:              # working
#                 speak(pyjokes.get_joke())

#             elif 'ip address' in self.query:                    # working
#                 ip = get("https://api.ipify.org").text
#                 speak(f'Your current IP address is {ip}')

#             elif 'time' in self.query or 'date' in self.query:          # working
#                 now = datetime.datetime.now()
#                 if 'time' in self.query:
#                     current_time = now.strftime("%I:%M %p")
#                     speak(f"The current time is {current_time}")
#                 if 'date' in self.query:
#                     current_date = now.strftime("%A, %B %d, %Y")
#                     speak(f"Today's date is {current_date}")


#             elif 'where is' in self.query.lower():                                              # working
#                 Place = self.query.lower().replace('where is', '').replace('cortana', '').strip()
#                 if not Place:
#                     speak("I couldn't understand the location. Please try again.")
#                 else:
#                     speak(f"Searching for {Place} on Google Maps.")
#                     # Open Google Maps with the specific query
#                     import webbrowser
#                     webbrowser.open(f"https://www.google.com/maps/search/{Place}")

       
#             elif 'current temperature' in self.query:                       # working
#                 search = "temperature in my current location"
#                 url = f"https://www.google.com/search?q={search}"
#                 r = requests.get(url)
#                 data = BeautifulSoup(r.text, "html.parser")
#                 temp = data.find("div", class_="BNeawe").text
#                 speak(f'The current temperature in your location is {temp}')


#             elif 'windows' in self.query or any(keyword in self.query for keyword in ['home screen', 'minimize', 'minimise', 'maximise', 'maximize','close the window','close the application',
#                                                                                       'show start', 'open setting','open search', 'screen shot', 'shutdown' , 'restart', 'log out','system sleep'
#                                                                                        'take a screenshot' , 'restore windows','start recording', 'screenshot', 'stop recording']):
#                 WindowsAuto(self.query)


#                 # adding new features

#             elif "internet speed" in self.query:    #working
#                 check_internet_speed()

#             elif 'my location' in self.query:       #working
#                 My_Location() 


#             elif 'show location' in self.query or 'find location' in self.query:        #working    
#                 try:
#                     # Ask the user for the place name using speech
#                     speak("Please tell me the name of the place.")
#                     place = listen() # Use the listen function for speech-based input
        
#                     if place:
#                         speak(f"Searching for {place} on Google Maps.")
#                         GoogleMaps(place)  # Call the GoogleMaps function with the place name
#                     else:
#                         speak("I couldn't hear the place name. Please try again.")
#                 except Exception as e:
#                         print(f"Error occurred: {e}")
#                         speak("Sorry, I couldn't fetch the location. Please try again.")

#             elif 'open app' in self.query:
#                 speak("Which app would you like me to open?")
#                 app_name = listen_command()  # Capture app name from user
#                 open_application(app_name)

#             # elif  'open app' in self.query:
#             #     speak("Which app would you like me to open?")
#             #     app_name = listen_command()  # Capture app name from user
#             #     call_function(app_name)


#             elif "hello" in self.query or "hey" in self.query:                          # working
#                 speak('Hello sir , Good to see you')
#                 speak('How may i help You?')

    
#             elif any(keyword in self.query for keyword in ['turn on bluetooth','turn off bluetooth','bluetooth','increase brigntness', 'decrease brigntness',
#                                                              'night light', 'increase volume', 'decrease volume', 'turn on night light','turn on aeroplance mode','turn off aeroplance mode',
#                                                            'turn on night light', 'mute system volume','brightness','no sound','sound','check volume level','check current volume level',
#                                                             'unmute system volume','maximum volume','set volume to','check brightness level','set brightness to']):
#                 process_command(self.query)             # working



#             elif 'type' in self.query or 'start typing' in self.query or 'starttyping' in self.query or 'start type' in self.query:
#                 speak("please tell me what should i write")
#                 while True:
#                     writeInNotepad=command()
#                     if writeInNotepad=='exit typing':
#                         speak("Done sir")
#                     else:
#                         pyautogui.write(writeInNotepad)
        

#             elif "what can you do for me" in self.query:    # working
#                 speak('Yes sir,Nice Question')
#                 speak('As per my program,I\'m a virtual assiatant which can perform tasks through your voice cammand')
            
#             elif "cool" in self.query or "nice" in self.query or "awsome" in self.query or "thank you" in self.query:   # working
#                 speak("Yes sir,That's my pleasure!")

#                         #     FOR APPP FUNCTIONS

#             # elif 'open app' in command or 'open application' in command:
#             #     open_application(command)

#             # elif 'type' in command or 'type what i am saying' in command:
#             #     type_in_app(command)


#             # elif 'save' in command or 'save file' in command:
#             #     save_file(command)

#             # elif 'message' in command or 'send a message' in command:
#             #     send_message(command)


#             elif "game" in self.query:      # new       # working ____ need to improve____
#                 from game import games
#                 games()
                
#             elif 'search' in self.query:                # new   # working
#                 import wikipedia as googleScrap
#                 self.query = self.query.replace('jarvis', '   ')
#                 self.query = self.query.replace('google search', '    ')
#                 self.query = self.query.replace('google','    ')
            
#                 speak('Here are some results...')

#                 try:
#                     pywhatkit.search(self.query)
#                     result = googleScrap.summary(self.query,3)
#                     speak(result)

#                 except:
#                     speak(' Data not cached..')

#             elif 'sleep mode' in self.query or 'sleep nova' in self.query or 'activate sleep mode' in self.query:    #new    # working
#                 sleep_mode()

#             elif 'wake up' in self.query or 'wakeup' in self.query or 'activate wake up mode' in self.query:    #new    # working
#                 sleep_mode()

#             elif "weather" in self.query or 'climate' in self.query:                #new      # not working
#                 weather_command()


#             elif 'screenshot' in self.query or 'screen shot' in self.query:               # working
#                 try:
#                     import pyautogui
#                     screenshot = pyautogui.screenshot()
#                     screenshot.save("screenshot.jpg")  # Save screenshot as "screenshot.jpg" in the current directory
#                     speak("Screenshot taken and saved as 'screenshot.jpg' in the current directory.")
#                 except Exception as e:
#                     speak(f"Failed to take a screenshot: {e}")


#             elif 'read news' in self.query or 'current news' in self.query or 'news mode' in self.query:    #new    # working
#                 read_news()

#             elif 'space news' in self.query or 'nasa news' in self.query or 'astrological news' in self.query:    #new    # working
#                 latest_space_news()


#             elif 'scroll up' in self.query or 'scroll down' in self.query or 'scroll to top' in self.query or 'scroll to bottom' in self.query:
#                 perform_scroll_action(self.query)                                            # new   # working



#             elif any(keyword in self.query for keyword in ['add new tab','close tab','zoom in','zoom out', 'refresh page','go to history', 'go to bookmarks',
#                                                              'switch to next tab', 'switch to previous tab', 'open history', 'open bookmarks',
#                                                            'go back', 'go forward','open dev tools','toggle full screen','open private window'
#                                                            'go to dev tools','go to private window','next tab','previous tab']):
                                                           
#                 perform_browser_action(self.query)          # new   # working


#             elif 'get to website' in self.query or 'go to website' in self.query:                # new   # working
#                 # Extract the website name from the query
#                 website_name = self.query.lower().replace("get to website", "").replace("go to website", "").strip()
#                 # Call the function to open the website
#                 open_website(website_name)
        

#             elif "battery status" in self.query or "battery percentage" in self.query:          # new   # working
#                 battery_percentage_query()  

#             elif "running apps" in self.query or "list running apps" in self.query:     # new   # working
#                 list_running_apps()

#             elif 'how are you' in self.query:       # new   # working
#                 handle_how_are_you()                    
#                 #speak("i am absolutely fine sir. what about you")

#             elif 'movie' in self.query:                         # new   # working
#                 movies_db = imdb.IMDb()
#                 speak("tell me the movie name:")
#                 text = listen_command()
#                 movies = movies_db.search_movie(text)
#                 speak("searching for" + text)
#                 speak("i found this")
#                 for movie in movies:
#                     title = movie["title"]
#                     year = movie["year"]
#                     speak(f"{title}-{year}")
#                     info = movie.getID()
#                     movie_info = movies_db.get_movie(info)
#                     rating = movie_info["rating"]
#                     cast = movie_info["cast"]
#                     actor = cast[0:5]
#                     plot = movie_info.get('plot outline','plot summary not available')
#                     #speak(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {actor}.the plot summary of movie is {plot}")
#                     speak(f"{title} was released in {year} has imdb ratings of {rating}.the plot summary of movie is {plot}")
#                     print(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {actor}.the plot summary of movie is {plot}")


#             elif 'how developed you' in self.query or 'who created you' in self.query or 'who is your master' in self.query:    # working
#                 speak("thiyagu")                   # new   # working

#             elif "what are you" in self.query:          # new   # working
#                 speak('Hello sir, I am your personalized voice assistant, also known as Jarvis.')

#             elif "what are the task's you can perform" in self.query:    # working
#                 speak('google search ,play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi  speed, provide you news from NASA, calculate, search the map, wikipedia search , and many more')


#             elif 'send an email' in self.query or 'send a mail' in self.query:
#                 speak("on what email address do you want to send sir?.please enter in terminal")
#                 receiver_add = input("Email address:")
#                 speak("what should be the subject sir?")
#                 subject = command().capitalize()
#                 speak("what is the message ?")
#                 message = command().capitalize()
#                 if send_email(receiver_add,subject,message):
#                     speak(" I have sent the email sir")
#                     print(" I have sent the email sir")
#                 else:
#                     speak("something went wrong sir")



#             elif 'shutup' in self.query or 'exit program' in self.query or 'exit' in self.query:    # working
#                 speak("Shutting down. Goodbye, sir.")
#                 sys.exit()


# # Main Class for GUI
# class JarvisApp:
#     def __init__(self):
#         self.core = MainThread()

#     def run_gui(self):
#         """Launches desktop_1 GUI and starts other processes."""
#         app = QApplication(sys.argv)
#         window = JarvisGUI()
#         window.show()
        
#         # Start desktop_2 and Jarvis core before entering the event loop
#         self.open_desktop_2()
#         self.start_jarvis()
        
#         sys.exit(app.exec())  # Use sys.exit to ensure proper cleanup

#     def open_desktop_2(self):
#         """Opens desktop_2.py"""
#         try:
#             subprocess.Popen(["python", "desktop_2.py"])
#             print("Successfully launched desktop_2.py")
#         except Exception as e:
#             print(f"Error launching desktop_2.py: {e}")

#     def start_jarvis(self):
#         """Start Jarvis AI core functions"""
#         try:
#             # Use QThread's built-in start method
#             self.core.start()
#             print("Successfully started Jarvis core thread")
#         except Exception as e:
#             print(f"Error starting Jarvis core: {e}")

# if __name__ == "__main__":
#     try:
#         app = JarvisApp()
#         app.run_gui()
#     except Exception as e:
#         print(f"Error in main execution: {e}")
#         sys.exit(1)

from sqlite3 import Date
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
from requests import get
import sys
import requests
from bs4 import BeautifulSoup
import subprocess
import time
import threading
import psutil
import imdb
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
from sympy import sympify, SympifyError

# Import all the required modules and features
from YT import YouTubeAuto
from WindowsAuto import WindowsAuto
from internet_speed_test import check_internet_speed
from Features import My_Location, GoogleMaps, listen, Temp, read_news, send_email
from on_off import process_command
from app_handler import open_application, close_application, type_in_app, save_file, send_message
from game import games
from utils import get_weather
from Nasa import latest_space_news
from scrool_system import perform_scroll_action, scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
from scrool_system import perform_browser_action
from Web_Open import open_website
from desktop_1 import InfoDialog, JarvisGUI

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

# Global active state
active = True

def speak(audio):
    """Speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def listen_command():
    """Listen for a voice command from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=4)
    
    try:
        command = recognizer.recognize_google(audio, language='en-in').lower()
        print(f"You said: {command}\n")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
        return ""

# Sleep and Wake-up functions
def sleep_mode():
    global active
    active = False
    speak("I am going to sleep mode. Say 'Wake up nova' to reactivate me.")

def wake_up_mode():
    global active
    active = True
    speak("I am back and ready to assist you.")

# Startup message
def startup():
    speak("All systems have been activated.")

# Greet the user based on time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning sir!")
        speak("Good morning sir!")
    elif hour >= 12 and hour < 17:
        print("Good afternoon sir!")
        speak("Good afternoon sir!")
    elif hour >= 17 and hour < 21:
        print("Good evening sir!")
        speak("Good evening sir!")
    else:
        print("Good night sir!")
        speak("Good night sir!")
    speak("Please tell me how may I help you.")

# Wikipedia search function
def tell_me_about(query):
    try:
        # Removing the trigger phrase
        speak('Searching Wikipedia...please wait')
        query = query.replace("tell me about", "").strip()
        print(f"Query: {query}")

        # Searching for the topic
        results = wikipedia.summary(query, sentences=2)
        
        # Speaking the result
        speak("According to wikipedia...")
        print(results)
        speak(results)

    except wikipedia.DisambiguationError as e:
        # Handle multiple results found for the query
        speak("There are multiple topics matching your query. Please be more specific.")
        print(f"DisambiguationError: {e.options}")

    except wikipedia.PageError:
        # Handle the case where no results are found
        speak("Sorry, I could not find any information on Wikipedia for that topic.")
        print("PageError: No results found for the query.")

    except Exception as e:
        # Catch all other exceptions
        speak("Sorry, an error occurred while searching Wikipedia.")
        print(f"Error: {e}")

# Weather function
def weather_command():
    speak("Please tell me the location for weather information.")
    location = listen_command()
    if location:
        get_weather(location)
    else:
        speak("I couldn't hear the location. Please try again.")

# Battery status function
def battery_percentage_query():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"The battery is at {percent}% charge.")
    else:
        speak("Battery information is not available.")

# List running apps function
def list_running_apps():
    speak("Checking running applications.")
    running_apps = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            app_name = proc.info['name']
            if app_name:
                running_apps.append(app_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if running_apps:
        speak(f"I found {len(running_apps)} running applications.")
        for app in running_apps[:10]:  # Limit output to 10 apps
            speak(app)
    else:
        speak("No running applications found.")

# How are you function
def handle_how_are_you():
    speak("I am absolutely fine, sir. What about you?")
    user_response = listen_command()
    
    if 'good' in user_response or 'i am fine' in user_response or 'fine' in user_response:
        speak("I'm glad to hear that!")
    else:
        speak("Sorry to hear that. Soon, it will get better!")

# Main Thread for Task Execution
class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=4)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

    def TaskExecution(self):
        global active
        startup()
        wishMe()
        
        while True:
            if not active:  # Check if NOVA is in sleep mode
                query = self.takeCommand()
                if 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
                    wake_up_mode()
                continue

            query = self.takeCommand()
            
            if 'tell me about' in query:
                tell_me_about(query)

            elif 'open' in query:
                if 'instagram' in query:
                    open_application('Instagram')
                elif 'youtube' in query:
                    open_application('YouTube')
                elif 'facebook' in query:
                    open_application('Facebook')
                else:
                    app_name = query.replace('open ', '').strip()
                    open_application(app_name)

            elif 'close' in query:
                if 'instagram' in query:
                    close_application('Instagram')
                elif 'youtube' in query:
                    close_application('YouTube')
                elif 'facebook' in query:
                    close_application('Facebook')
                else:
                    app_name = query.replace('close ', '').strip()
                    close_application(app_name)

            elif 'type' in query or 'start typing' in query:
                speak("Please tell me what should I type. Say 'exit typing' to stop.")
                while True:
                    text_to_type = listen_command()
                    if 'exit typing' in text_to_type or 'stop typing' in text_to_type:
                        speak("Exiting typing mode.")
                        break
                    elif text_to_type:
                        type_in_app(text_to_type)
                    else:
                        speak("I didn't catch that. Please try again.")

            elif 'save file' in query or 'save this file' in query:
                speak("Saving the current file.")
                save_file()

            elif 'send message' in query or 'send a message' in query:
                speak("Who should I send the message to?")
                recipient = listen_command()
                speak("What is the message?")
                message = listen_command()
                if recipient and message:
                    send_message(recipient, message)
                else:
                    speak("I couldn't get the recipient or message. Please try again.")

            elif "calculate" in query or "what is" in query or "multiply" in query or "times" in query:
                try:
                    question = query.replace("calculate", "").replace("what is", "").replace("multiply", "").replace("times", "").strip()
                    expression = sympify(question)
                    result = expression.evalf()

                    if float(result).is_integer():
                        answer = int(result)
                    else:
                        answer = round(float(result), 6)
                    print(f"The answer is {answer}")
                    speak(f"The answer is {answer}")
                except SympifyError:
                    speak("I couldn't understand the mathematical expression. Please try again.")
                except Exception as e:
                    speak("An error occurred while performing the calculation. Please try again.")

            elif 'play' in query:
                speak('Surfing the browser.... Hold on sir')
                query = query.replace('play', '')
                speak('Playing' + query)
                speak('Enjoy the music')
                pywhatkit.playonyt(query)

            elif any(keyword in query for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
                                                    'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
                                                    'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
                                                    'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
                YouTubeAuto(query)

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'ip address' in query:
                ip = get("https://api.ipify.org").text
                speak(f'Your current IP address is {ip}')

            elif 'time' in query or 'date' in query:
                now = datetime.datetime.now()
                if 'time' in query:
                    current_time = now.strftime("%I:%M %p")
                    speak(f"The current time is {current_time}")
                if 'date' in query:
                    current_date = now.strftime("%A, %B %d, %Y")
                    speak(f"Today's date is {current_date}")

            elif 'where is' in query:
                Place = query.replace('where is', '').replace('cortana', '').strip()
                if not Place:
                    speak("I couldn't understand the location. Please try again.")
                else:
                    speak(f"Searching for {Place} on Google Maps.")
                    webbrowser.open(f"https://www.google.com/maps/search/{Place}")

            elif 'current temperature' in query:
                search = "temperature in my current location"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f'The current temperature in your location is {temp}')

            elif 'windows' in query or any(keyword in query for keyword in ['home screen', 'minimize', 'minimise', 'maximise', 'maximize','close the window','close the application',
                                                                              'show start', 'open setting','open search', 'screen shot', 'shutdown' , 'restart', 'log out','system sleep'
                                                                              'take a screenshot' , 'restore windows','start recording', 'screenshot', 'stop recording']):
                WindowsAuto(query)

            elif "internet speed" in query:
                check_internet_speed()

            elif 'my location' in query:
                My_Location()

            elif 'show location' in query or 'find location' in query:
                try:
                    speak("Please tell me the name of the place.")
                    place = listen()
                    if place:
                        speak(f"Searching for {place} on Google Maps.")
                        GoogleMaps(place)
                    else:
                        speak("I couldn't hear the place name. Please try again.")
                except Exception as e:
                    print(f"Error occurred: {e}")
                    speak("Sorry, I couldn't fetch the location. Please try again.")

            elif 'open app' in query:
                speak("Which app would you like me to open?")
                app_name = listen_command()
                open_application(app_name)

            elif "hello" in query or "hey" in query:
                speak('Hello sir, Good to see you')
                speak('How may I help You?')

            elif any(keyword in query for keyword in ['turn on bluetooth','turn off bluetooth','bluetooth','increase brigntness', 'decrease brigntness',
                                                     'night light', 'increase volume', 'decrease volume', 'turn on night light','turn on aeroplance mode','turn off aeroplance mode',
                                                     'turn on night light', 'mute system volume','brightness','no sound','sound','check volume level','check current volume level',
                                                     'unmute system volume','maximum volume','set volume to','check brightness level','set brightness to']):
                process_command(query)

            elif "game" in query:
                games()
                
            elif 'search' in query:
                import wikipedia as googleScrap
                query = query.replace('jarvis', '').replace('google search', '').replace('google', '').strip()
                speak('Here are some results...')
                try:
                    pywhatkit.search(query)
                    result = googleScrap.summary(query, 3)
                    speak(result)
                except:
                    speak('Data not cached..')

            elif 'sleep mode' in query or 'sleep nova' in query or 'activate sleep mode' in query:
                sleep_mode()

            elif 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
                wake_up_mode()

            elif "weather" in query or 'climate' in query:
                weather_command()

            elif 'screenshot' in query or 'screen shot' in query:
                try:
                    import pyautogui
                    screenshot = pyautogui.screenshot()
                    screenshot.save("screenshot.jpg")
                    speak("Screenshot taken and saved as 'screenshot.jpg' in the current directory.")
                except Exception as e:
                    speak(f"Failed to take a screenshot: {e}")

            elif 'read news' in query or 'current news' in query or 'news mode' in query:
                read_news()

            elif 'space news' in query or 'nasa news' in query or 'astrological news' in query:
                latest_space_news()

            elif 'scroll up' in query or 'scroll down' in query or 'scroll to top' in query or 'scroll to bottom' in query:
                perform_scroll_action(query)

            elif any(keyword in query for keyword in ['add new tab','close tab','zoom in','zoom out', 'refresh page','go to history', 'go to bookmarks',
                                                     'switch to next tab', 'switch to previous tab', 'open history', 'open bookmarks',
                                                     'go back', 'go forward','open dev tools','toggle full screen','open private window'
                                                     'go to dev tools','go to private window','next tab','previous tab']):
                perform_browser_action(query)

            elif 'get to website' in query or 'go to website' in query:
                website_name = query.lower().replace("get to website", "").replace("go to website", "").strip()
                open_website(website_name)

            elif "battery status" in query or "battery percentage" in query:
                battery_percentage_query()

            elif "running apps" in query or "list running apps" in query:
                list_running_apps()

            elif 'how are you' in query:
                handle_how_are_you()

            elif 'movie' in query:
                movies_db = imdb.IMDb()
                speak("tell me the movie name:")
                text = listen_command()
                movies = movies_db.search_movie(text)
                speak("searching for " + text)
                speak("i found this")
                for movie in movies:
                    title = movie["title"]
                    year = movie["year"]
                    speak(f"{title}-{year}")
                    info = movie.getID()
                    movie_info = movies_db.get_movie(info)
                    rating = movie_info["rating"]
                    cast = movie_info["cast"]
                    plot = movie_info.get('plot outline','plot summary not available')
                    speak(f"{title} was released in {year} has imdb ratings of {rating}.the plot summary of movie is {plot}")
                    print(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {cast[0:5]}.the plot summary of movie is {plot}")

            elif 'how developed you' in query or 'who created you' in query or 'who is your master' in query:
                speak("thiyagu")

            elif "what are you" in query:
                speak('Hello sir, I am your personalized voice assistant, also known as Jarvis.')

            elif "what are the task's you can perform" in query:
                speak('google search, play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi speed, provide you news from NASA, calculate, search the map, wikipedia search, and many more')

            elif 'send an email' in query or 'send a mail' in query:
                speak("on what email address do you want to send sir? Please enter in terminal")
                receiver_add = input("Email address:")
                speak("what should be the subject sir?")
                subject = listen_command().capitalize()
                speak("what is the message?")
                message = listen_command().capitalize()
                if send_email(receiver_add, subject, message):
                    speak("I have sent the email sir")
                    print("I have sent the email sir")
                else:
                    speak("something went wrong sir")

            elif 'shutup' in query or 'exit program' in query or 'exit' in query:
                speak("Shutting down. Goodbye, sir.")
                sys.exit()

# Main Application
class JarvisApp:
    def __init__(self):
        self.core = MainThread()
        
    def start(self):
        """Execute Jarvis with proper sequence"""
        try:
            # Use the full paths to the desktop files
            desktop_1_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_1.py"
            desktop_2_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_2.py"
            
            # Step 1: Launch desktop_1.py and wait for it to finish
            print("Launching Desktop 1...")
            desktop_1_process = subprocess.Popen(["python", desktop_1_path])
            desktop_1_process.wait()
            
            # Step 2: Launch desktop_2.py
            print("Launching Desktop 2...")
            desktop_2_process = subprocess.Popen(["python", desktop_2_path])
            
            # Allow desktop_2.py some time to initialize
            time.sleep(3)
            
            # Step 3: Start the Main Task Execution in a separate thread
            print("Starting Main Task Execution...")
            self.core.start()
            
            # Keep the main process running
            self.core.wait()
            
        except Exception as e:
            print(f"Error in Jarvis execution: {e}")
            sys.exit(1)

if __name__ == "__main__":
    try:
        jarvis = JarvisApp()
        jarvis.start()
    except Exception as e:
        print(f"Error in main execution: {e}")
        sys.exit(1)