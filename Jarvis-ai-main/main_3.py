# # # # from sqlite3 import Date
# # # # import pyttsx3
# # # # import speech_recognition as sr
# # # # import datetime
# # # # import wikipedia
# # # # import webbrowser
# # # # import pywhatkit
# # # # import pyjokes
# # # # import os
# # # # from requests import get
# # # # import sys
# # # # import requests
# # # # from bs4 import BeautifulSoup
# # # # import subprocess
# # # # import time
# # # # import threading
# # # # import psutil
# # # # import imdb
# # # # from PyQt6.QtWidgets import QApplication
# # # # from PyQt6 import QtCore
# # # # from sympy import sympify, SympifyError

# # # # # Import all the required modules and features
# # # # from YT import YouTubeAuto
# # # # from WindowsAuto import WindowsAuto
# # # # from internet_speed_test import check_internet_speed
# # # # from Features import My_Location, GoogleMaps, listen, Temp, read_news, send_email
# # # # from on_off import process_command
# # # # from app_handler import open_application, close_application, type_in_app, save_file, send_message
# # # # from game import games
# # # # from utils import get_weather
# # # # from Nasa import latest_space_news
# # # # from scrool_system import perform_scroll_action, scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
# # # # from scrool_system import perform_browser_action
# # # # from Web_Open import open_website
# # # # from desktop_1 import InfoDialog, JarvisGUI

# # # # # Initialize pyttsx3 engine
# # # # engine = pyttsx3.init('sapi5')
# # # # voices = engine.getProperty('voices')
# # # # engine.setProperty('voice', voices[0].id)
# # # # engine.setProperty('rate', 175)

# # # # # Global active state
# # # # active = True

# # # # # Global terminal widget (will be set from outside)
# # # # terminal_widget = None  # Added global variable

# # # # def speak(audio):
# # # #     """Speak the given text."""
# # # #     engine.say(audio)
# # # #     engine.runAndWait()

# # # # def listen_command():
# # # #     """Listen for a voice command from the user."""
# # # #     recognizer = sr.Recognizer()
# # # #     with sr.Microphone() as source:
# # # #         print_to_terminal("Listening...")
# # # #         recognizer.adjust_for_ambient_noise(source)
# # # #         audio = recognizer.listen(source, timeout=4)

# # # #     try:
# # # #         command = recognizer.recognize_google(audio, language='en-in').lower()
# # # #         print_to_terminal(f"You said: {command}\n")
# # # #         return command
# # # #     except sr.UnknownValueError:
# # # #         speak("Sorry, I couldn't understand that.")
# # # #         return ""
# # # #     except sr.RequestError:
# # # #         speak("Sorry, there was an issue with the speech recognition service.")
# # # #         return ""

# # # # # Sleep and Wake-up functions
# # # # def sleep_mode():
# # # #     global active
# # # #     active = False
# # # #     speak("I am going to sleep mode. Say 'Wake up nova' to reactivate me.")

# # # # def wake_up_mode():
# # # #     global active
# # # #     active = True
# # # #     speak("I am back and ready to assist you.")

# # # # # Startup message
# # # # def startup():
# # # #     print_to_terminal("All systems have been activated.")
# # # #     speak("All systems have been activated.")

# # # # # Greet the user based on time
# # # # def wishMe():
# # # #     hour = int(datetime.datetime.now().hour)
# # # #     if hour >= 0 and hour < 12:
# # # #         print_to_terminal("Good morning sir!")
# # # #         speak("Good morning sir!")
# # # #     elif hour >= 12 and hour < 17:
# # # #         print_to_terminal("Good afternoon sir!")
# # # #         speak("Good afternoon sir!")
# # # #     elif hour >= 17 and hour < 21:
# # # #         print_to_terminal("Good evening sir!")
# # # #         speak("Good evening sir!")
# # # #     else:
# # # #         print_to_terminal("Good night sir!")
# # # #         speak("Good night sir!")
# # # #     speak("Please tell me how may I help you.")

# # # # # Wikipedia search function
# # # # def tell_me_about(query):
# # # #     try:
# # # #         # Removing the trigger phrase
# # # #         speak('Searching Wikipedia...please wait')
# # # #         query = query.replace("tell me about", "").strip()
# # # #         print_to_terminal(f"Query: {query}")

# # # #         # Searching for the topic
# # # #         results = wikipedia.summary(query, sentences=2)

# # # #         # Speaking the result
# # # #         speak("According to wikipedia...")
# # # #         print_to_terminal(results)
# # # #         speak(results)

# # # #     except wikipedia.DisambiguationError as e:
# # # #         # Handle multiple results found for the query
# # # #         speak("There are multiple topics matching your query. Please be more specific.")
# # # #         print_to_terminal(f"DisambiguationError: {e.options}")

# # # #     except wikipedia.PageError:
# # # #         # Handle the case where no results are found
# # # #         speak("Sorry, I could not find any information on Wikipedia for that topic.")
# # # #         print_to_terminal("PageError: No results found for the query.")

# # # #     except Exception as e:
# # # #         # Catch all other exceptions
# # # #         speak("Sorry, an error occurred while searching Wikipedia.")
# # # #         print_to_terminal(f"Error: {e}")

# # # # # Weather function
# # # # def weather_command():
# # # #     speak("Please tell me the location for weather information.")
# # # #     location = listen_command()
# # # #     if location:
# # # #         get_weather(location)
# # # #     else:
# # # #         speak("I couldn't hear the location. Please try again.")

# # # # # Battery status function
# # # # def battery_percentage_query():
# # # #     battery = psutil.sensors_battery()
# # # #     if battery:
# # # #         percent = battery.percent
# # # #         print_to_terminal(f"The battery is at {percent}% charge.")
# # # #         speak(f"The battery is at {percent}% charge.")
# # # #     else:
# # # #         speak("Battery information is not available.")

# # # # # List running apps function
# # # # def list_running_apps():
# # # #     speak("Checking running applications.")
# # # #     running_apps = []
# # # #     for proc in psutil.process_iter(['pid', 'name']):
# # # #         try:
# # # #             app_name = proc.info['name']
# # # #             if app_name:
# # # #                 running_apps.append(app_name)
# # # #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
# # # #             continue

# # # #     if running_apps:
# # # #         print_to_terminal(f"I found {len(running_apps)} running applications.")
# # # #         speak(f"I found {len(running_apps)} running applications.")
# # # #         for app in running_apps[:10]:  # Limit output to 10 apps
# # # #             print_to_terminal(app)
# # # #             speak(app)
# # # #     else:
# # # #         speak("No running applications found.")

# # # # # How are you function
# # # # def handle_how_are_you():
# # # #     speak("I am absolutely fine, sir. What about you?")
# # # #     user_response = listen_command()

# # # #     if 'good' in user_response or 'i am fine' in user_response or 'fine' in user_response:
# # # #         speak("I'm glad to hear that!")
# # # #     else:
# # # #         speak("Sorry to hear that. Soon, it will get better!")

# # # # # Thread-safe function to append to the terminal
# # # # def print_to_terminal(text):
# # # #     global terminal_widget
# # # #     if terminal_widget:
# # # #         terminal_widget.append_to_terminal(text)
# # # #     else:
# # # #         print(text)  # Fallback if terminal is not yet available

# # # # # Main Thread for Task Execution
# # # # class MainThread(QtCore.QThread):
# # # #     def __init__(self, terminal_widget):
# # # #         super(MainThread, self).__init__()
# # # #         self.terminal_widget = terminal_widget

# # # #     def run(self):
# # # #         self.TaskExecution()

# # # #     def takeCommand(self):
# # # #         r = sr.Recognizer()
# # # #         with sr.Microphone() as source:
# # # #             print_to_terminal("Listening...")
# # # #             r.pause_threshold = 1
# # # #             audio = r.listen(source, timeout=4)

# # # #         try:
# # # #             print_to_terminal("Recognizing...")
# # # #             query = r.recognize_google(audio, language='en-in')
# # # #             print_to_terminal(f"User said: {query}\n")
# # # #         except Exception as e:
# # # #             print_to_terminal("Say that again please...")
# # # #             return "None"
# # # #         return query.lower()

# # # #     def TaskExecution(self):
# # # #         global active, terminal_widget
# # # #         terminal_widget = self.terminal_widget
# # # #         startup()
# # # #         wishMe()

# # # #         while True:
# # # #             if not active:  # Check if NOVA is in sleep mode
# # # #                 query = self.takeCommand()
# # # #                 if 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
# # # #                     wake_up_mode()
# # # #                 continue

# # # #             query = self.takeCommand()

# # # #             if 'tell me about' in query:
# # # #                 tell_me_about(query)

# # # #             elif 'open' in query:
# # # #                 if 'instagram' in query:
# # # #                     open_application('Instagram')
# # # #                 elif 'youtube' in query:
# # # #                     open_application('YouTube')
# # # #                 elif 'facebook' in query:
# # # #                     open_application('Facebook')
# # # #                 else:
# # # #                     app_name = query.replace('open ', '').strip()
# # # #                     open_application(app_name)

# # # #             elif 'close' in query:
# # # #                 if 'instagram' in query:
# # # #                     close_application('Instagram')
# # # #                 elif 'youtube' in query:
# # # #                     close_application('YouTube')
# # # #                 elif 'facebook' in query:
# # # #                     close_application('Facebook')
# # # #                 else:
# # # #                     app_name = query.replace('close ', '').strip()
# # # #                     close_application(app_name)

# # # #             elif 'type' in query or 'start typing' in query:
# # # #                 speak("Please tell me what should I type. Say 'exit typing' to stop.")
# # # #                 while True:
# # # #                     text_to_type = listen_command()
# # # #                     if 'exit typing' in text_to_type or 'stop typing' in text_to_type:
# # # #                         speak("Exiting typing mode.")
# # # #                         break
# # # #                     elif text_to_type:
# # # #                         type_in_app(text_to_type)
# # # #                     else:
# # # #                         speak("I didn't catch that. Please try again.")

# # # #             elif 'save file' in query or 'save this file' in query:
# # # #                 speak("Saving the current file.")
# # # #                 save_file()

# # # #             elif 'send message' in query or 'send a message' in query:
# # # #                 speak("Who should I send the message to?")
# # # #                 recipient = listen_command()
# # # #                 speak("What is the message?")
# # # #                 message = listen_command()
# # # #                 if recipient and message:
# # # #                     send_message(recipient, message)
# # # #                 else:
# # # #                     speak("I couldn't get the recipient or message. Please try again.")

# # # #             elif "calculate" in query or "what is" in query or "multiply" in query or "times" in query:
# # # #                 try:
# # # #                     question = query.replace("calculate", "").replace("what is", "").replace("multiply", "").replace("times", "").strip()
# # # #                     expression = sympify(question)
# # # #                     result = expression.evalf()

# # # #                     if float(result).is_integer():
# # # #                         answer = int(result)
# # # #                     else:
# # # #                         answer = round(float(result), 6)
# # # #                     print_to_terminal(f"The answer is {answer}")
# # # #                     speak(f"The answer is {answer}")
# # # #                 except SympifyError:
# # # #                     speak("I couldn't understand the mathematical expression. Please try again.")
# # # #                 except Exception as e:
# # # #                     speak("An error occurred while performing the calculation. Please try again.")

# # # #             elif 'play' in query:
# # # #                 speak('Surfing the browser.... Hold on sir')
# # # #                 query = query.replace('play', '')
# # # #                 speak('Playing' + query)
# # # #                 speak('Enjoy the music')
# # # #                 pywhatkit.playonyt(query)

