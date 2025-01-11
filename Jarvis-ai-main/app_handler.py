# import speech_recognition as sr
# import os
# import webbrowser
# import pyttsx3

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()

# def speak(text):
#     """Speak the given text."""
#     engine.say(text)
#     engine.runAndWait()

# def open_app(command):
#     """Open the app or fallback to browser if app is not found."""
#     if "kmplayer" in command:
#         speak("Opening KMPlayer")
#         try:
#             os.system("start kmplayer")  # For Windows, adjust for your OS if needed
#         except:
#             webbrowser.open("https://www.kmplayer.com")  # Fallback to KMPlayer website
#     elif "settings" in command:
#         speak("Opening Settings")
#         try:
#             os.system("start ms-settings:")  # For Windows
#         except:
#             webbrowser.open("https://www.microsoft.com/en-us/windows/get-windows-10")  # Fallback to Windows settings page

#     elif "speed.exe" in command:
#         speak("Opening need for speed game")
#         try:
#             os.system("")  # For Windows
#         except:
#             webbrowser.open("https://www.google.com/search?q=notepad")  # Fallback to search for Notepad



#     elif "notepad" in command:
#         speak("Opening Notepad")
#         try:
#             os.system("start notepad")  # For Windows
#         except:
#             webbrowser.open("https://www.google.com/search?q=notepad")  # Fallback to search for Notepad
#     else:
#         speak(f"I didn't recognize the app, searching for {command}")
#         print("App not recognized! Searching in browser...")
#         webbrowser.open(f"https://www.google.com/search?q={command}")
        
  
# # Recognize Voice Command
# recognizer = sr.Recognizer()
# with sr.Microphone() as source:
#     speak("I am listening for your command.")
#     print("Listening...")
#     audio = recognizer.listen(source)
#     try:
#         command = recognizer.recognize_google(audio).lower()
#         speak(f"You said {command}")
#         open_app(command)
#     except sr.UnknownValueError:
#         speak("Sorry, I couldn't understand that.")
#         print("Sorry, I couldn't understand that.")

#*********************************************i am using this before the close the app feature working*************************************


#///////////////////////////////////////////// open using path/////////////////

# import os
# import webbrowser
# import pyttsx3
# import pyautogui

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()

# def speak(text):
#     """Speak the given text."""
#     engine.say(text)
#     engine.runAndWait()

# def open_kmplayer():
#     """Open KMPlayer."""
#     speak("Opening KMPlayer sir.")
#     try:
#         os.startfile("C:\\Program Files\\KMPlayer 64X\\KMPlayer64.exe")
#     except:
#         webbrowser.open("https://www.kmplayer.com")

# def open_settings():
#     """Open system settings."""
#     speak("Opening Settings sir.")
#     try:
#         os.system("start ms-settings:")
#     except:
#         webbrowser.open("https://www.microsoft.com/en-us/windows/get-windows-10")

# def open_notepad():
#     """Open Notepad."""
#     speak("Opening Notepad sir.")
#     try:
#         os.startfile("C:\\Windows\\notepad.exe")
#     except:
#         webbrowser.open("https://www.google.com/search?q=notepad")

# def open_notepad():
#     """Open Notepad."""
#     speak("Opening Notepad sir.")
#     os.startfile("C:\\Windows\\notepad.exe")
#     # while True:
#     #     notepadQuery=command().lower()
#     #     if "paste" min notepadQuery:
#     #         pyautogui.hotkey('ctrl','v')
#     #         speak("done sir!...")
#     #     elif "save this file" in notepadQuery:
#     #         pyautogui.hotkey('ctrl','s')
#     #         speak("sir,please specify a name for this file")
#     #         notepadSavingQuery=command()
#     #         pyautogui.write(notepadSavingQuery)
#     #         pyaytogui.press('enter')
#     #     elif 'type' in self.query:
#     #             speak("please tell me what should i write")
#     #             while True:
#     #                 writeInNotepad=command()
#     #                 if writeInNotepad=='exit typing':
#     #                     speak("Done sir")
#     #                 else:
#     #                     pyautogui.write(writeInNotepad)
#     #     elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
#     #         speak("quiting notepad sir....")
#     #         pyautogui.hotkey('ctrl','w')
#     #         break



# def open_instagram():
#     """Open Instagram."""
#     speak("Opening Instagram sir.")
#     webbrowser.open("https://www.instagram.com")

