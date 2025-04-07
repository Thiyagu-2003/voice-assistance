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
import re
import platform
import logging
import json
from plyer import notification
# Import all the required modules and features
from YT import YouTubeAuto
from WindowsAuto import WindowsAuto
from internet_speed_test import check_internet_speed
from Features import My_Location, GoogleMaps, listen, read_news, send_email
from on_off import process_command
from game import games
from Nasa import latest_space_news
from scrool_system import perform_scroll_action, scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
from scrool_system import perform_browser_action
from desktop_1 import InfoDialog, JarvisGUI
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
from desktop_2 import JarvisOverlayGUI
from temperature import get_weather_api
from application_handler_new import open_website, open_system_app, close_application, close_website,type_in_app,save_file,process_app_command
from gemini import query_google_gemini
#from gemini import query_gemini_image, query_gemini_code, query_gemini_text,process_query
from api import speak, listen, process_command, search_pincode, search_book, get_random_recipe, get_lyrics, get_quote, get_fun_fact, call_anime_quote_api, call_anime_character_api, get_lyrics, get_word_definition

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

# Global active state
active = True


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from desktop_2 import JarvisOverlayGUI
# In main_2.py, add this to communicate with the GUI
def update_assistant_state(state):
    """Update the GUI to reflect the current state of the assistant"""
    for widget in QApplication.topLevelWidgets():
        if isinstance(widget, JarvisOverlayGUI):
            QtCore.QMetaObject.invokeMethod(
                widget, 
                "update_gif_state", 
                QtCore.Qt.ConnectionType.QueuedConnection,
                QtCore.Q_ARG(str, state)
            )

# -----------------------------
# Memory storage (name, preferences, last search)
# -----------------------------
MEMORY_FILE = 'memory.json'

def load_memory():
    try:
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"name": "", "preferences": {}, "last_search": ""}

def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

memory = load_memory()

# -----------------------------
# Task system with reminders
# -----------------------------
TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# -----------------------------
# Background Task Checker
# -----------------------------
def task_checker():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks = load_tasks()
        for task in tasks:
            if task['time'] == now and not task.get("done"):
                reminder_message = f"Reminder: {task['task']}"
                speak(reminder_message)
                show_notification("Task Reminder", task['task'])
                task["done"] = True
        save_tasks(tasks)
        time.sleep(60)

# -----------------------------
# Notification function
# -----------------------------
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def speak(audio):
    """Speak the given text."""
    update_assistant_state("speaking")
    engine.say(audio)
    engine.runAndWait()
    update_assistant_state("sleeping")  # Return to default state after speaking

def listen_command():
    """Listen for a voice command from the user."""
    update_assistant_state("listening")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=4)
    
    update_assistant_state("loading")  # Switch to loading while processing speech
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
    
def process_app_command(command):
    """Process the user's voice command."""
    if not command:
        return True
    command = command.lower().strip()

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

def Terminalprint(self,text):
    self.Terminalext.appendPlainText(text)