# # # #             elif any(keyword in query for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
# # # #                                                     'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
# # # #                                                     'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
# # # #                                                     'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
# # # #                 YouTubeAuto(query)

# # # #             elif 'joke' in query:
# # # #                 speak(pyjokes.get_joke())

# # # #             elif 'ip address' in query:
# # # #                 ip = get("https://api.ipify.org").text
# # # #                 print_to_terminal(f'Your current IP address is {ip}')
# # # #                 speak(f'Your current IP address is {ip}')

# # # #             elif 'time' in query or 'date' in query:
# # # #                 now = datetime.datetime.now()
# # # #                 if 'time' in query:
# # # #                     current_time = now.strftime("%I:%M %p")
# # # #                     print_to_terminal(f"The current time is {current_time}")
# # # #                     speak(f"The current time is {current_time}")
# # # #                 if 'date' in query:
# # # #                     current_date = now.strftime("%A, %B %d, %Y")
# # # #                     print_to_terminal(f"Today's date is {current_date}")
# # # #                     speak(f"Today's date is {current_date}")

# # # #             elif 'where is' in query:
# # # #                 Place = query.replace('where is', '').replace('cortana', '').strip()
# # # #                 if not Place:
# # # #                     speak("I couldn't understand the location. Please try again.")
# # # #                 else:
# # # #                     print_to_terminal(f"Searching for {Place} on Google Maps.")
# # # #                     speak(f"Searching for {Place} on Google Maps.")
# # # #                     webbrowser.open(f"https://www.google.com/maps/search/{Place}")

# # # #             elif 'current temperature' in query:
# # # #                 search = "temperature in my current location"
# # # #                 url = f"https://www.google.com/search?q={search}"
# # # #                 r = requests.get(url)
# # # #                 data = BeautifulSoup(r.text, "html.parser")
# # # #                 temp = data.find("div", class_="BNeawe").text
# # # #                 print_to_terminal(f'The current temperature in your location is {temp}')
# # # #                 speak(f'The current temperature in your location is {temp}')

# # # #             elif 'windows' in query or any(keyword in query for keyword in ['home screen', 'minimize', 'minimise', 'maximise', 'maximize','close the window','close the application',
# # # #                                                                               'show start', 'open setting','open search', 'screen shot', 'shutdown' , 'restart', 'log out','system sleep'
# # # #                                                                               'take a screenshot' , 'restore windows','start recording', 'screenshot', 'stop recording']):
# # # #                 WindowsAuto(query)

# # # #             elif "internet speed" in query:
# # # #                 check_internet_speed()

# # # #             elif 'my location' in query:
# # # #                 My_Location()

# # # #             elif 'show location' in query or 'find location' in query:
# # # #                 try:
# # # #                     speak("Please tell me the name of the place.")
# # # #                     place = listen()
# # # #                     if place:
# # # #                         print_to_terminal(f"Searching for {place} on Google Maps.")
# # # #                         speak(f"Searching for {place} on Google Maps.")
# # # #                         GoogleMaps(place)
# # # #                     else:
# # # #                         speak("I couldn't hear the place name. Please try again.")
# # # #                 except Exception as e:
# # # #                     print_to_terminal(f"Error occurred: {e}")
# # # #                     speak("Sorry, I couldn't fetch the location. Please try again.")

# # # #             elif 'open app' in query:
# # # #                 speak("Which app would you like me to open?")
# # # #                 app_name = listen_command()
# # # #                 open_application(app_name)

# # # #             elif "hello" in query or "hey" in query:
# # # #                 print_to_terminal('Hello sir, Good to see you')
# # # #                 print_to_terminal('How may I help You?')


# # # #             elif any(keyword in query for keyword in ['turn on bluetooth','turn off bluetooth','bluetooth','increase brigntness', 'decrease brigntness',
# # # #                                                      'night light', 'increase volume', 'decrease volume', 'turn on night light','turn on aeroplance mode','turn off aeroplance mode',
# # # #                                                      'turn on night light', 'mute system volume','brightness','no sound','sound','check volume level','check current volume level',
# # # #                                                      'unmute system volume','maximum volume','set volume to','check brightness level','set brightness to']):
# # # #                 process_command(query)

# # # #             elif "game" in query:
# # # #                 games()
                
# # # #             elif 'search' in query:
# # # #                 import wikipedia as googleScrap
# # # #                 query = query.replace('jarvis', '').replace('google search', '').replace('google', '').strip()
# # # #                 speak('Here are some results...')
# # # #                 try:
# # # #                     pywhatkit.search(query)
# # # #                     result = googleScrap.summary(query, 3)
# # # #                     speak(result)
# # # #                 except:
# # # #                     speak('Data not cached..')

# # # #             elif 'sleep mode' in query or 'sleep nova' in query or 'activate sleep mode' in query:
# # # #                 sleep_mode()

# # # #             elif 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
# # # #                 wake_up_mode()

# # # #             elif "weather" in query or 'climate' in query:
# # # #                 weather_command()

# # # #             elif 'screenshot' in query or 'screen shot' in query:
# # # #                 try:
# # # #                     import pyautogui
# # # #                     screenshot = pyautogui.screenshot()
# # # #                     screenshot.save("screenshot.jpg")
# # # #                     speak("Screenshot taken and saved as 'screenshot.jpg' in the current directory.")
# # # #                 except Exception as e:
# # # #                     speak(f"Failed to take a screenshot: {e}")

# # # #             elif 'read news' in query or 'current news' in query or 'news mode' in query:
# # # #                 read_news()

# # # #             elif 'space news' in query or 'nasa news' in query or 'astrological news' in query:
# # # #                 latest_space_news()

# # # #             elif 'scroll up' in query or 'scroll down' in query or 'scroll to top' in query or 'scroll to bottom' in query:
# # # #                 perform_scroll_action(query)

# # # #             elif any(keyword in query for keyword in ['add new tab','close tab','zoom in','zoom out', 'refresh page','go to history', 'go to bookmarks',
# # # #                                                      'switch to next tab', 'switch to previous tab', 'open history', 'open bookmarks',
# # # #                                                      'go back', 'go forward','open dev tools','toggle full screen','open private window'
# # # #                                                      'go to dev tools','go to private window','next tab','previous tab']):
# # # #                 perform_browser_action(query)

# # # #             elif 'get to website' in query or 'go to website' in query:
# # # #                 website_name = query.lower().replace("get to website", "").replace("go to website", "").strip()
# # # #                 open_website(website_name)

# # # #             elif "battery status" in query or "battery percentage" in query:
# # # #                 battery_percentage_query()

# # # #             elif "running apps" in query or "list running apps" in query:
# # # #                 list_running_apps()

# # # #             elif 'how are you' in query:
# # # #                 handle_how_are_you()

# # # #             elif 'movie' in query:
# # # #                 movies_db = imdb.IMDb()
# # # #                 speak("tell me the movie name:")
# # # #                 text = listen_command()
# # # #                 movies = movies_db.search_movie(text)
# # # #                 speak("searching for " + text)
# # # #                 speak("i found this")
# # # #                 for movie in movies:
# # # #                     title = movie["title"]
# # # #                     year = movie["year"]
# # # #                     speak(f"{title}-{year}")
# # # #                     info = movie.getID()
# # # #                     movie_info = movies_db.get_movie(info)
# # # #                     rating = movie_info["rating"]
# # # #                     cast = movie_info["cast"]
# # # #                     plot = movie_info.get('plot outline','plot summary not available')
# # # #                     speak(f"{title} was released in {year} has imdb ratings of {rating}.the plot summary of movie is {plot}")
# # # #                     print_to_terminal(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {cast[0:5]}.the plot summary of movie is {plot}")

# # # #             elif 'how developed you' in query or 'who created you' in query or 'who is your master' in query:
# # # #                 speak("thiyagu")

# # # #             elif "what are you" in query:
# # # #                 speak('Hello sir, I am your personalized voice assistant, also known as Jarvis.')

# # # #             elif "what are the task's you can perform" in query:
# # # #                 speak('google search, play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi speed, provide you news from NASA, calculate, search the map, wikipedia search, and many more')

# # # #             elif 'send an email' in query or 'send a mail' in query:
# # # #                 speak("on what email address do you want to send sir? Please enter in terminal")
# # # #                 receiver_add = input("Email address:")
# # # #                 speak("what should be the subject sir?")
# # # #                 subject = listen_command().capitalize()
# # # #                 speak("what is the message?")
# # # #                 message = listen_command().capitalize()
# # # #                 if send_email(receiver_add, subject, message):
# # # #                     speak("I have sent the email sir")
# # # #                     print_to_terminal("I have sent the email sir")
# # # #                 else:
# # # #                     speak("something went wrong sir")

# # # #             elif 'shutup' in query or 'exit program' in query or 'exit' in query:
# # # #                 speak("Shutting down. Goodbye, sir.")
# # # #                 sys.exit()

# # # # # Modified JarvisApp class
# # # # class JarvisApp:
# # # #     def __init__(self):
# # # #         self.core = MainThread()
        
# # # #     def start(self):
# # # #         """Execute Jarvis with proper sequence"""
# # # #         try:
# # # #             # Use the full paths to the desktop files
# # # #             desktop_1_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_1.py"
# # # #             desktop_2_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_2.py"
            
# # # #             # Launch desktop_1.py and wait for it to complete initialization
# # # #             print_to_terminal("Launching Desktop 1...")
# # # #             desktop_1_process = subprocess.Popen(["python", desktop_1_path])
            
# # # #             # Allow desktop_1.py time to fully initialize
# # # #             time.sleep(15)
            
# # # #             # Launch desktop_2.py and wait for it to complete initialization
# # # #             print_to_terminal("Launching Desktop 2...")
# # # #             desktop_2_process = subprocess.Popen(["python", desktop_2_path])
            
# # # #             # Allow desktop_2.py time to fully initialize
# # # #             time.sleep(3)
            
# # # #             # Start the Main Task Execution
# # # #             print_to_terminal("Starting Main Task Execution...")
# # # #             self.core.start()
            
# # # #             return self.core
            
# # # #         except Exception as e:
# # # #             print_to_terminal(f"Error in Jarvis execution: {e}")
# # # #             sys.exit(1)

# # # # # Modified main execution
# # # # if __name__ == "__main__":
# # # #     try:
# # # #         # Create a QApplication instance
# # # #         app = QApplication(sys.argv)
        
# # # #         # Initialize and start Jarvis
# # # #         jarvis = JarvisApp()
# # # #         main_thread = jarvis.start()
        
# # # #         # Keep the application running
# # # #         sys.exit(app.exec())
        
# # # #     except Exception as e:
# # # #         print_to_terminal(f"Error in main execution: {e}")
# # # #         sys.exit(1)



# # # from sqlite3 import Date
# # # import pyttsx3
# # # import speech_recognition as sr
# # # import datetime
# # # import wikipedia
# # # import webbrowser
# # # import pywhatkit
# # # import pyjokes
# # # import os
# # # from requests import get
# # # import sys
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import subprocess
# # # import time
# # # import threading
# # # import psutil
# # # import imdb
# # # from PyQt6.QtWidgets import QApplication
# # # from PyQt6 import QtCore
# # # from sympy import sympify, SympifyError

# # # # Import all the required modules and features
# # # from YT import YouTubeAuto
# # # from WindowsAuto import WindowsAuto
# # # from internet_speed_test import check_internet_speed
# # # from Features import My_Location, GoogleMaps, listen, Temp, read_news, send_email
# # # from on_off import process_command
# # # from app_handler import open_application, close_application, type_in_app, save_file, send_message
# # # from game import games
# # # from utils import get_weather
# # # from Nasa import latest_space_news
# # # from scrool_system import perform_scroll_action, scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
# # # from scrool_system import perform_browser_action
# # # from Web_Open import open_website
# # # from desktop_1 import InfoDialog, JarvisGUI