# def open_facebook():
#     """Open Facebook."""
#     speak("Opening Facebook sir.")
#     webbrowser.open("https://www.facebook.com")

# def open_whatsapp():
#     """Open WhatsApp."""
#     speak("Opening WhatsApp sir.")
#     try:
#         os.startfile("")
#     except:
#         webbrowser.open("https://web.whatsapp.com")

# def open_youtube():
#     """Open YouTube."""
#     speak("Opening YouTube sir.")
#     webbrowser.open("https://www.youtube.com")

# def open_gmail():
#     """Open Gmail."""
#     speak("Opening Gmail sir.")
#     webbrowser.open("https://mail.google.com")

# def open_spotify():
#     """Open Spotify."""
#     speak("Opening Spotify sir.")
#     webbrowser.open("https://open.spotify.com")

# def open_twitter():
#     """Open Twitter."""
#     speak("Opening Twitter sir.")
#     webbrowser.open("https://twitter.com")

# def open_discord():
#     """Open Discord."""
#     speak("Opening Discord sir.")
#     webbrowser.open("https://discord.com")

# def open_chrome():
#     """Open chrome."""
#     speak("Opening google chrome sir.")
#     try:
#         os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
#     except:
#         webbrowser.open("https://www.google.com/chrome/index.html")


# #************************* youtube jarvis code with close feature**********************


# # def open_google():
# #     """Open chrome."""
# #     speak("Opening google chrome sir.")
# #     os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
# #     while True:
# #         chromeQuery=command().lower()
# #         if "search" in chromeQuery:
# #             youtubeQuery=chromeQuery
# #             youtubeQuery=youtubeQuery.replace("search","")
# #             pyautogui.write(youtubeQuery)
# #             pyautogui.press('enter')
# #             speak('searching....')
# #         elif "close chrome" in chromeQuery or "exit chrome" in chromeQuery or "exit google":
# #             pyautogui.hotkey('ctrl','w')
# #             speak("closing google chrome sir....")
# #             break
  


# def open_explorer():
#     """Open explorer."""
#     speak("Opening explorer sir.")
#     os.startfile("C:\\Windows\\explorer.exe")



# def open_paint():
#     """Open paint."""
#     speak("Opening paint sir.")
#     os.startfile()
    
# def open_app(command):
#     """Open apps based on the given command."""
#     if "kmplayer" in command:
#         open_kmplayer()
#     elif "settings" in command:
#         open_settings()
#     elif "notepad" in command:
#         open_notepad()
#         while True:
#             notepadQuery=command().lower()
#             if "paste" in notepadQuery:
#                 pyautogui.hotkey('ctrl','v')
#                 speak("done sir!...")
#             elif "save this file" in notepadQuery:
#                 pyautogui.hotkey('ctrl','s')
#                 speak("sir,please specify a name for this file")
#                 notepadSavingQuery=command()
#                 pyautogui.write(notepadSavingQuery)
#                 pyautogui.press('enter')
#             elif 'type' in notepadQuery:
#                 speak("please tell me what should i write")
#                 while True:
#                     writeInNotepad=command()
#                     if writeInNotepad=='exit typing':
#                         speak("Done sir")
#                     else:
#                         pyautogui.write(writeInNotepad)
#             elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
#                 speak("quiting notepad sir....")
#                 pyautogui.hotkey('ctrl','w')
#                 break

#     elif "instagram" in command:
#         open_instagram()
#     elif "facebook" in command:
#         open_facebook()
#     elif "whatsapp" in command:
#         open_whatsapp()
#     elif "youtube" in command:
#         open_youtube()
#     elif "gmail" in command:
#         open_gmail()
#     elif "spotify" in command:
#         open_spotify()
#     elif "twitter" in command:
#         open_twitter()
#     elif "discord" in command:
#         open_discord()
#     elif "chrome" in command:
#         open_chrome()
#     # elif "google" in command:
#     #     open_google()
#     elif "file explorer" in command:
#         open_explorer()
#     else:
#         speak("Sorry, I couldn't recognize that app.")





#********************************************   end has closing and opening fearure  **************************************************


# import os
# import webbrowser
# import pyttsx3
# import psutil

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()

# def speak(text):
#     """Speak the given text."""
#     engine.say(text)
#     engine.runAndWait()