def process_weather_command(query):         #working    #new
    """Process weather-related voice commands."""
    # Check if it's a weather request
    if "weather" in query or "temperature" in query or "climate" in query or "current temperature" in query or "forecast" in query:
        # Extract location if provided
        location = "Chennai"  # Default location
        
        # Try to find a location in the query
        if "in" in query:
            location_part = query.split("in", 1)[1].strip()
            if location_part:
                location = location_part
        
        # Get and speak weather information
        get_weather_api(location)
        return True
    return False

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
            
            # Convert to lowercase for easier command processing
            query_lower = query.lower()
            
            if 'tell me about' in query_lower:
                tell_me_about(query)

            elif 'type' in query_lower or 'start typing' in query_lower or 'type something' in query_lower or 'typing mode' in query_lower:
                type_in_app() 

            elif 'exit typing' in query_lower or 'stop typing' in query_lower or 'end typing' in query_lower or 'quit typing' in query_lower:
                type_in_app()

            elif 'save file' in query_lower or 'save this file' in query_lower or 'save the file' in query_lower:
                speak("Saving the current file.")
                save_file()

            elif "calculate" in query_lower or "what is" in query_lower or "multiply" in query_lower or "times" in query_lower:
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

            elif 'play' in query_lower:
                speak('Surfing the browser.... Hold on sir')
                query = query.replace('play', '')
                speak('Playing' + query)
                speak('Enjoy the music')
                pywhatkit.playonyt(query)

            elif any(keyword in query_lower for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
                                                    'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
                                                    'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
                                                    'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
                YouTubeAuto(query)

            elif 'joke' in query_lower:
                speak(pyjokes.get_joke())

            elif 'ip address' in query_lower:
                ip = get("https://api.ipify.org").text
                speak(f'Your current IP address is {ip}')

            elif 'time' in query_lower or 'date' in query_lower:
                now = datetime.datetime.now()
                if 'time' in query_lower:
                    current_time = now.strftime("%I:%M %p")
                    speak(f"The current time is {current_time}")
                if 'date' in query_lower:
                    current_date = now.strftime("%A, %B %d, %Y")
                    speak(f"Today's date is {current_date}")

            elif 'where is' in query_lower:
                Place = query.replace('where is', '').replace('cortana', '').strip()
                if not Place:
                    speak("I couldn't understand the location. Please try again.")
                else:
                    speak(f"Searching for {Place} on Google Maps.")
                    webbrowser.open(f"https://www.google.com/maps/search/{Place}")

            elif 'temperature' in query_lower or 'weather' in query_lower or 'climate' in query_lower or 'current temperature' in query_lower:
                process_weather_command(query)

            elif 'windows' in query_lower or any(keyword in query_lower for keyword in ['home screen', 'minimize', 'minimise', 'maximise', 'maximize','close the window','close the application',
                                                                        'show start', 'open setting','open search', 'screen shot', 'shutdown' , 'restart', 'log out','system sleep'
                                                                        'take a screenshot' , 'restore windows','start recording', 'screenshot', 'stop recording']):
                WindowsAuto(query)

            elif "internet speed" in query_lower:
                check_internet_speed()

            elif 'my location' in query_lower or 'current location' in query_lower or 'where am i' in query_lower:
                My_Location()

            elif 'show location' in query_lower or 'find location' in query_lower:
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

            elif "hello" in query_lower or "hey" in query_lower:
                speak('Hello sir, Good to see you')
                speak('How may I help You?')

            elif any(keyword in query_lower for keyword in ['turn on bluetooth','turn off bluetooth','bluetooth','increase brigntness', 'decrease brigntness',
                                                    'night light', 'increase volume', 'decrease volume', 'turn on night light','turn on aeroplance mode','turn off aeroplance mode',
                                                    'turn on night light', 'mute system volume','brightness','no sound','sound','check volume level','check current volume level',
                                                    'unmute system volume','maximum volume','set volume to','check brightness level','set brightness to']):
                process_command(query)

            elif "game" in query_lower:
                games()
                
            elif 'search' in query_lower:
                import wikipedia as googleScrap
                query = query.replace('jarvis', '').replace('google search', '').replace('google', '').strip()
                speak('Here are some results...')
                try:
                    pywhatkit.search(query)
                    result = googleScrap.summary(query, 3)
                    speak(result)
                except:
                    speak('Data not cached..')

            elif 'sleep mode' in query_lower or 'sleep nova' in query_lower or 'activate sleep mode' in query_lower:
                sleep_mode()

            elif 'wake up' in query_lower or 'wakeup' in query_lower or 'activate wake up mode' in query_lower:
                wake_up_mode()

                # First, convert query to lowercase
                query_lower = query.lower()

            # Screenshot command handling
            elif any(phrase in query_lower for phrase in ["capture screen", "take a screenshot", "screenshot", "screen shot","capture"]):
                try:
                    import pyautogui
                    screenshot = pyautogui.screenshot()
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"screenshot_{timestamp}.jpg"
                    screenshot.save(filename)
                    speak(f"Screenshot taken and saved")
                    print(f"Screenshot saved as: {filename}")
                except Exception as e:
                    speak(f"Failed to take a screenshot: {e}")
                    print(f"Screenshot error: {e}")
                    
            elif 'read news' in query_lower or 'current news' in query_lower or 'news mode' in query_lower:
                read_news()

            elif 'space news' in query_lower or 'nasa news' in query_lower or 'astrological news' in query_lower:
                latest_space_news()

            elif 'scroll up' in query_lower or 'scroll down' in query_lower or 'scroll to top' in query_lower or 'scroll to bottom' in query_lower:
                perform_scroll_action(query)

            elif any(keyword in query_lower for keyword in ['add new tab','close tab','zoom in','zoom out', 'refresh page','go to history', 'go to bookmarks',
                                                    'switch to next tab', 'switch to previous tab', 'open history', 'open bookmarks',
                                                    'go back', 'go forward','open dev tools','toggle full screen','open private window'
                                                    'go to dev tools','go to private window','next tab','previous tab']):
                perform_browser_action(query)

            elif "battery status" in query_lower or "battery percentage" in query_lower:
                battery_percentage_query()

            elif "running apps" in query_lower or "list running apps" in query_lower:
                list_running_apps()

            elif 'how are you' in query_lower:
                handle_how_are_you()

            elif 'movie' in query_lower:
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

            elif 'how developed you' in query_lower or 'who created you' in query_lower or 'who is your master' in query_lower:
                speak("thiyagu")

            elif "what are you" in query_lower:
                speak('Hello sir, I am your personalized voice assistant, also known as Nova.')

            elif "what are the task's you can perform" in query_lower:
                speak('google search, play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi speed, provide you news from NASA, calculate, search the map, wikipedia search, and many more')

            elif 'send an email' in query_lower or 'send a mail' in query_lower:
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

            elif 'open nova documentation' in query_lower or 'open documentation' in query_lower or 'open nova document' in query_lower:
                speak("Opening Nova documentation, sir.")
                webbrowser.open("https://docs.google.com/document/d/1P9IIDUwryn3IXeyReSDqVwbukJOUIgazOn1htyIXzw8/edit?usp=sharing")

            elif 'open camera' in query_lower:
                speak("Opening camera.")
                if platform.system() == 'Windows':
                    os.system("start microsoft.windows.camera:")
                elif platform.system() == 'Darwin':  # macOS
                    os.system("open -a Photo\\ Booth")
                elif platform.system() == 'Linux':
                    os.system("cheese")

            elif 'close camera' in query_lower:
                speak("Closing camera.")
                if platform.system() == 'Windows':
                    close_application("camera")
                elif platform.system() == 'Darwin':  # macOS
                    close_application("Photo Booth")
                elif platform.system() == 'Linux':
                    close_application("cheese")

            elif 'open' in query_lower and len(query.replace('open', '').strip()) > 0:
                item_name = query.lower().replace("open", "").strip()
                
                # Try to open as system app first
                app_success = open_system_app(item_name)
                
                # If not successful as an app, try as website
                if not app_success:
                    website_success = open_website(item_name)
                    
                # If neither worked, inform the user
                if not app_success and not website_success:
                    speak(f"I couldn't find {item_name} as an app or website in my database.")

            elif 'close' in query_lower and len(query.replace('close', '').strip()) > 0:
                item_name = query.lower().replace("close", "").strip()
                
                # Try to close as system app first
                app_success = close_application(item_name)
                
                # If not successful as an app, try as website (browser tab)
                if not app_success:
                    website_success = close_website(item_name)
                    
                # If neither worked, inform the user
                if not app_success and not website_success:
                    speak(f"I couldn't find {item_name} as an open app or website tab.")

            elif "book" in query_lower:
                search_book(query_lower.replace("book", "").strip())

            elif "pincode" in query_lower:
                search_pincode(query_lower.split()[-1])

            elif "recipe" in query_lower or "cook" in query_lower or "food" in query_lower:
                get_random_recipe()

            elif "lyrics" in query_lower and "by" in query_lower:
                parts = query_lower.split("lyrics", 1)[1].strip()
                song, artist = parts.split("by", 1)
                get_lyrics(artist.strip(), song.strip())

            elif "quote" in query_lower or "inspiration" in query_lower:
                get_quote()

            elif "fact" in query_lower:
                get_fun_fact()

            elif "anime quote" in query_lower:
                call_anime_quote_api()

            elif "anime character" in query_lower:
                call_anime_character_api()
            
            elif "meaning" in query_lower or "define" in query_lower or "dictionary" in query_lower:
                get_word_definition()

            elif any(phrase in query_lower for phrase in ["select all", "highlight all", "mark all"]):
                try:
                    import pyautogui
                    pyautogui.hotkey("ctrl", "a")
                    speak("All text selected")
                    print("Select All command executed")
                except Exception as e:
                    speak(f"Failed to select all: {e}")
                    print(f"Select All error: {e}")

            elif any(phrase in query_lower for phrase in ["copy", "copy text"]):
                try:
                    import pyautogui
                    pyautogui.hotkey("ctrl", "c")
                    speak("Text copied")
                    print("Copy command executed")
                except Exception as e:
                    speak(f"Failed to copy: {e}")
                    print(f"Copy error: {e}")


            elif any(phrase in query_lower for phrase in ["paste", "paste text"]):
                try:
                    import pyautogui
                    pyautogui.hotkey("ctrl", "v")
                    speak("Text pasted")
                    print("Paste command executed")
                except Exception as e:
                    speak(f"Failed to paste: {e}")
                    print(f"Paste error: {e}")


            elif any(phrase in query_lower for phrase in ["save file", "save document", "save this"]):
                try:
                    import pyautogui
                    pyautogui.hotkey("ctrl", "s")
                    speak("File saved")
                    print("Save command executed")
                except Exception as e:
                    speak(f"Failed to save file: {e}")
                    print(f"Save error: {e}")

            elif any(phrase in query_lower for phrase in ["undo", "go back"]):
                try:
                    import pyautogui
                    pyautogui.hotkey("ctrl", "z")
                    speak("Undo performed")
                    print("Undo command executed")
                except Exception as e:
                    speak(f"Failed to undo: {e}")
                    print(f"Undo error: {e}")

            elif any(phrase in query_lower for phrase in ["redo", "do again"]):
                try:
                    import pyautogui
                    pyautogui.hotkey("ctrl", "y")
                    speak("Redo performed")
                    print("Redo command executed")
                except Exception as e:
                    speak(f"Failed to redo: {e}")
                    print(f"Redo error: {e}")


            elif any(phrase in query_lower for phrase in ["capture screen", "take a screenshot"]):
                try:
                    import pyautogui
                    screenshot = pyautogui.screenshot()
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"screenshot_{timestamp}.png"
                    screenshot.save(filename)
                    
                    # Open the screenshot
                    os.system(filename)  # Works on Windows
                    speak("Screenshot taken and opened")
                    print(f"Screenshot saved as: {filename}")
                except Exception as e:
                    speak(f"Failed to take a screenshot: {e}")
                    print(f"Screenshot error: {e}")

            elif any(phrase in query_lower for phrase in ["move mouse", "mouse to center"]):
                try:
                    import pyautogui
                    screen_width, screen_height = pyautogui.size()  # Get screen size
                    pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=1)  # Move to center
                    speak("Mouse moved to the center")
                    print("Mouse moved to center")
                except Exception as e:
                    speak(f"Failed to move mouse: {e}")
                    print(f"Mouse move error: {e}")


            elif any(phrase in query_lower for phrase in ["click", "left click"]):
                import pyautogui
                pyautogui.click()
                speak("Clicked")

            elif any(phrase in query_lower for phrase in ["double click"]):
                import pyautogui
                pyautogui.doubleClick()
                speak("Double clicked")

            elif any(phrase in query_lower for phrase in ["right click"]):
                import pyautogui
                pyautogui.rightClick()
                speak("Right clicked")

                # newly added code for remembering name and tasks


            elif "my name is" in query_lower:
                memory['name'] = query_lower.split("my name is")[-1].strip()
                save_memory(memory)
                speak(f"Got it! I’ll remember your name is {memory['name']}.")

            elif "what is my name" in query_lower:
                if memory['name']:
                    speak(f"Your name is {memory['name']}.")
                else:
                    speak("I don't know your name yet.")

            elif "remember that" in query_lower:
                key = query_lower.split("remember that")[-1].strip()
                memory['last_search'] = key
                save_memory(memory)
                speak(f"I’ll remember that: {key}.")

            elif "what did i ask you to remember" in query_lower:
                if memory['last_search']:
                    speak(f"You asked me to remember: {memory['last_search']}.")
                else:
                    speak("You haven't asked me to remember anything yet.")

            elif "remind me to" in query_lower:
                try:
                    # Expected format: "remind me to drink water at 15:30"
                    task_text = query_lower.split("remind me to")[1].split(" at ")[0].strip()
                    task_time = query_lower.split(" at ")[1].strip()

                    now = datetime.now()
                    full_time = datetime.strptime(f"{now.date()} {task_time}", "%Y-%m-%d %H:%M")

                    task = {
                        "task": task_text,
                        "time": full_time.strftime("%Y-%m-%d %H:%M"),
                        "done": False
                    }

                    tasks = load_tasks()
                    tasks.append(task)
                    save_tasks(tasks)

                    speak(f"Reminder set for {task_text} at {task_time}")
                except Exception as e:
                    print("Error:", e)
                    speak("Please say: remind me to [task] at [HH:MM]")




            elif 'shutup' in query_lower or 'exit program' in query_lower or 'exit' in query_lower:
                speak("Shutting down. Goodbye, sir.")
                sys.exit()

            elif "gemini" in query_lower:
            #else:
                speak("I am not programmed to answer that. Let me check online...")
                response = query_google_gemini(query)
                
                # Split the response into content and token info (if present)
                if "\n\nTokens - " in response:
                    main_content, token_info = response.split("\n\nTokens - ", 1)
                    token_info = "Tokens - " + token_info
                else:
                    main_content = response
                    token_info = ""
                
                # Only speak the main content
                speak(main_content)
                
                # Print the full response including token info
                print(response)