# # # # Initialize pyttsx3 engine
# # # engine = pyttsx3.init('sapi5')
# # # voices = engine.getProperty('voices')
# # # engine.setProperty('voice', voices[0].id)
# # # engine.setProperty('rate', 175)

# # # # Global active state
# # # active = True

# # # # Global terminal widget (will be set from outside)
# # # terminal_widget = None  # Added global variable

# # # def speak(audio):
# # #     """Speak the given text."""
# # #     engine.say(audio)
# # #     engine.runAndWait()

# # # def listen_command():
# # #     """Listen for a voice command from the user."""
# # #     recognizer = sr.Recognizer()
# # #     with sr.Microphone() as source:
# # #         print_to_terminal("Listening...")
# # #         recognizer.adjust_for_ambient_noise(source)
# # #         audio = recognizer.listen(source, timeout=4)

# # #     try:
# # #         command = recognizer.recognize_google(audio, language='en-in').lower()
# # #         print_to_terminal(f"You said: {command}\n")
# # #         return command
# # #     except sr.UnknownValueError:
# # #         speak("Sorry, I couldn't understand that.")
# # #         return ""
# # #     except sr.RequestError:
# # #         speak("Sorry, there was an issue with the speech recognition service.")
# # #         return ""

# # # # Sleep and Wake-up functions
# # # def sleep_mode():
# # #     global active
# # #     active = False
# # #     speak("I am going to sleep mode. Say 'Wake up nova' to reactivate me.")

# # # def wake_up_mode():
# # #     global active
# # #     active = True
# # #     speak("I am back and ready to assist you.")

# # # # Startup message
# # # def startup():
# # #     print_to_terminal("All systems have been activated.")
# # #     speak("All systems have been activated.")

# # # # Greet the user based on time
# # # def wishMe():
# # #     hour = int(datetime.datetime.now().hour)
# # #     if hour >= 0 and hour < 12:
# # #         print_to_terminal("Good morning sir!")
# # #         speak("Good morning sir!")
# # #     elif hour >= 12 and hour < 17:
# # #         print_to_terminal("Good afternoon sir!")
# # #         speak("Good afternoon sir!")
# # #     elif hour >= 17 and hour < 21:
# # #         print_to_terminal("Good evening sir!")
# # #         speak("Good evening sir!")
# # #     else:
# # #         print_to_terminal("Good night sir!")
# # #         speak("Good night sir!")
# # #     speak("Please tell me how may I help you.")

# # # # Wikipedia search function
# # # def tell_me_about(query):
# # #     try:
# # #         # Removing the trigger phrase
# # #         speak('Searching Wikipedia...please wait')
# # #         query = query.replace("tell me about", "").strip()
# # #         print_to_terminal(f"Query: {query}")

# # #         # Searching for the topic
# # #         results = wikipedia.summary(query, sentences=2)

# # #         # Speaking the result
# # #         speak("According to wikipedia...")
# # #         print_to_terminal(results)
# # #         speak(results)

# # #     except wikipedia.DisambiguationError as e:
# # #         # Handle multiple results found for the query
# # #         speak("There are multiple topics matching your query. Please be more specific.")
# # #         print_to_terminal(f"DisambiguationError: {e.options}")

# # #     except wikipedia.PageError:
# # #         # Handle the case where no results are found
# # #         speak("Sorry, I could not find any information on Wikipedia for that topic.")
# # #         print_to_terminal("PageError: No results found for the query.")

# # #     except Exception as e:
# # #         # Catch all other exceptions
# # #         speak("Sorry, an error occurred while searching Wikipedia.")
# # #         print_to_terminal(f"Error: {e}")

# # # # Weather function
# # # def weather_command():
# # #     speak("Please tell me the location for weather information.")
# # #     location = listen_command()
# # #     if location:
# # #         get_weather(location)
# # #     else:
# # #         speak("I couldn't hear the location. Please try again.")

# # # # Battery status function
# # # def battery_percentage_query():
# # #     battery = psutil.sensors_battery()
# # #     if battery:
# # #         percent = battery.percent
# # #         print_to_terminal(f"The battery is at {percent}% charge.")
# # #         speak(f"The battery is at {percent}% charge.")
# # #     else:
# # #         speak("Battery information is not available.")

# # # # List running apps function
# # # def list_running_apps():
# # #     speak("Checking running applications.")
# # #     running_apps = []
# # #     for proc in psutil.process_iter(['pid', 'name']):
# # #         try:
# # #             app_name = proc.info['name']
# # #             if app_name:
# # #                 running_apps.append(app_name)
# # #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
# # #             continue

# # #     if running_apps:
# # #         print_to_terminal(f"I found {len(running_apps)} running applications.")
# # #         speak(f"I found {len(running_apps)} running applications.")
# # #         for app in running_apps[:10]:  # Limit output to 10 apps
# # #             print_to_terminal(app)
# # #             speak(app)
# # #     else:
# # #         speak("No running applications found.")

# # # # How are you function
# # # def handle_how_are_you():
# # #     speak("I am absolutely fine, sir. What about you?")
# # #     user_response = listen_command()

# # #     if 'good' in user_response or 'i am fine' in user_response or 'fine' in user_response:
# # #         speak("I'm glad to hear that!")
# # #     else:
# # #         speak("Sorry to hear that. Soon, it will get better!")

# # # # Thread-safe function to append to the terminal
# # # def print_to_terminal(text):
# # #     global terminal_widget
# # #     if terminal_widget:
# # #         terminal_widget.append_to_terminal(text)
# # #     else:
# # #         print(text)  # Fallback if terminal is not yet available

# # # # Main Thread for Task Execution
# # # class MainThread(QtCore.QThread):
# # #     def __init__(self, terminal_widget):
# # #         super(MainThread, self).__init__()
# # #         self.terminal_widget = terminal_widget
# # #         global terminal_widget  # Update global here
# # #         terminal_widget = self.terminal_widget

# # #     def run(self):
# # #         self.TaskExecution()

# # #     def takeCommand(self):
# # #         r = sr.Recognizer()
# # #         with sr.Microphone() as source:
# # #             print_to_terminal("Listening...")
# # #             r.pause_threshold = 1
# # #             audio = r.listen(source, timeout=4)

# # #         try:
# # #             print_to_terminal("Recognizing...")
# # #             query = r.recognize_google(audio, language='en-in')
# # #             print_to_terminal(f"User said: {query}\n")
# # #             return query.lower()
# # #         except Exception as e:
# # #             print_to_terminal("Say that again please...")
# # #             return "None"

# # #     def TaskExecution(self):
# # #         startup()
# # #         wishMe()

# # #         global active  # add this line to declare 'active' as a global variable
# # #         while True:
# # #             if not active:  # Check if NOVA is in sleep mode
# # #                 query = self.takeCommand()
# # #                 if 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
# # #                     wake_up_mode()
# # #                 continue

# # #             query = self.takeCommand()

# # #             if 'tell me about' in query:
# # #                 tell_me_about(query)

# # #             elif 'open' in query:
# # #                 if 'instagram' in query:
# # #                     open_application('Instagram')
# # #                 elif 'youtube' in query:
# # #                     open_application('YouTube')
# # #                 elif 'facebook' in query:
# # #                     open_application('Facebook')
# # #                 else:
# # #                     app_name = query.replace('open ', '').strip()
# # #                     open_application(app_name)

# # #             elif 'close' in query:
# # #                 if 'instagram' in query:
# # #                     close_application('Instagram')
# # #                 elif 'youtube' in query:
# # #                     close_application('YouTube')
# # #                 elif 'facebook' in query:
# # #                     close_application('Facebook')
# # #                 else:
# # #                     app_name = query.replace('close ', '').strip()
# # #                     close_application(app_name)

# # #             elif 'type' in query or 'start typing' in query:
# # #                 speak("Please tell me what should I type. Say 'exit typing' to stop.")
# # #                 while True:
# # #                     text_to_type = listen_command()
# # #                     if 'exit typing' in text_to_type or 'stop typing' in text_to_type:
# # #                         speak("Exiting typing mode.")
# # #                         break
# # #                     elif text_to_type:
# # #                         type_in_app(text_to_type)
# # #                     else:
# # #                         speak("I didn't catch that. Please try again.")

# # #             elif 'save file' in query or 'save this file' in query:
# # #                 speak("Saving the current file.")
# # #                 save_file()

# # #             elif 'send message' in query or 'send a message' in query:
# # #                 speak("Who should I send the message to?")
# # #                 recipient = listen_command()
# # #                 speak("What is the message?")
# # #                 message = listen_command()
# # #                 if recipient and message:
# # #                     send_message(recipient, message)
# # #                 else:
# # #                     speak("I couldn't get the recipient or message. Please try again.")

# # #             elif "calculate" in query or "what is" in query or "multiply" in query or "times" in query:
# # #                 try:
# # #                     question = query.replace("calculate", "").replace("what is", "").replace("multiply", "").replace("times", "").strip()
# # #                     expression = sympify(question)
# # #                     result = expression.evalf()

# # #                     if float(result).is_integer():
# # #                         answer = int(result)
# # #                     else:
# # #                         answer = round(float(result), 6)
# # #                     print_to_terminal(f"The answer is {answer}")
# # #                     speak(f"The answer is {answer}")
# # #                 except SympifyError:
# # #                     speak("I couldn't understand the mathematical expression. Please try again.")
# # #                 except Exception as e:
# # #                     speak("An error occurred while performing the calculation. Please try again.")

# # #             elif 'play' in query:
# # #                 speak('Surfing the browser.... Hold on sir')
# # #                 query = query.replace('play', '')
# # #                 speak('Playing' + query)
# # #                 speak('Enjoy the music')
# # #                 pywhatkit.playonyt(query)

# # #             elif any(keyword in query for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
# # #                                                     'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
# # #                                                     'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
# # #                                                     'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
# # #                 YouTubeAuto(query)

# # #             elif 'joke' in query:
# # #                 speak(pyjokes.get_joke())

# # #             elif 'ip address' in query:
# # #                 ip = get("https://api.ipify.org").text
# # #                 print_to_terminal(f'Your current IP address is {ip}')
# # #                 speak(f'Your current IP address is {ip}')

# # #             elif 'time' in query or 'date' in query:
# # #                 now = datetime.datetime.now()
# # #                 if 'time' in query:
# # #                     current_time = now.strftime("%I:%M %p")
# # #                     print_to_terminal(f"The current time is {current_time}")
# # #                     speak(f"The current time is {current_time}")
# # #                 if 'date' in query:
# # #                     current_date = now.strftime("%A, %B %d, %Y")
# # #                     print_to_terminal(f"Today's date is {current_date}")
# # #                     speak(f"Today's date is {current_date}")

# # #             elif 'where is' in query:
# # #                 Place = query.replace('where is', '').replace('cortana', '').strip()
# # #                 if not Place:
# # #                     speak("I couldn't understand the location. Please try again.")
# # #                 else:
# # #                     print_to_terminal(f"Searching for {Place} on Google Maps.")
# # #                     speak(f"Searching for {Place} on Google Maps.")
# # #                     webbrowser.open(f"https://www.google.com/maps/search/{Place}")

# # #             elif 'current temperature' in query:
# # #                 search = "temperature in my current location"
# # #                 url = f"https://www.google.com/search?q={search}"
# # #                 r = requests.get(url)
# # #                 data = BeautifulSoup(r.text, "html.parser")
# # #                 temp = data.find("div", class_="BNeawe").text
# # #                 print_to_terminal(f'The current temperature in your location is {temp}')
# # #                 speak(f'The current temperature in your location is {temp}')