# def open_application(app_name, app_path=None, fallback_url=None):
#     """Open an application or a fallback URL."""
#     speak(f"Opening {app_name} sir.")
#     try:
#         if app_path:
#             os.startfile(app_path)
#         elif fallback_url:
#             webbrowser.open(fallback_url)
#         else:
#             speak(f"Unable to open {app_name}. No path or URL provided.")
#     except Exception as e:
#         if fallback_url:
#             speak(f"{app_name} not found. Opening fallback URL.")
#             webbrowser.open(fallback_url)
#         else:
#             speak(f"Failed to open {app_name}.")
#             print(f"Error: {e}")

# def close_application(app_name):
#     """Close the specified application."""
#     speak(f"Closing {app_name} sir.")
#     try:
#         for proc in psutil.process_iter(attrs=['name']):
#             if app_name.lower() in proc.info['name'].lower():
#                 proc.kill()
#                 speak(f"{app_name} has been closed.")
#                 return
#         speak(f"{app_name} is not running.")
#     except Exception as e:
#         speak("Unable to close the application.")
#         print(f"Error: {e}")

# # Application functions
# def open_kmplayer():
#     open_application("KMPlayer", "C:\\Program Files\\KMPlayer 64X\\KMPlayer64.exe", "https://www.kmplayer.com")

# def open_settings():
#     open_application("Settings", None, None)
#     os.system("start ms-settings:")

# def open_notepad():
#     open_application("Notepad", "C:\\Windows\\notepad.exe")

# def open_instagram():
#     open_application("Instagram", None, "https://www.instagram.com")

# def open_facebook():
#     open_application("Facebook", None, "https://www.facebook.com")

# def open_whatsapp():
#     open_application("WhatsApp", None, "https://web.whatsapp.com")

# def open_youtube():
#     open_application("YouTube", None, "https://www.youtube.com")

# def open_gmail():
#     open_application("Gmail", None, "https://mail.google.com")

# def open_spotify():
#     open_application("Spotify", None, "https://open.spotify.com")

# def open_twitter():
#     open_application("Twitter", None, "https://twitter.com")

# def open_discord():
#     open_application("Discord", None, "https://discord.com")

# def open_chrome():
#     open_application("Google Chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://www.google.com/chrome/index.html")

# def open_paint():
#     open_application("Paint", "C:\\Windows\\System32\\mspaint.exe")

# def open_explorer():
#     open_application("File Explorer", None)
#     os.system("explorer")

# def call_function(command):
#     """Call the appropriate function based on the command."""
#     command = command.lower()

#     if "open kmplayer" in command:
#         open_kmplayer()
#     elif "open settings" in command:
#         open_settings()
#     elif "open notepad" in command:
#         open_notepad()
#     elif "open instagram" in command:
#         open_instagram()
#     elif "open facebook" in command:
#         open_facebook()
#     elif "open whatsapp" in command:
#         open_whatsapp()
#     elif "open youtube" in command:
#         open_youtube()
#     elif "open gmail" in command:
#         open_gmail()
#     elif "open spotify" in command:
#         open_spotify()
#     elif "open twitter" in command:
#         open_twitter()
#     elif "open discord" in command:
#         open_discord()
#     elif "open chrome" in command:
#         open_chrome()
#     elif "open paint" in command:
#         open_paint()
#     elif "open explorer" in command:
#         open_explorer()
#     elif "close" in command:
#         # Extract application name after 'close' in the command
#         app_name = command.replace("close", "").strip()
#         close_application(app_name)
#     else:
#         speak("Command not recognized. Please try again.")

#//////////////////////////////////////////////////writing and above function added/////////////////////////////

# import os
# import webbrowser
# import pyttsx3
# import psutil
# import pyautogui
# import time
# import speech_recognition as sr

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()
# recognizer = sr.Recognizer()

# def speak(text):
#     """Speak the given text."""
#     engine.say(text)
#     engine.runAndWait()

# def listen_command():
#     """Capture voice command from the user."""
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         try:
#             audio = recognizer.listen(source)
#             command = recognizer.recognize_google(audio)
#             return command.lower()
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't catch that. Please repeat.")
#             return ""
#         except sr.RequestError:
#             speak("Sorry, I'm having trouble connecting. Please try again later.")
#             return ""