# Modified JarvisApp class
class JarvisApp:
    def __init__(self):
        self.core = MainThread()
        
    def start(self):
        """Execute Jarvis with proper sequence"""
        try:
            # Use the full paths to the desktop files
            desktop_1_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\NOVA-ai-main\\desktop_1.py"
            desktop_2_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\NOVA-ai-main\\desktop_2.py"
            
            # Launch desktop_1.py and wait for it to complete initialization
            print("Launching Desktop 1...")
            desktop_1_process = subprocess.Popen(["python", desktop_1_path])
            
            # Allow desktop_1.py time to fully initialize
            time.sleep(15)
            
            # Launch desktop_2.py and wait for it to complete initialization
            print("Launching Desktop 2...")
            desktop_2_process = subprocess.Popen(["python", desktop_2_path])
            
            # Allow desktop_2.py time to fully initialize
            time.sleep(3)
            
            # Start the Main Task Execution
            print("Starting Main Task Execution...")
            self.core.start()
            
            return self.core
            
        except Exception as e:
            print(f"Error in Jarvis execution: {e}")
            sys.exit(1)

# Modified main execution
if __name__ == "__main__":
    try:
        # Create a QApplication instance
        app = QApplication(sys.argv)
        threading.Thread(target=task_checker, daemon=True).start()
        # Initialize and start Jarvis
        jarvis = JarvisApp()
        main_thread = jarvis.start()
        
        # Keep the application running
        sys.exit(app.exec())
        
    except Exception as e:
        print(f"Error in main execution: {e}")
        sys.exit(1)