# # #             elif 'windows' in query or any(keyword in query for keyword in ['home screen', 'minimize', 'minimise', 'maximise', 'maximize','close the window','close the application',
# # #                                                                               'show start', 'open setting','open search', 'screen shot', 'shutdown' , 'restart', 'log out','system sleep'
# # #                                                                               'take a screenshot' , 'restore windows','start recording', 'screenshot', 'stop recording']):
# # #                 WindowsAuto(query)

# # #             elif "internet speed" in query:
# # #                 check_internet_speed()

# # #             elif 'my location' in query:
# # #                 My_Location()

# # #             elif 'show location' in query or 'find location' in query:
# # #                 try:
# # #                     speak("Please tell me the name of the place.")
# # #                     place = listen()
# # #                     if place:
# # #                         print_to_terminal(f"Searching for {place} on Google Maps.")
# # #                         speak(f"Searching for {place} on Google Maps.")
# # #                         GoogleMaps(place)
# # #                     else:
# # #                         speak("I couldn't hear the place name. Please try again.")
# # #                 except Exception as e:
# # #                     print_to_terminal(f"Error occurred: {e}")
# # #                     speak("Sorry, I couldn't fetch the location. Please try again.")

# # #             elif 'open app' in query:
# # #                 speak("Which app would you like me to open?")
# # #                 app_name = listen_command()
# # #                 open_application(app_name)

# # #             elif "hello" in query or "hey" in query:
# # #                 print_to_terminal('Hello sir, Good to see you')
# # #                 print_to_terminal('How may I help You?')

# # #             elif any(keyword in query for keyword in ['turn on bluetooth','turn off bluetooth','bluetooth','increase brigntness', 'decrease brigntness',
# # #                                                      'night light', 'increase volume', 'decrease volume', 'turn on night light','turn on aeroplance mode','turn off aeroplance mode',
# # #                                                      'turn on night light', 'mute system volume','brightness','no sound','sound','check volume level','check current volume level',
# # #                                                      'unmute system volume','maximum volume','set volume to','check brightness level','set brightness to']):
# # #                 process_command(query)

# # #             elif "game" in query:
# # #                 games()

# # #             elif 'search' in query:
# # #                 import wikipedia as googleScrap
# # #                 query = query.replace('jarvis', '').replace('google search', '').replace('google', '').strip()
# # #                 speak('Here are some results...')
# # #                 try:
# # #                     pywhatkit.search(query)
# # #                     result = googleScrap.summary(query, 3)
# # #                     speak(result)
# # #                 except:
# # #                     speak('Data not cached..')

# # #             elif 'sleep mode' in query or 'sleep nova' in query or 'activate sleep mode' in query:
# # #                 sleep_mode()

# # #             elif 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
# # #                 wake_up_mode()

# # #             elif "weather" in query or 'climate' in query:
# # #                 weather_command()

# # #             elif 'screenshot' in query or 'screen shot' in query:
# # #                 try:
# # #                     import pyautogui
# # #                     screenshot = pyautogui.screenshot()
# # #                     screenshot.save("screenshot.jpg")
# # #                     speak("Screenshot taken and saved as 'screenshot.jpg' in the current directory.")
# # #                 except Exception as e:
# # #                     speak(f"Failed to take a screenshot: {e}")

# # #             elif 'read news' in query or 'current news' in query or 'news mode' in query:
# # #                 read_news()

# # #             elif 'space news' in query or 'nasa news' in query or 'astrological news' in query:
# # #                 latest_space_news()

# # #             elif 'scroll up' in query or 'scroll down' in query or 'scroll to top' in query or 'scroll to bottom' in query:
# # #                 perform_scroll_action(query)

# # #             elif any(keyword in query for keyword in ['add new tab','close tab','zoom in','zoom out', 'refresh page','go to history', 'go to bookmarks',
# # #                                                      'switch to next tab', 'switch to previous tab', 'open history', 'open bookmarks',
# # #                                                      'go back', 'go forward','open dev tools','toggle full screen','open private window'
# # #                                                      'go to dev tools','go to private window','next tab','previous tab']):
# # #                 perform_browser_action(query)

# # #             elif 'get to website' in query or 'go to website' in query:
# # #                 website_name = query.lower().replace("get to website", "").replace("go to website", "").strip()
# # #                 open_website(website_name)

# # #             elif "battery status" in query or "battery percentage" in query:
# # #                 battery_percentage_query()

# # #             elif "running apps" in query or "list running apps" in query:
# # #                 list_running_apps()

# # #             elif 'how are you' in query:
# # #                 handle_how_are_you()

# # #             elif 'movie' in query:
# # #                 movies_db = imdb.IMDb()
# # #                 speak("tell me the movie name:")
# # #                 text = listen_command()
# # #                 movies = movies_db.search_movie(text)
# # #                 speak("searching for " + text)
# # #                 speak("i found this")
# # #                 for movie in movies:
# # #                     title = movie["title"]
# # #                     year = movie["year"]
# # #                     speak(f"{title}-{year}")
# # #                     info = movie.getID()
# # #                     movie_info = movies_db.get_movie(info)
# # #                     rating = movie_info["rating"]
# # #                     cast = movie_info["cast"]
# # #                     plot = movie_info.get('plot outline','plot summary not available')
# # #                     speak(f"{title} was released in {year} has imdb ratings of {rating}.the plot summary of movie is {plot}")
# # #                     print_to_terminal(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {cast[0:5]}.the plot summary of movie is {plot}")

# # #             elif 'how developed you' in query or 'who created you' in query or 'who is your master' in query:
# # #                 speak("thiyagu")

# # #             elif "what are you" in query:
# # #                 speak('Hello sir, I am your personalized voice assistant, also known as Jarvis.')

# # #             elif "what are the task's you can perform" in query:
# # #                 speak('google search, play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi speed, provide you news from NASA, calculate, search the map, wikipedia search, and many more')

# # #             elif 'send an email' in query or 'send a mail' in query:
# # #                 speak("on what email address do you want to send sir? Please enter in terminal")
# # #                 receiver_add = input("Email address:")
# # #                 speak("what should be the subject sir?")
# # #                 subject = listen_command().capitalize()
# # #                 speak("what is the message?")
# # #                 message = listen_command().capitalize()
# # #                 if send_email(receiver_add, subject, message):
# # #                     speak("I have sent the email sir")
# # #                     print_to_terminal("I have sent the email sir")
# # #                 else:
# # #                     speak("something went wrong sir")

# # #             elif 'shutup' in query or 'exit program' in query or 'exit' in query:
# # #                 speak("Shutting down. Goodbye, sir.")
# # #                 sys.exit()

# # # # Modified JarvisApp class
# # # class JarvisApp:
# # #     def __init__(self):
# # #         self.core = MainThread()
        
# # #     def start(self):
# # #         """Execute Jarvis with proper sequence"""
# # #         try:
# # #             # Use the full paths to the desktop files
# # #             desktop_1_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_1.py"
# # #             desktop_2_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_2.py"
            
# # #             # Launch desktop_1.py and wait for it to complete initialization
# # #             print_to_terminal("Launching Desktop 1...")
# # #             desktop_1_process = subprocess.Popen(["python", desktop_1_path])
            
# # #             # Allow desktop_1.py time to fully initialize
# # #             time.sleep(15)
            
# # #             # Launch desktop_2.py and wait for it to complete initialization
# # #             print_to_terminal("Launching Desktop 2...")
# # #             desktop_2_process = subprocess.Popen(["python", desktop_2_path])
            
# # #             # Allow desktop_2.py time to fully initialize
# # #             time.sleep(3)
            
# # #             # Start the Main Task Execution
# # #             print_to_terminal("Starting Main Task Execution...")
# # #             self.core.start()
            
# # #             return self.core
            
# # #         except Exception as e:
# # #             print_to_terminal(f"Error in Jarvis execution: {e}")
# # #             sys.exit(1)

# # # # Modified main execution
# # # if __name__ == "__main__":
# # #     try:
# # #         # Create a QApplication instance
# # #         app = QApplication(sys.argv)
        
# # #         # Initialize and start Jarvis
# # #         jarvis = JarvisApp()
# # #         main_thread = jarvis.start()
        
# # #         # Keep the application running
# # #         sys.exit(app.exec())
        
# # #     except Exception as e:
# # #         print_to_terminal(f"Error in main execution: {e}")
# # #         sys.exit(1)


# # from sqlite3 import Date
# # import pyttsx3
# # import speech_recognition as sr
# # import datetime
# # import wikipedia
# # import webbrowser
# # import pywhatkit
# # import pyjokes
# # import os
# # from requests import get
# # import sys
# # import requests
# # from bs4 import BeautifulSoup
# # import subprocess
# # import time
# # import threading
# # import psutil
# # import imdb
# # from PyQt6.QtWidgets import QApplication
# # from PyQt6 import QtCore
# # from sympy import sympify, SympifyError

# # # Import all the required modules and features
# # from YT import YouTubeAuto
# # from WindowsAuto import WindowsAuto
# # from internet_speed_test import check_internet_speed
# # from Features import My_Location, GoogleMaps, listen, Temp, read_news, send_email
# # from on_off import process_command
# # from app_handler import open_application, close_application, type_in_app, save_file, send_message
# # from game import games
# # from utils import get_weather
# # from Nasa import latest_space_news
# # from scrool_system import perform_scroll_action, scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
# # from scrool_system import perform_browser_action
# # from Web_Open import open_website
# # from desktop_1 import InfoDialog, JarvisGUI

# # # Initialize pyttsx3 engine
# # engine = pyttsx3.init('sapi5')
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[0].id)
# # engine.setProperty('rate', 175)

# # # Global active state
# # active = True

# # # Global terminal widget (will be set from outside)
# # terminal_widget = None  # Added global variable

# # def speak(audio):
# #     """Speak the given text."""
# #     engine.say(audio)
# #     engine.runAndWait()

# # def listen_command():
# #     """Listen for a voice command from the user."""
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print_to_terminal("Listening...")
# #         recognizer.adjust_for_ambient_noise(source)
# #         audio = recognizer.listen(source, timeout=4)

# #     try:
# #         command = recognizer.recognize_google(audio, language='en-in').lower()
# #         print_to_terminal(f"You said: {command}\n")
# #         return command
# #     except sr.UnknownValueError:
# #         speak("Sorry, I couldn't understand that.")
# #         return ""
# #     except sr.RequestError:
# #         speak("Sorry, there was an issue with the speech recognition service.")
# #         return ""

# # # Sleep and Wake-up functions
# # def sleep_mode():
# #     global active
# #     active = False
# #     speak("I am going to sleep mode. Say 'Wake up nova' to reactivate me.")

# # def wake_up_mode():
# #     global active
# #     active = True
# #     speak("I am back and ready to assist you.")

# # # Startup message
# # def startup():
# #     print_to_terminal("All systems have been activated.")
# #     speak("All systems have been activated.")

# # # Greet the user based on time
# # def wishMe():
# #     hour = int(datetime.datetime.now().hour)
# #     if hour >= 0 and hour < 12:
# #         print_to_terminal("Good morning sir!")
# #         speak("Good morning sir!")
# #     elif hour >= 12 and hour < 17:
# #         print_to_terminal("Good afternoon sir!")
# #         speak("Good afternoon sir!")
# #     elif hour >= 17 and hour < 21:
# #         print_to_terminal("Good evening sir!")
# #         speak("Good evening sir!")
# #     else:
# #         print_to_terminal("Good night sir!")
# #         speak("Good night sir!")
# #     speak("Please tell me how may I help you.")