# def open_application(app_name, app_path=None, fallback_url=None):
#     """Open an application or a fallback URL."""
#     speak(f"Opening {app_name} sir.")
#     try:
#         if app_path:
#             os.startfile(app_path)
#         elif fallback_url:
#             webbrowser.open(fallback_url)
#         else:
#             speak(f"Unable to open {app_name}. No path or URL provided.")
#     except Exception as e:
#         if fallback_url:
#             speak(f"{app_name} not found. Opening fallback URL.")
#             webbrowser.open(fallback_url)
#         else:
#             speak(f"Failed to open {app_name}.")
#             print(f"Error: {e}")

# def close_application(app_name):
#     """Close the specified application."""
#     speak(f"Closing {app_name} sir.")
#     try:
#         for proc in psutil.process_iter(attrs=['name']):
#             if app_name.lower() in proc.info['name'].lower():
#                 proc.kill()
#                 speak(f"{app_name} has been closed.")
#                 return
#         speak(f"{app_name} is not running.")
#     except Exception as e:
#         speak("Unable to close the application.")
#         print(f"Error: {e}")

# def type_in_app():
#     """Handle typing in the currently open application."""
#     speak("I am ready to type. Please start speaking.")
#     while True:
#         command = listen_command()
#         if "exit typing" in command:
#             speak("Exiting typing mode.")
#             break
#         else:
#             pyautogui.write(command)

# def save_file():
#     """Handle saving a file with a user-specified name."""
#     speak("Please specify a name for the file.")
#     file_name = listen_command()
#     if file_name:
#         pyautogui.hotkey('ctrl', 's')
#         time.sleep(1)  # Give some time for the save dialog to appear
#         pyautogui.write(file_name)
#         pyautogui.press('enter')
#         speak(f"File has been saved as {file_name}.")
#     else:
#         speak("File name not provided. Unable to save the file.")

# def send_message():
#     """Handle typing and sending a message in social media apps."""
#     speak("I am ready to type your message. Please start speaking.")
#     while True:
#         command = listen_command()
#         if "exit typing" in command:
#             speak("Exiting typing mode and sending the message.")
#             pyautogui.press('enter')
#             break
#         else:
#             pyautogui.write(command)

# # Application functions
# def open_kmplayer():
#     open_application("KMPlayer", "C:\\Program Files\\KMPlayer 64X\\KMPlayer64.exe", "https://www.kmplayer.com")

# def open_settings():
#     open_application("Settings", None, None)
#     os.system("start ms-settings:")

# def open_notepad():
#     open_application("Notepad", "C:\\Windows\\notepad.exe")
#     type_in_app()
#     save_file()

# def open_paint():
#     open_application("Paint", "C:\\Windows\\System32\\mspaint.exe")
#     type_in_app()
#     save_file()

# def open_instagram():
#     open_application("Instagram", None, "https://www.instagram.com")
#     send_message()

# def open_facebook():
#     open_application("Facebook", None, "https://www.facebook.com")
#     send_message()

# def open_whatsapp():
#     open_application("WhatsApp", None, "https://web.whatsapp.com")
#     send_message()

# def open_youtube():
#     open_application("YouTube", None, "https://www.youtube.com")

# def open_gmail():
#     open_application("Gmail", None, "https://mail.google.com")

# def open_spotify():
#     open_application("Spotify", None, "https://open.spotify.com")

# def open_twitter():
#     open_application("Twitter", None, "https://twitter.com")
#     send_message()

# def open_discord():
#     open_application("Discord", None, "https://discord.com")
#     send_message()

# def open_chrome():
#     open_application("Google Chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://www.google.com/chrome/index.html")

# def open_explorer():
#     open_application("File Explorer", None)
#     os.system("explorer")

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# import os
# import webbrowser
# import pyttsx3                               # correcting this
# import psutil
# import pyautogui
# import time
# import platform
# import logging
# import speech_recognition as sr

# # Initialize logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()
# recognizer = sr.Recognizer()

# def speak(text):
#     """Speak the given text."""
#     logging.info(f"Speaking: {text}")
#     engine.say(text)
#     engine.runAndWait()

# def listen_command():
#     """Capture voice command from the user."""
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         speak("Listening for your command...")
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             command = recognizer.recognize_google(audio)
#             logging.info(f"Command received: {command}")
#             return command.lower()
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't catch that. Please repeat.")
#             return ""
#         except sr.RequestError:
#             speak("Sorry, I'm having trouble connecting. Please try again later.")
#             return ""
#         except Exception as e:
#             speak("An error occurred while capturing your command.")
#             logging.error(f"Error in listen_command: {e}")
#             return ""

