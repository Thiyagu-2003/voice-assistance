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
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
from new_desktop_2 import JarvisOverlayGUI, gui_instance

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

# Global active state
active = True

# Function to print to the terminal in the GUI
def terminal_print(text):
    """Print text to the terminal in the GUI and also to console"""
    print(text)  # Print to console for debugging
    if gui_instance:
        # Use QtCore.QMetaObject.invokeMethod to safely call GUI methods from other threads
        QtCore.QMetaObject.invokeMethod(
            gui_instance,
            "append_to_terminal",
            QtCore.Qt.ConnectionType.QueuedConnection,
            QtCore.Q_ARG(str, text)
        )

# Function to update the assistant state in the GUI
def update_assistant_state(state):
    """Update the GUI to reflect the current state of the assistant"""
    if gui_instance:
        QtCore.QMetaObject.invokeMethod(
            gui_instance, 
            "update_gif_state", 
            QtCore.Qt.ConnectionType.QueuedConnection,
            QtCore.Q_ARG(str, state)
        )

def speak(audio):
    """Speak the given text."""
    update_assistant_state("speaking")
    terminal_print(f"NOVA: {audio}")
    engine.say(audio)
    engine.runAndWait()
    update_assistant_state("sleeping")  # Return to default state after speaking

def listen_command():
    """Listen for a voice command from the user."""
    update_assistant_state("listening")
    terminal_print("Listening...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=4)
    
    update_assistant_state("loading")  # Switch to loading while processing speech
    try:
        command = recognizer.recognize_google(audio, language='en-in').lower()
        terminal_print(f"You said: {command}")
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
    terminal_print("Initializing NOVA...")
    speak("All systems have been activated.")

# Greet the user based on time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        terminal_print("Good morning sir!")
        speak("Good morning sir!")
    elif hour >= 12 and hour < 17:
        terminal_print("Good afternoon sir!")
        speak("Good afternoon sir!")
    elif hour >= 17 and hour < 21:
        terminal_print("Good evening sir!")
        speak("Good evening sir!")
    else:
        terminal_print("Good night sir!")
        speak("Good night sir!")
    speak("Please tell me how may I help you.")

# Wikipedia search function
def tell_me_about(query):
    try:
        # Removing the trigger phrase
        speak('Searching Wikipedia...please wait')
        query = query.replace("tell me about", "").strip()
        terminal_print(f"Query: {query}")

        # Searching for the topic
        results = wikipedia.summary(query, sentences=2)
        
        # Speaking the result
        speak("According to wikipedia...")
        terminal_print(results)
        speak(results)

    except wikipedia.DisambiguationError as e:
        # Handle multiple results found for the query
        speak("There are multiple topics matching your query. Please be more specific.")
        terminal_print(f"DisambiguationError: {e.options}")

    except wikipedia.PageError:
        # Handle the case where no results are found
        speak("Sorry, I could not find any information on Wikipedia for that topic.")
        terminal_print("PageError: No results found for the query.")

    except Exception as e:
        # Catch all other exceptions
        speak("Sorry, an error occurred while searching Wikipedia.")
        terminal_print(f"Error: {e}")

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
    # Add a signal to communicate with GUI
    terminal_signal = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(MainThread, self).__init__()
        # Connect the signal to the terminal_print function
        self.terminal_signal.connect(self.emit_terminal_text)
    
    def emit_terminal_text(self, text):
        """Handle the signal emission by updating the GUI"""
        terminal_print(text)

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.terminal_signal.emit("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=4)

        try:
            self.terminal_signal.emit("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            self.terminal_signal.emit(f"User said: {query}")
        except Exception as e:
            self.terminal_signal.emit("Say that again please...")
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
                    terminal_print(f"The answer is {answer}")
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

            elif 'open nova documentation' in query or 'open documentation' in query or 'open nova document' in query or 'open nova doc' in query or 'open doc' in query:
                speak("Opening Nova documentation, sir.")
                webbrowser.open("https://docs.google.com/document/d/1P9IIDUwryn3IXeyReSDqVwbukJOUIgazOn1htyIXzw8/edit?usp=sharing")

            elif 'shutup' in query or 'exit program' in query or 'exit' in query:
                speak("Shutting down. Goodbye, sir.")
                sys.exit()

# Modified JarvisApp class
class JarvisApp:
    def __init__(self):
        self.core = MainThread()
        
    def start(self):
        """Execute Jarvis with proper sequence"""
        try:
            # Use the full paths to the desktop files
            desktop_1_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_1.py"
            desktop_2_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_2.py"
            
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
        
        # Initialize and start Jarvis
        jarvis = JarvisApp()
        main_thread = jarvis.start()
        
        # Keep the application running
        sys.exit(app.exec())
        
    except Exception as e:
        print(f"Error in main execution: {e}")
        sys.exit(1)