# # # Wikipedia search function
# # def tell_me_about(query):
# #     try:
# #         # Removing the trigger phrase
# #         speak('Searching Wikipedia...please wait')
# #         query = query.replace("tell me about", "").strip()
# #         print_to_terminal(f"Query: {query}")

# #         # Searching for the topic
# #         results = wikipedia.summary(query, sentences=2)

# #         # Speaking the result
# #         speak("According to wikipedia...")
# #         print_to_terminal(results)
# #         speak(results)

# #     except wikipedia.DisambiguationError as e:
# #         # Handle multiple results found for the query
# #         speak("There are multiple topics matching your query. Please be more specific.")
# #         print_to_terminal(f"DisambiguationError: {e.options}")

# #     except wikipedia.PageError:
# #         # Handle the case where no results are found
# #         speak("Sorry, I could not find any information on Wikipedia for that topic.")
# #         print_to_terminal("PageError: No results found for the query.")

# #     except Exception as e:
# #         # Catch all other exceptions
# #         speak("Sorry, an error occurred while searching Wikipedia.")
# #         print_to_terminal(f"Error: {e}")

# # # Weather function
# # def weather_command():
# #     speak("Please tell me the location for weather information.")
# #     location = listen_command()
# #     if location:
# #         get_weather(location)
# #     else:
# #         speak("I couldn't hear the location. Please try again.")

# # # Battery status function
# # def battery_percentage_query():
# #     battery = psutil.sensors_battery()
# #     if battery:
# #         percent = battery.percent
# #         print_to_terminal(f"The battery is at {percent}% charge.")
# #         speak(f"The battery is at {percent}% charge.")
# #     else:
# #         speak("Battery information is not available.")

# # # List running apps function
# # def list_running_apps():
# #     speak("Checking running applications.")
# #     running_apps = []
# #     for proc in psutil.process_iter(['pid', 'name']):
# #         try:
# #             app_name = proc.info['name']
# #             if app_name:
# #                 running_apps.append(app_name)
# #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
# #             continue

# #     if running_apps:
# #         print_to_terminal(f"I found {len(running_apps)} running applications.")
# #         speak(f"I found {len(running_apps)} running applications.")
# #         for app in running_apps[:10]:  # Limit output to 10 apps
# #             print_to_terminal(app)
# #             speak(app)
# #     else:
# #         speak("No running applications found.")

# # # How are you function
# # def handle_how_are_you():
# #     speak("I am absolutely fine, sir. What about you?")
# #     user_response = listen_command()

# #     if 'good' in user_response or 'i am fine' in user_response or 'fine' in user_response:
# #         speak("I'm glad to hear that!")
# #     else:
# #         speak("Sorry to hear that. Soon, it will get better!")

# # # Thread-safe function to append to the terminal
# # def print_to_terminal(text):
# #     global terminal_widget
# #     if terminal_widget:
# #         terminal_widget.append_to_terminal(text)
# #     else:
# #         print(text)  # Fallback if terminal is not yet available

# # # Main Thread for Task Execution
# # class MainThread(QtCore.QThread):
# #     def __init__(self, terminal_widget):
# #         super(MainThread, self).__init__()
# #         self.terminal_widget = terminal_widget
# #         # Remove the redundant global declaration

# #     def run(self):
# #         self.TaskExecution()

# #     def takeCommand(self):
# #         r = sr.Recognizer()
# #         with sr.Microphone() as source:
# #             print_to_terminal("Listening...")
# #             r.pause_threshold = 1
# #             audio = r.listen(source, timeout=4)

# #         try:
# #             print_to_terminal("Recognizing...")
# #             query = r.recognize_google(audio, language='en-in')
# #             print_to_terminal(f"User said: {query}\n")
# #             return query.lower()
# #         except Exception as e:
# #             print_to_terminal("Say that again please...")
# #             return "None"

# #     def TaskExecution(self):
# #         global active, terminal_widget
# #         terminal_widget = self.terminal_widget
# #         startup()
# #         wishMe()

# #         while True:
# #             if not active:  # Check if NOVA is in sleep mode
# #                 query = self.takeCommand()
# #                 if 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
# #                     wake_up_mode()
# #                 continue

# #             query = self.takeCommand()

# #             if 'tell me about' in query:
# #                 tell_me_about(query)

# #             elif 'open' in query:
# #                 if 'instagram' in query:
# #                     open_application('Instagram')
# #                 elif 'youtube' in query:
# #                     open_application('YouTube')
# #                 elif 'facebook' in query:
# #                     open_application('Facebook')
# #                 else:
# #                     app_name = query.replace('open ', '').strip()
# #                     open_application(app_name)

# #             elif 'close' in query:
# #                 if 'instagram' in query:
# #                     close_application('Instagram')
# #                 elif 'youtube' in query:
# #                     close_application('YouTube')
# #                 elif 'facebook' in query:
# #                     close_application('Facebook')
# #                 else:
# #                     app_name = query.replace('close ', '').strip()
# #                     close_application(app_name)

# #             elif 'type' in query or 'start typing' in query:
# #                 speak("Please tell me what should I type. Say 'exit typing' to stop.")
# #                 while True:
# #                     text_to_type = listen_command()
# #                     if 'exit typing' in text_to_type or 'stop typing' in text_to_type:
# #                         speak("Exiting typing mode.")
# #                         break
# #                     elif text_to_type:
# #                         type_in_app(text_to_type)
# #                     else:
# #                         speak("I didn't catch that. Please try again.")

# #             elif 'save file' in query or 'save this file' in query:
# #                 speak("Saving the current file.")
# #                 save_file()

# #             elif 'send message' in query or 'send a message' in query:
# #                 speak("Who should I send the message to?")
# #                 recipient = listen_command()
# #                 speak("What is the message?")
# #                 message = listen_command()
# #                 if recipient and message:
# #                     send_message(recipient, message)
# #                 else:
# #                     speak("I couldn't get the recipient or message. Please try again.")

# #             elif "calculate" in query or "what is" in query or "multiply" in query or "times" in query:
# #                 try:
# #                     question = query.replace("calculate", "").replace("what is", "").replace("multiply", "").replace("times", "").strip()
# #                     expression = sympify(question)
# #                     result = expression.evalf()

# #                     if float(result).is_integer():
# #                         answer = int(result)
# #                     else:
# #                         answer = round(float(result), 6)
# #                     print_to_terminal(f"The answer is {answer}")
# #                     speak(f"The answer is {answer}")
# #                 except SympifyError:
# #                     speak("I couldn't understand the mathematical expression. Please try again.")
# #                 except Exception as e:
# #                     speak("An error occurred while performing the calculation. Please try again.")

# #             elif 'play' in query:
# #                 speak('Surfing the browser.... Hold on sir')
# #                 query = query.replace('play', '')
# #                 speak('Playing' + query)
# #                 speak('Enjoy the music')
# #                 pywhatkit.playonyt(query)

# #             elif any(keyword in query for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
# #                                                     'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
# #                                                     'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
# #                                                     'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
# #                 YouTubeAuto(query)

# #             elif 'joke' in query:
# #                 speak(pyjokes.get_joke())

# #             elif 'ip address' in query:
# #                 ip = get("https://api.ipify.org").text
# #                 print_to_terminal(f'Your current IP address is {ip}')
# #                 speak(f'Your current IP address is {ip}')

# #             elif 'time' in query or 'date' in query:
# #                 now = datetime.datetime.now()
# #                 if 'time' in query:
# #                     current_time = now.strftime("%I:%M %p")
# #                     print_to_terminal(f"The current time is {current_time}")
# #                     speak(f"The current time is {current_time}")
# #                 if 'date' in query:
# #                     current_date = now.strftime("%A, %B %d, %Y")
# #                     print_to_terminal(f"Today's date is {current_date}")
# #                     speak(f"Today's date is {current_date}")

# #             elif 'where is' in query:
# #                 Place = query.replace('where is', '').replace('cortana', '').strip()
# #                 if not Place:
# #                     speak("I couldn't understand the location. Please try again.")
# #                 else:
# #                     print_to_terminal(f"Searching for {Place} on Google Maps.")
# #                     speak(f"Searching for {Place} on Google Maps.")
# #                     webbrowser.open(f"https://www.google.com/maps/search/{Place}")

# #             elif 'current temperature' in query:
# #                 search = "temperature in my current location"
# #                 url = f"https://www.google.com/search?q={search}"
# #                 r = requests.get(url)
# #                 data = BeautifulSoup(r.text, "html.parser")
# #                 temp = data.find("div", class_="BNeawe").text
# #                 print_to_terminal(f'The current temperature in your location is {temp}')
# #                 speak(f'The current temperature in your location is {temp}')

# #             elif 'windows' in query or any(keyword in query for keyword in ['home screen', 'minimize', 'minimise', 'maximise', 'maximize','close the window','close the application',
# #                                                                               'show start', 'open setting','open search', 'screen shot', 'shutdown' , 'restart', 'log out','system sleep'
# #                                                                               'take a screenshot' , 'restore windows','start recording', 'screenshot', 'stop recording']):
# #                 WindowsAuto(query)

# #             elif "internet speed" in query:
# #                 check_internet_speed()

# #             elif 'my location' in query:
# #                 My_Location()

# #             elif 'show location' in query or 'find location' in query:
# #                 try:
# #                     speak("Please tell me the name of the place.")
# #                     place = listen()
# #                     if place:
# #                         print_to_terminal(f"Searching for {place} on Google Maps.")
# #                         speak(f"Searching for {place} on Google Maps.")
# #                         GoogleMaps(place)
# #                     else:
# #                         speak("I couldn't hear the place name. Please try again.")
# #                 except Exception as e:
# #                     print_to_terminal(f"Error occurred: {e}")
# #                     speak("Sorry, I couldn't fetch the location. Please try again.")

# #             elif 'open app' in query:
# #                 speak("Which app would you like me to open?")
# #                 app_name = listen_command()
# #                 open_application(app_name)

# #             elif "hello" in query or "hey" in query:
# #                 print_to_terminal('Hello sir, Good to see you')
# #                 print_to_terminal('How may I help You?')

# #             elif any(keyword in query for keyword in ['turn on bluetooth','turn off bluetooth','bluetooth','increase brigntness', 'decrease brigntness',
# #                                                      'night light', 'increase volume', 'decrease volume', 'turn on night light','turn on aeroplance mode','turn off aeroplance mode',
# #                                                      'turn on night light', 'mute system volume','brightness','no sound','sound','check volume level','check current volume level',
# #                                                      'unmute system volume','maximum volume','set volume to','check brightness level','set brightness to']):
# #                 process_command(query)

# #             elif "game" in query:
# #                 games()
                
# #             elif 'search' in query:
# #                 import wikipedia as googleScrap
# #                 query = query.replace('jarvis', '').replace('google search', '').replace('google', '').strip()
# #                 speak('Here are some results...')
# #                 try:
# #                     pywhatkit.search(query)
# #                     result = googleScrap.summary(query, 3)
# #                     speak(result)
# #                 except:
# #                     speak('Data not cached..')

# #             elif 'sleep mode' in query or 'sleep nova' in query or 'activate sleep mode' in query:
# #                 sleep_mode()

# #             elif 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
# #                 wake_up_mode()

# #             elif "weather" in query or 'climate' in query:
# #                 weather_command()

# #             elif 'screenshot' in query or 'screen shot' in query:
# #                 try:
# #                     import pyautogui
# #                     screenshot = pyautogui.screenshot()
# #                     screenshot.save("screenshot.jpg")
# #                     speak("Screenshot taken and saved as 'screenshot.jpg' in the current directory.")
# #                 except Exception as e:
# #                     speak(f"Failed to take a screenshot: {e}")