# def open_application(app_name, app_path=None, fallback_url=None):
#     """Open an application or a fallback URL."""
#     speak(f"Opening {app_name} sir.")
#     try:
#         if app_path:
#             if os.path.exists(app_path):
#                 os.startfile(app_path)
#             else:
#                 speak(f"The path for {app_name} does not exist.")
#                 logging.error(f"Invalid path: {app_path}")
#         elif fallback_url:
#             webbrowser.open(fallback_url)
#         else:
#             speak(f"Unable to open {app_name}. No path or URL provided.")
#     except Exception as e:
#         speak(f"Failed to open {app_name}.")
#         logging.error(f"Error opening {app_name}: {e}")
#         if fallback_url:
#             speak(f"Opening fallback URL for {app_name}.")
#             webbrowser.open(fallback_url)

# def close_application(app_name):
#     """Close the specified application."""
#     speak(f"Closing {app_name} sir.")
#     try:
#         for proc in psutil.process_iter(attrs=['name']):
#             if app_name.lower() in proc.info['name'].lower():
#                 proc.kill()
#                 speak(f"{app_name} has been closed.")
#                 logging.info(f"{app_name} process terminated.")
#                 return
#         speak(f"{app_name} is not running.")
#     except Exception as e:
#         speak("Unable to close the application.")
#         logging.error(f"Error closing {app_name}: {e}")

# def type_in_app():
#     """Handle typing in the currently open application."""
#     speak("I am ready to type. Please start speaking.")
#     while True:
#         command = listen_command()
#         if "exit typing" in command:
#             speak("Exiting typing mode.")
#             break
#         else:
#             pyautogui.write(command)

# def save_file():
#     """Handle saving a file with a user-specified name."""
#     speak("Please specify a name for the file.")
#     file_name = listen_command()
#     if file_name:
#         pyautogui.hotkey('ctrl', 's')
#         time.sleep(1)
#         pyautogui.write(file_name)
#         pyautogui.press('enter')
#         speak(f"File has been saved as {file_name}.")
#     else:
#         speak("File name not provided. Unable to save the file.")

# def send_message():
#     """Handle typing and sending a message in social media apps."""
#     speak("I am ready to type your message. Please start speaking.")
#     while True:
#         command = listen_command()
#         if "exit typing" in command:
#             speak("Exiting typing mode and sending the message.")
#             pyautogui.press('enter')
#             break
#         else:
#             pyautogui.write(command)

# # Platform-specific functions
# def check_platform():
#     if platform.system() != "Windows":
#         speak("This script is designed for Windows systems and may not work on other platforms.")
#         raise SystemError("Unsupported platform")

# # Application-specific functions
# def open_kmplayer():
#     open_application("KMPlayer", "C:\program files\kmplayer 64x", "https://www.kmplayer.com")

# def open_settings():
#     if platform.system() == "Windows":
#         open_application("Settings", None, None)
#         os.system("start ms-settings:")
#     else:
#         speak("Settings can only be opened on Windows.")

# def open_notepad():
#     open_application("Notepad", "C:\\Windows\\notepad.exe")
#     type_in_app()
#     save_file()

# def open_paint():
#     open_application("Paint", "C:\\Windows\\System32\\mspaint.exe")
#     type_in_app()
#     save_file()

# def open_instagram():
#     open_application("Instagram", None, "https://www.instagram.com")
#     send_message()

# def open_facebook():
#     open_application("Facebook", None, "https://www.facebook.com")
#     send_message()

# def open_whatsapp():
#     open_application("WhatsApp", "C:\\Program Files\\WhatsApp", "https://web.whatsapp.com")
#     send_message()

# def open_youtube():
#     open_application("YouTube", None, "https://www.youtube.com")

# def open_gmail():
#     open_application("Gmail", None, "https://mail.google.com")

# def open_spotify():
#     open_application("Spotify", None, "https://open.spotify.com")

# def open_twitter():
#     open_application("Twitter", None, "https://twitter.com")
#     send_message()

# def open_discord():
#     open_application("Discord", None, "https://discord.com")
#     send_message()

# def open_chrome():
#     open_application("Google Chrome","C:\program files\google\chrome\application", "https://www.google.com/chrome/index.html")

# def open_msedge():
#     open_application("microsoft edge ", "C:\program files (x86)\microsoft\edge\application", "https://discord.com")