# #             elif 'read news' in query or 'current news' in query or 'news mode' in query:
# #                 read_news()

# #             elif 'space news' in query or 'nasa news' in query or 'astrological news' in query:
# #                 latest_space_news()

# #             elif 'scroll up' in query or 'scroll down' in query or 'scroll to top' in query or 'scroll to bottom' in query:
# #                 perform_scroll_action(query)

# #             elif any(keyword in query for keyword in ['add new tab','close tab','zoom in','zoom out', 'refresh page','go to history', 'go to bookmarks',
# #                                                      'switch to next tab', 'switch to previous tab', 'open history', 'open bookmarks',
# #                                                      'go back', 'go forward','open dev tools','toggle full screen','open private window'
# #                                                      'go to dev tools','go to private window','next tab','previous tab']):
# #                 perform_browser_action(query)

# #             elif 'get to website' in query or 'go to website' in query:
# #                 website_name = query.lower().replace("get to website", "").replace("go to website", "").strip()
# #                 open_website(website_name)

# #             elif "battery status" in query or "battery percentage" in query:
# #                 battery_percentage_query()

# #             elif "running apps" in query or "list running apps" in query:
# #                 list_running_apps()

# #             elif 'how are you' in query:
# #                 handle_how_are_you()

# #             elif 'movie' in query:
# #                 movies_db = imdb.IMDb()
# #                 speak("tell me the movie name:")
# #                 text = listen_command()
# #                 movies = movies_db.search_movie(text)
# #                 speak("searching for " + text)
# #                 speak("i found this")
# #                 for movie in movies:
# #                     title = movie["title"]
# #                     year = movie["year"]
# #                     speak(f"{title}-{year}")
# #                     info = movie.getID()
# #                     movie_info = movies_db.get_movie(info)
# #                     rating = movie_info["rating"]
# #                     cast = movie_info["cast"]
# #                     plot = movie_info.get('plot outline','plot summary not available')
# #                     speak(f"{title} was released in {year} has imdb ratings of {rating}.the plot summary of movie is {plot}")
# #                     print_to_terminal(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {cast[0:5]}.the plot summary of movie is {plot}")

# #             elif 'how developed you' in query or 'who created you' in query or 'who is your master' in query:
# #                 speak("thiyagu")

# #             elif "what are you" in query:
# #                 speak('Hello sir, I am your personalized voice assistant, also known as Jarvis.')

# #             elif "what are the task's you can perform" in query:
# #                 speak('google search, play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi speed, provide you news from NASA, calculate, search the map, wikipedia search, and many more')

# #             elif 'send an email' in query or 'send a mail' in query:
# #                 speak("on what email address do you want to send sir? Please enter in terminal")
# #                 receiver_add = input("Email address:")
# #                 speak("what should be the subject sir?")
# #                 subject = listen_command().capitalize()
# #                 speak("what is the message?")
# #                 message = listen_command().capitalize()
# #                 if send_email(receiver_add, subject, message):
# #                     speak("I have sent the email sir")
# #                     print_to_terminal("I have sent the email sir")
# #                 else:
# #                     speak("something went wrong sir")

# #             elif 'shutup' in query or 'exit program' in query or 'exit' in query:
# #                 speak("Shutting down. Goodbye, sir.")
# #                 sys.exit()

# # # Modified JarvisApp class
# # class JarvisApp:
# #     def __init__(self):
# #         # Create a QApplication instance
# #         app = QApplication(sys.argv)

# #     def start(self):
# #         """Execute Jarvis with proper sequence"""
# #         try:
# #             # Use the full paths to the desktop files
# #             desktop_1_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_1.py"
# #             desktop_2_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_2.py"

# #             # Launch desktop_1.py and wait for it to complete initialization
# #             print_to_terminal("Launching Desktop 1...")
# #             desktop_1_process = subprocess.Popen(["python", desktop_1_path])

# #             # Allow desktop_1.py time to fully initialize
# #             time.sleep(15)

# #             # Launch desktop_2.py and wait for it to complete initialization
# #             print_to_terminal("Launching Desktop 2...")
# #             desktop_2_process = subprocess.Popen(["python", desktop_2_path])

# #             # Allow desktop_2.py time to fully initialize
# #             time.sleep(3)

# #             # find desktop_2.py to pass terminal widget
# #             app = QApplication.instance()

# #             # Find JarvisOverlayGUI Instance
# #             gui_instances = []
# #             for widget in app.topLevelWidgets():
# #                 from desktop_2 import JarvisOverlayGUI
# #                 if isinstance(widget,JarvisOverlayGUI):
# #                     gui_instances.append(widget)

# #             if gui_instances:
# #                 gui_instance = gui_instances[0]
# #                 terminal_widget = gui_instance.get_terminal_widget()

# #                 # Start the Main Task Execution
# #                 print_to_terminal("Starting Main Task Execution...")
# #                 self.core = MainThread(terminal_widget)
# #                 self.core.start()

# #                 return self.core
# #             else:
# #                 print_to_terminal("JarvisOverlayGUI instance not found!")
# #                 sys.exit(1)

# #         except Exception as e:
# #             print_to_terminal(f"Error in Jarvis execution: {e}")
# #             sys.exit(1)

# # # Modified main execution
# # if __name__ == "__main__":
# #     # Make app here since QApplication can only be made once
# #     app = QApplication(sys.argv)
# #     try:

# #         # Initialize and start Jarvis
# #         jarvis = JarvisApp()
# #         main_thread = jarvis.start()

# #         # Keep the application running
# #         sys.exit(app.exec())

# #     except Exception as e:
# #         print_to_terminal(f"Error in main execution: {e}")
# #         sys.exit(1)



# from sqlite3 import Date
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import pywhatkit
# import pyjokes
# import os
# from requests import get
# import sys
# import requests
# from bs4 import BeautifulSoup
# import subprocess
# import time
# import threading
# import psutil
# import imdb
# from PyQt6.QtWidgets import QApplication
# from PyQt6 import QtCore
# from sympy import sympify, SympifyError

# # Import all the required modules and features
# from YT import YouTubeAuto
# from WindowsAuto import WindowsAuto
# from internet_speed_test import check_internet_speed
# from Features import My_Location, GoogleMaps, listen, Temp, read_news, send_email
# from on_off import process_command
# from app_handler import open_application, close_application, type_in_app, save_file, send_message
# from game import games
# from utils import get_weather
# from Nasa import latest_space_news
# from scrool_system import perform_scroll_action, scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
# from scrool_system import perform_browser_action
# from Web_Open import open_website
# from desktop_1 import InfoDialog, JarvisGUI

# # Initialize pyttsx3 engine
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 175)

# # Global active state
# active = True

# # Global terminal widget (will be set from outside)
# terminal_widget = None  # Added global variable

# def speak(audio):
#     """Speak the given text."""
#     engine.say(audio)
#     engine.runAndWait()

# def listen_command():
#     """Listen for a voice command from the user."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print_to_terminal("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source, timeout=4)

#     try:
#         command = recognizer.recognize_google(audio, language='en-in').lower()
#         print_to_terminal(f"You said: {command}\n")
#         return command
#     except sr.UnknownValueError:
#         speak("Sorry, I couldn't understand that.")
#         return ""
#     except sr.RequestError:
#         speak("Sorry, there was an issue with the speech recognition service.")
#         return ""

# # Sleep and Wake-up functions
# def sleep_mode():
#     global active
#     active = False
#     speak("I am going to sleep mode. Say 'Wake up nova' to reactivate me.")

# def wake_up_mode():
#     global active
#     active = True
#     speak("I am back and ready to assist you.")

# # Startup message
# def startup():
#     print_to_terminal("All systems have been activated.")
#     speak("All systems have been activated.")

# # Greet the user based on time
# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         print_to_terminal("Good morning sir!")
#         speak("Good morning sir!")
#     elif hour >= 12 and hour < 17:
#         print_to_terminal("Good afternoon sir!")
#         speak("Good afternoon sir!")
#     elif hour >= 17 and hour < 21:
#         print_to_terminal("Good evening sir!")
#         speak("Good evening sir!")
#     else:
#         print_to_terminal("Good night sir!")
#         speak("Good night sir!")
#     speak("Please tell me how may I help you.")

# # Wikipedia search function
# def tell_me_about(query):
#     try:
#         # Removing the trigger phrase
#         speak('Searching Wikipedia...please wait')
#         query = query.replace("tell me about", "").strip()
#         print_to_terminal(f"Query: {query}")

#         # Searching for the topic
#         results = wikipedia.summary(query, sentences=2)

#         # Speaking the result
#         speak("According to wikipedia...")
#         print_to_terminal(results)
#         speak(results)

#     except wikipedia.DisambiguationError as e:
#         # Handle multiple results found for the query
#         speak("There are multiple topics matching your query. Please be more specific.")
#         print_to_terminal(f"DisambiguationError: {e.options}")

#     except wikipedia.PageError:
#         # Handle the case where no results are found
#         speak("Sorry, I could not find any information on Wikipedia for that topic.")
#         print_to_terminal("PageError: No results found for the query.")

#     except Exception as e:
#         # Catch all other exceptions
#         speak("Sorry, an error occurred while searching Wikipedia.")
#         print_to_terminal(f"Error: {e}")

# # Weather function
# def weather_command():
#     speak("Please tell me the location for weather information.")
#     location = listen_command()
#     if location:
#         get_weather(location)
#     else:
#         speak("I couldn't hear the location. Please try again.")

# # Battery status function
# def battery_percentage_query():
#     battery = psutil.sensors_battery()
#     if battery:
#         percent = battery.percent
#         print_to_terminal(f"The battery is at {percent}% charge.")
#         speak(f"The battery is at {percent}% charge.")
#     else:
#         speak("Battery information is not available.")

# # List running apps function
# def list_running_apps():
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
#         print_to_terminal(f"I found {len(running_apps)} running applications.")
#         speak(f"I found {len(running_apps)} running applications.")
#         for app in running_apps[:10]:  # Limit output to 10 apps
#             print_to_terminal(app)
#             speak(app)
#     else:
#         speak("No running applications found.")

# # How are you function
# def handle_how_are_you():
#     speak("I am absolutely fine, sir. What about you?")
#     user_response = listen_command()

#     if 'good' in user_response or 'i am fine' in user_response or 'fine' in user_response:
#         speak("I'm glad to hear that!")
#     else:
#         speak("Sorry to hear that. Soon, it will get better!")

# # Thread-safe function to append to the terminal
# def print_to_terminal(text):
#     global terminal_widget
#     if terminal_widget:
#         terminal_widget.append_to_terminal(text)
#     else:
#         print(text)  # Fallback if terminal is not yet available

# # Main Thread for Task Execution
# class MainThread(QtCore.QThread):
#     def __init__(self, terminal_widget):
#         super(MainThread, self).__init__()
#         self.terminal_widget = terminal_widget

#     def run(self):
#         self.TaskExecution()

#     def takeCommand(self):
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print_to_terminal("Listening...")
#             r.pause_threshold = 1
#             audio = r.listen(source, timeout=4)

#         try:
#             print_to_terminal("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             print_to_terminal(f"User said: {query}\n")
#             return query.lower()
#         except Exception as e:
#             print_to_terminal("Say that again please...")
#             return "None"

#     def TaskExecution(self):
#         global active, terminal_widget
#         terminal_widget = self.terminal_widget
#         startup()
#         wishMe()

#         while True:
#             if not active:  # Check if NOVA is in sleep mode
#                 query = self.takeCommand()
#                 if 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
#                     wake_up_mode()
#                 continue

#             query = self.takeCommand()

#             if 'tell me about' in query:
#                 tell_me_about(query)

#             elif 'open' in query:
#                 if 'instagram' in query:
#                     open_application('Instagram')
#                 elif 'youtube' in query:
#                     open_application('YouTube')
#                 elif 'facebook' in query:
#                     open_application('Facebook')
#                 else:
#                     app_name = query.replace('open ', '').strip()
#                     open_application(app_name)

#             elif 'close' in query:
#                 if 'instagram' in query:
#                     close_application('Instagram')
#                 elif 'youtube' in query:
#                     close_application('YouTube')
#                 elif 'facebook' in query:
#                     close_application('Facebook')
#                 else:
#                     app_name = query.replace('close ', '').strip()
#                     close_application(app_name)

#             elif 'type' in query or 'start typing' in query:
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

#             elif 'save file' in query or 'save this file' in query:
#                 speak("Saving the current file.")
#                 save_file()

#             elif 'send message' in query or 'send a message' in query:
#                 speak("Who should I send the message to?")
#                 recipient = listen_command()
#                 speak("What is the message?")
#                 message = listen_command()
#                 if recipient and message:
#                     send_message(recipient, message)
#                 else:
#                     speak("I couldn't get the recipient or message. Please try again.")

#             elif "calculate" in query or "what is" in query or "multiply" in query or "times" in query:
#                 try:
#                     question = query.replace("calculate", "").replace("what is", "").replace("multiply", "").replace("times", "").strip()
#                     expression = sympify(question)
#                     result = expression.evalf()

#                     if float(result).is_integer():
#                         answer = int(result)
#                     else:
#                         answer = round(float(result), 6)
#                     print_to_terminal(f"The answer is {answer}")
#                     speak(f"The answer is {answer}")
#                 except SympifyError:
#                     speak("I couldn't understand the mathematical expression. Please try again.")
#                 except Exception as e:
#                     speak("An error occurred while performing the calculation. Please try again.")

#             elif 'play' in query:
#                 speak('Surfing the browser.... Hold on sir')
#                 query = query.replace('play', '')
#                 speak('Playing' + query)
#                 speak('Enjoy the music')
#                 pywhatkit.playonyt(query)

#             elif any(keyword in query for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
#                                                     'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
#                                                     'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
#                                                     'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
#                 YouTubeAuto(query)

#             elif 'joke' in query:
#                 speak(pyjokes.get_joke())

#             elif 'ip address' in query:
#                 ip = get("https://api.ipify.org").text
#                 print_to_terminal(f'Your current IP address is {ip}')
#                 speak(f'Your current IP address is {ip}')

#             elif 'time' in query or 'date' in query:
#                 now = datetime.datetime.now()
#                 if 'time' in query:
#                     current_time = now.strftime("%I:%M %p")
#                     print_to_terminal(f"The current time is {current_time}")
#                     speak(f"The current time is {current_time}")
#                 if 'date' in query:
#                     current_date = now.strftime("%A, %B %d, %Y")
#                     print_to_terminal(f"Today's date is {current_date}")
#                     speak(f"Today's date is {current_date}")

#             elif 'where is' in query:
#                 Place = query.replace('where is', '').replace('cortana', '').strip()
#                 if not Place:
#                     speak("I couldn't understand the location. Please try again.")
#                 else:
#                     print_to_terminal(f"Searching for {Place} on Google Maps.")
#                     speak(f"Searching for {Place} on Google Maps.")
#                     webbrowser.open(f"https://www.google.com/maps/search/{Place}")

#             elif 'current temperature' in query:
#                 search = "temperature in my current location"
#                 url = f"https://www.google.com/search?q={search}"
#                 r = requests.get(url)
#                 data = BeautifulSoup(r.text, "html.parser")
#                 temp = data.find("div", class_="BNeawe").text
#                 print_to_terminal(f'The current temperature in your location is {temp}')
#                 speak(f'The current temperature in your location is {temp}')

#             elif 'windows' in query or any(keyword in query for keyword in ['home screen', 'minimize', 'minimise', 'maximise', 'maximize','close the window','close the application',
#                                                                               'show start', 'open setting','open search', 'screen shot', 'shutdown' , 'restart', 'log out','system sleep'
#                                                                               'take a screenshot' , 'restore windows','start recording', 'screenshot', 'stop recording']):
#                 WindowsAuto(query)

#             elif "internet speed" in query:
#                 check_internet_speed()

#             elif 'my location' in query:
#                 My_Location()

#             elif 'show location' in query or 'find location' in query:
#                 try:
#                     speak("Please tell me the name of the place.")
#                     place = listen()
#                     if place:
#                         print_to_terminal(f"Searching for {place} on Google Maps.")
#                         speak(f"Searching for {place} on Google Maps.")
#                         GoogleMaps(place)
#                     else:
#                         speak("I couldn't hear the place name. Please try again.")
#                 except Exception as e:
#                     print_to_terminal(f"Error occurred: {e}")
#                     speak("Sorry, I couldn't fetch the location. Please try again.")

#             elif 'open app' in query:
#                 speak("Which app would you like me to open?")
#                 app_name = listen_command()
#                 open_application(app_name)

#             elif "hello" in query or "hey" in query:
#                 print_to_terminal('Hello sir, Good to see you')
#                 print_to_terminal('How may I help You?')

#             elif any(keyword in query for keyword in ['turn on bluetooth','turn off bluetooth','bluetooth','increase brigntness', 'decrease brigntness',
#                                                      'night light', 'increase volume', 'decrease volume', 'turn on night light','turn on aeroplance mode','turn off aeroplance mode',
#                                                      'turn on night light', 'mute system volume','brightness','no sound','sound','check volume level','check current volume level',
#                                                      'unmute system volume','maximum volume','set volume to','check brightness level','set brightness to']):
#                 process_command(query)

#             elif "game" in query:
#                 games()
                
#             elif 'search' in query:
#                 import wikipedia as googleScrap
#                 query = query.replace('jarvis', '').replace('google search', '').replace('google', '').strip()
#                 speak('Here are some results...')
#                 try:
#                     pywhatkit.search(query)
#                     result = googleScrap.summary(query, 3)
#                     speak(result)
#                 except:
#                     speak('Data not cached..')

#             elif 'sleep mode' in query or 'sleep nova' in query or 'activate sleep mode' in query:
#                 sleep_mode()

#             elif 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
#                 wake_up_mode()

#             elif "weather" in query or 'climate' in query:
#                 weather_command()

#             elif 'screenshot' in query or 'screen shot' in query:
#                 try:
#                     import pyautogui
#                     screenshot = pyautogui.screenshot()
#                     screenshot.save("screenshot.jpg")
#                     speak("Screenshot taken and saved as 'screenshot.jpg' in the current directory.")
#                 except Exception as e:
#                     speak(f"Failed to take a screenshot: {e}")

#             elif 'read news' in query or 'current news' in query or 'news mode' in query:
#                 read_news()

#             elif 'space news' in query or 'nasa news' in query or 'astrological news' in query:
#                 latest_space_news()

#             elif 'scroll up' in query or 'scroll down' in query or 'scroll to top' in query or 'scroll to bottom' in query:
#                 perform_scroll_action(query)

#             elif any(keyword in query for keyword in ['add new tab','close tab','zoom in','zoom out', 'refresh page','go to history', 'go to bookmarks',
#                                                      'switch to next tab', 'switch to previous tab', 'open history', 'open bookmarks',
#                                                      'go back', 'go forward','open dev tools','toggle full screen','open private window'
#                                                      'go to dev tools','go to private window','next tab','previous tab']):
#                 perform_browser_action(query)

#             elif 'get to website' in query or 'go to website' in query:
#                 website_name = query.lower().replace("get to website", "").replace("go to website", "").strip()
#                 open_website(website_name)

#             elif "battery status" in query or "battery percentage" in query:
#                 battery_percentage_query()

#             elif "running apps" in query or "list running apps" in query:
#                 list_running_apps()

#             elif 'how are you' in query:
#                 handle_how_are_you()

#             elif 'movie' in query:
#                 movies_db = imdb.IMDb()
#                 speak("tell me the movie name:")
#                 text = listen_command()
#                 movies = movies_db.search_movie(text)
#                 speak("searching for " + text)
#                 speak("i found this")
#                 for movie in movies:
#                     title = movie["title"]
#                     year = movie["year"]
#                     speak(f"{title}-{year}")
#                     info = movie.getID()
#                     movie_info = movies_db.get_movie(info)
#                     rating = movie_info["rating"]
#                     cast = movie_info["cast"]
#                     plot = movie_info.get('plot outline','plot summary not available')
#                     speak(f"{title} was released in {year} has imdb ratings of {rating}.the plot summary of movie is {plot}")
#                     print_to_terminal(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {cast[0:5]}.the plot summary of movie is {plot}")

#             elif 'how developed you' in query or 'who created you' in query or 'who is your master' in query:
#                 speak("thiyagu")

#             elif "what are you" in query:
#                 speak('Hello sir, I am your personalized voice assistant, also known as Jarvis.')

#             elif "what are the task's you can perform" in query:
#                 speak('google search, play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi speed, provide you news from NASA, calculate, search the map, wikipedia search, and many more')

#             elif 'send an email' in query or 'send a mail' in query:
#                 speak("on what email address do you want to send sir? Please enter in terminal")
#                 receiver_add = input("Email address:")
#                 speak("what should be the subject sir?")
#                 subject = listen_command().capitalize()
#                 speak("what is the message?")
#                 message = listen_command().capitalize()
#                 if send_email(receiver_add, subject, message):
#                     speak("I have sent the email sir")
#                     print_to_terminal("I have sent the email sir")
#                 else:
#                     speak("something went wrong sir")

#             elif 'shutup' in query or 'exit program' in query or 'exit' in query:
#                 speak("Shutting down. Goodbye, sir.")
#                 sys.exit()

# # Modified JarvisApp class
# class JarvisApp:
#     def start(self):
#         """Execute Jarvis with proper sequence"""
#         try:
#             # Use the full paths to the desktop files
#             desktop_1_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_1.py"
#             desktop_2_path = "D:\\FINAL_YEAR_PROJECT\\voice-assistance\\Jarvis-ai-main\\desktop_2.py"

#             # Launch desktop_1.py and wait for it to complete initialization
#             print_to_terminal("Launching Desktop 1...")
#             desktop_1_process = subprocess.Popen(["python", desktop_1_path])

#             # Allow desktop_1.py time to fully initialize
#             time.sleep(15)

#             # Launch desktop_2.py and wait for it to complete initialization
#             print_to_terminal("Launching Desktop 2...")
#             desktop_2_process = subprocess.Popen(["python", desktop_2_path])

#             # Allow desktop_2.py time to fully initialize
#             time.sleep(3)

#             # find desktop_2.py to pass terminal widget
#             app = QApplication.instance()

#             # Find JarvisOverlayGUI Instance
#             gui_instances = []
#             for widget in app.topLevelWidgets():
#                 from desktop_2 import JarvisOverlayGUI
#                 if isinstance(widget,JarvisOverlayGUI):
#                     gui_instances.append(widget)

#             if gui_instances:
#                 gui_instance = gui_instances[0]
#                 terminal_widget = gui_instance.get_terminal_widget()

#                 # Start the Main Task Execution
#                 print_to_terminal("Starting Main Task Execution...")
#                 self.core = MainThread(terminal_widget)
#                 self.core.start()

#                 return self.core
#             else:
#                 print_to_terminal("JarvisOverlayGUI instance not found!")
#                 sys.exit(1)