# def open_explorer():
#     if platform.system() == "Windows":
#         open_application("File Explorer", "C:\windows")
#         os.system("explorer")
#     else:
#         speak("File Explorer can only be opened on Windows.")


# def open_powerpoint():
#     if platform.system() == "Windows":
#         open_application("powerpoint", "C:\program files\microsoft office\root\office16")
#         os.system("powerpnt.exe")
#     else:
#         speak("powerpoint can only be opened on Windows.")

        





#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1 neew ///////////////////////////////////


import os
import webbrowser
import pyttsx3
import psutil
import pyautogui
import time
import platform
import logging
import speech_recognition as sr

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    """Speak the given text."""
    logging.info(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Capture voice command from the user."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("Listening for your command...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio)
            logging.info(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting. Please try again later.")
            return ""
        except Exception as e:
            speak("An error occurred while capturing your command.")
            logging.error(f"Error in listen_command: {e}")
            return ""

def open_application(app_name, command):
    """Open a system application or a specific URL."""
    speak(f"Opening {app_name}.")
    try:
        if command == "notepad":
            os.system("notepad")
        elif command == "paint":
            os.system("mspaint")
        elif command == "explorer":
            os.system("explorer")
        elif command == "settings":
            os.system("start ms-settings:")
        elif command == "instagram":
            webbrowser.open("https://www.instagram.com")
        elif command == "facebook":
            webbrowser.open("https://www.facebook.com")
        elif command == "whatsapp":
            webbrowser.open("https://web.whatsapp.com")
        elif command == "youtube":
            webbrowser.open("https://www.youtube.com")
        elif command == "gmail":
            webbrowser.open("https://mail.google.com")
        elif command == "spotify":
            webbrowser.open("https://open.spotify.com")
        elif command == "twitter":
            webbrowser.open("https://twitter.com")
        elif command == "discord":
            webbrowser.open("https://discord.com")
        elif command == "chrome":
            os.system("start chrome")
        else:
            speak(f"I don't know how to open {app_name}.")
    except Exception as e:
        speak(f"Failed to open {app_name}.")
        logging.error(f"Error opening {app_name}: {e}")

def close_application(app_name):
    """Close the specified application."""
    speak(f"Closing {app_name}.")
    try:
        for proc in psutil.process_iter(attrs=['name']):
            if app_name.lower() in proc.info['name'].lower():
                proc.kill()
                speak(f"{app_name} has been closed.")
                logging.info(f"{app_name} process terminated.")
                return
        speak(f"{app_name} is not running.")
    except Exception as e:
        speak("Unable to close the application.")
        logging.error(f"Error closing {app_name}: {e}")

def type_in_app():
    """Handle typing in the currently open application."""
    speak("I am ready to type. Please start speaking.")
    while True:
        command = listen_command()
        if "stop typing" in command:
            speak("Exiting typing mode.")
            break
        else:
            pyautogui.write(command)

def save_file():
    """Handle saving a file with a user-specified name."""
    speak("Please specify a name for the file.")
    file_name = listen_command()
    if file_name:
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.write(file_name)
        pyautogui.press('enter')
        speak(f"File has been saved as {file_name}.")
    else:
        speak("File name not provided. Unable to save the file.")

def send_message():
    """Handle typing and sending a message in social media apps."""
    speak("I am ready to type your message. Please start speaking.")
    while True:
        command = listen_command()
        if "stop typing" in command:
            speak("Exiting typing mode and sending the message.")
            pyautogui.press('enter')
            break
        else:
            pyautogui.write(command)

def open_notepad():
    open_application("Notepad", "notepad")
    type_in_app()
    save_file()

def open_paint():
    open_application("Paint", "paint")
    type_in_app()
    save_file()

def open_explorer():
    open_application("File Explorer", "explorer")

def open_settings():
    open_application("Settings", "settings")

def open_instagram():
    open_application("Instagram", "instagram")
    send_message()

def open_facebook():
    open_application("Facebook", "facebook")
    send_message()

def open_whatsapp():
    open_application("WhatsApp", "whatsapp")
    send_message()

def open_youtube():
    open_application("YouTube", "youtube")

def open_gmail():
    open_application("Gmail", "gmail")

def open_spotify():
    open_application("Spotify", "spotify")

def open_twitter():
    open_application("Twitter", "twitter")
    send_message()

def open_discord():
    open_application("Discord", "discord")
    send_message()

def open_chrome():
    open_application("Google Chrome", "chrome")