#         except Exception as e:
#             print_to_terminal(f"Error in Jarvis execution: {e}")
#             sys.exit(1)

# # Modified main execution
# if __name__ == "__main__":
#     # Make app here since QApplication can only be made once
#     app = QApplication(sys.argv)
#     try:

#         # Initialize and start Jarvis
#         jarvis = JarvisApp()
#         main_thread = jarvis.start()

#         # Keep the application running
#         sys.exit(app.exec())

#     except Exception as e:
#         print_to_terminal(f"Error in main execution: {e}")
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
from game import games
from utils import get_weather
from Nasa import latest_space_news
from scrool_system import perform_scroll_action, scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
from scrool_system import perform_browser_action
from desktop_1 import InfoDialog, JarvisGUI

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

# Global active state
active = True

# Language settings
TAMIL = 'ta-IN'
ENGLISH = 'en-IN'
current_language = ENGLISH  # Default language

def speak(audio, language=current_language):
    """Speak the given text in the specified language."""
    engine.setProperty('voice', voices[0].id)  # Reset voice property
    if language == TAMIL:
        engine.setProperty('voice', voices[1].id)  # Assuming Tamil voice is at index 1
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()

def listen_command(language=current_language):
    """Listen for a voice command from the user in the specified language."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=4)
    
    try:
        command = recognizer.recognize_google(audio, language=language).lower()
        print(f"You said: {command}\n")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.", language=language)
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.", language=language)
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
def tell_me_about(query, language=ENGLISH):
    try:
        # Removing the trigger phrase
        speak('Searching Wikipedia...please wait', language=language)
        query = query.replace("tell me about", "").strip()
        print(f"Query: {query}")

        # Searching for the topic
        results = wikipedia.summary(query, sentences=2)
        
        # Speaking the result
        speak("According to wikipedia...", language=language)
        print(results)
        speak(results, language=language)

    except wikipedia.DisambiguationError as e:
        # Handle multiple results found for the query
        speak("There are multiple topics matching your query. Please be more specific.", language=language)
        print(f"DisambiguationError: {e.options}")

    except wikipedia.PageError:
        # Handle the case where no results are found
        speak("Sorry, I could not find any information on Wikipedia for that topic.", language=language)
        print("PageError: No results found for the query.")

    except Exception as e:
        # Catch all other exceptions
        speak("Sorry, an error occurred while searching Wikipedia.", language=language)
        print(f"Error: {e}")

# Weather function
def weather_command(language=ENGLISH):
    speak("Please tell me the location for weather information.", language=language)
    location = listen_command(language=language)
    if location:
        get_weather(location)
    else:
        speak("I couldn't hear the location. Please try again.", language=language)

# Battery status function
def battery_percentage_query(language=ENGLISH):
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"The battery is at {percent}% charge.", language=language)
    else:
        speak("Battery information is not available.", language=language)

# List running apps function
def list_running_apps(language=ENGLISH):
    speak("Checking running applications.", language=language)
    running_apps = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            app_name = proc.info['name']
            if app_name:
                running_apps.append(app_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if running_apps:
        speak(f"I found {len(running_apps)} running applications.", language=language)
        for app in running_apps[:10]:  # Limit output to 10 apps
            speak(app, language=language)
    else:
        speak("No running applications found.", language=language)

# How are you function
def handle_how_are_you(language=ENGLISH):
    speak("I am absolutely fine, sir. What about you?", language=language)
    user_response = listen_command(language=language)
    
    if 'good' in user_response or 'i am fine' in user_response or 'fine' in user_response:
        speak("I'm glad to hear that!", language=language)
    else:
        speak("Sorry to hear that. Soon, it will get better!", language=language)

# Main Thread for Task Execution
class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self, language=ENGLISH):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=4)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language=language)
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

    def TaskExecution(self):
        global active
        global current_language  # Use the global variable

        startup()
        wishMe()
        
        while True:
            if not active:  # Check if NOVA is in sleep mode
                query = self.takeCommand()
                if 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
                    wake_up_mode()
                continue

            query = self.takeCommand(language=current_language)

            # Language Switching
            if 'tamil mode' in query or 'tamil language' in query:
                current_language = TAMIL
                speak("Tamil mode activated.", language=ENGLISH)
                continue
            elif 'english mode' in query or 'english language' in query:
                current_language = ENGLISH
                speak("English mode activated.", language=ENGLISH)
                continue
            
            if 'tell me about' in query:
                tell_me_about(query, language=current_language)

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
                    speak(f"The answer is {answer}", language=current_language)
                except SympifyError:
                    speak("I couldn't understand the mathematical expression. Please try again.", language=current_language)
                except Exception as e:
                    speak("An error occurred while performing the calculation. Please try again.", language=current_language)

            elif 'play' in query:
                speak('Surfing the browser.... Hold on sir', language=current_language)
                query = query.replace('play', '')
                speak('Playing' + query, language=current_language)
                speak('Enjoy the music', language=current_language)
                pywhatkit.playonyt(query)

            elif any(keyword in query for keyword in ['pause','pass','unpass','resume', 'un pass','unpause','un pause',
                                                    'mute', 'unmute', 'next', 'previous', 'full screen','volume down','volumedown',
                                                    'back', 'skip', 'fullscreen', 'film screen','volume up','volumeup',
                                                    'filmscreen', 'decrease youtube volume', 'increase youtube volume', 'max volume']):
                YouTubeAuto(query)

            elif 'joke' in query:
                speak(pyjokes.get_joke(), language=current_language)

            elif 'ip address' in query:
                ip = get("https://api.ipify.org").text
                speak(f'Your current IP address is {ip}', language=current_language)

            elif 'time' in query or 'date' in query:
                now = datetime.datetime.now()
                if 'time' in query:
                    current_time = now.strftime("%I:%M %p")
                    speak(f"The current time is {current_time}", language=current_language)
                if 'date' in query:
                    current_date = now.strftime("%A, %B %d, %Y")
                    speak(f"Today's date is {current_date}", language=current_language)

            elif 'where is' in query:
                Place = query.replace('where is', '').replace('cortana', '').strip()
                if not Place:
                    speak("I couldn't understand the location. Please try again.", language=current_language)
                else:
                    speak(f"Searching for {Place} on Google Maps.", language=current_language)
                    webbrowser.open(f"https://www.google.com/maps/search/{Place}")

            elif 'current temperature' in query:
                search = "temperature in my current location"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f'The current temperature in your location is {temp}', language=current_language)

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
                    speak("Please tell me the name of the place.", language=current_language)
                    place = listen()
                    if place:
                        speak(f"Searching for {place} on Google Maps.", language=current_language)
                        GoogleMaps(place)
                    else:
                        speak("I couldn't hear the place name. Please try again.", language=current_language)
                except Exception as e:
                    print(f"Error occurred: {e}")
                    speak("Sorry, I couldn't fetch the location. Please try again.", language=current_language)

          

            elif "hello" in query or "hey" in query:
                speak('Hello sir, Good to see you', language=current_language)
                speak('How may I help You?', language=current_language)

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
                speak('Here are some results...', language=current_language)
                try:
                    pywhatkit.search(query)
                    result = googleScrap.summary(query, 3)
                    speak(result, language=current_language)
                except:
                    speak('Data not cached..', language=current_language)

            elif 'sleep mode' in query or 'sleep nova' in query or 'activate sleep mode' in query:
                sleep_mode()

            elif 'wake up' in query or 'wakeup' in query or 'activate wake up mode' in query:
                wake_up_mode()

            elif "weather" in query or 'climate' in query:
                weather_command(language=current_language)

            elif 'screenshot' in query or 'screen shot' in query:
                try:
                    import pyautogui
                    screenshot = pyautogui.screenshot()
                    screenshot.save("screenshot.jpg")
                    speak("Screenshot taken and saved as 'screenshot.jpg' in the current directory.", language=current_language)
                except Exception as e:
                    speak(f"Failed to take a screenshot: {e}", language=current_language)

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

            elif "battery status" in query or "battery percentage" in query:
                battery_percentage_query(language=current_language)

            elif "running apps" in query or "list running apps" in query:
                list_running_apps(language=current_language)

            elif 'how are you' in query:
                handle_how_are_you(language=current_language)

            elif 'movie' in query:
                movies_db = imdb.IMDb()
                speak("tell me the movie name:", language=current_language)
                text = listen_command(language=current_language)
                movies = movies_db.search_movie(text)
                speak("searching for " + text, language=current_language)
                speak("i found this", language=current_language)
                for movie in movies:
                    title = movie["title"]
                    year = movie["year"]
                    speak(f"{title}-{year}", language=current_language)
                    info = movie.getID()
                    movie_info = movies_db.get_movie(info)
                    rating = movie_info["rating"]
                    cast = movie_info["cast"]
                    plot = movie_info.get('plot outline','plot summary not available')
                    speak(f"{title} was released in {year} has imdb ratings of {rating}.the plot summary of movie is {plot}", language=current_language)
                    print(f"{title} was released in {year} has imdb ratings of {rating}. it has a cast of {cast[0:5]}.the plot summary of movie is {plot}")

            elif 'how developed you' in query or 'who created you' in query or 'who is your master' in query:
                speak("thiyagu", language=current_language)

            elif "what are you" in query:
                speak('Hello sir, I am your personalized voice assistant, also known as Jarvis.', language=current_language)

            elif "what are the task's you can perform" in query:
                speak('google search, play videos on youtube, search your location, check the current temperature, check your ip address, check your Wi-fi speed, provide you news from NASA, calculate, search the map, wikipedia search, and many more', language=current_language)

            elif 'send an email' in query or 'send a mail' in query:
                speak("on what email address do you want to send sir? Please enter in terminal", language=current_language)
                receiver_add = input("Email address:")
                speak("what should be the subject sir?", language=current_language)
                subject = listen_command(language=current_language).capitalize()
                speak("what is the message?", language=current_language)
                message = listen_command(language=current_language).capitalize()
                if send_email(receiver_add, subject, message):
                    speak("I have sent the email sir", language=current_language)
                    print("I have sent the email sir")
                else:
                    speak("something went wrong sir", language=current_language)

            elif 'shutup' in query or 'exit program' in query or 'exit' in query:
                speak("Shutting down. Goodbye, sir.", language=current_language)
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







        # def terminalprint(self,text):
        #     self.JarvisOverlayGUI.interaction_print_terminal.appendPlainText(text)

        # def terminalprint(self,text):
        #         self.terminaltext.appendPlainText(text)

        # def updategifs(self):
        #     if state == 'speaking':
        #         self.



            # # Image generation request handling
            # elif any(phrase in query_lower for phrase in ["generate image", "create image", "draw", "picture of", "show me", "visualize"]):
            #     speak("I'll generate that image for you, sir.")
            #     result = process_query(query)
            #     speak("Image has been generated and saved.")

            # # Code generation request handling
            # elif any(phrase in query_lower for phrase in ["write code", "generate code", "code for", "program", "function", "script", "class"]):
            #     speak("I'll write that code for you, sir.")
            #     result = process_query(query)
            #     speak("Code has been generated and saved.")

            # # Default to text response from Gemini for all other queries
            # else:
            #     speak("Let me process that for you.")
            #     result = process_query(query)
            #     # Extract just the text part without token info for speaking
            #     if isinstance(result, str) and "\n\n(Tokens Used:" in result:
            #         text_part = result.split("\n\n(Tokens Used:")[0]
            #         speak(text_part)
            #     else:
            #         speak(result)
            # else:
            #     speak("I am not programmed to answer that. Let me check online...")
            #     response = query_google_gemini(query)
            #     speak(response)
            #     print(response)
