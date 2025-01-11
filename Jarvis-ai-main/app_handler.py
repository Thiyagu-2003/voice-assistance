# import os
# import webbrowser
# import pyttsx3
# import pyautogui
# import time
# import speech_recognition as sr
# import threading
# import re

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()
# recognizer = sr.Recognizer()
# engine.setProperty('rate', 175)

# # Preload voices
# voices = engine.getProperty('voices')
# if voices:
#     engine.setProperty('voice', voices[1].id)

# def speak(text, blocking=False):
#     """Speak the given text in a thread (non-blocking)."""
#     def _speak():
#         engine.say(text)
#         engine.runAndWait()

#     if blocking:
#         _speak()
#     else:
#         threading.Thread(target=_speak).start()

# def listen_command():
#     """Capture voice command from the user with better error handling."""
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=0.5)
#         speak("Listening...", blocking=True)
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             command = recognizer.recognize_google(audio).lower()
#             print(f"Recognized command: {command}")
#             return command
#         except sr.WaitTimeoutError:
#            speak("I timed out listening. Please speak again.", blocking=True)
#            return ""
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand. Please repeat.", blocking=True)
#             return ""
#         except sr.RequestError as e:
#             speak(f"I'm having trouble connecting to Google. Please check your internet. Error: {e}", blocking=True)
#             return ""
#         except Exception as e:
#             speak(f"An error occurred: {e}", blocking=True)
#             return ""

# def open_application(command):
#     """Open a system application."""
#     command = command.replace("open ", "").strip()
#     try:
#        if "notepad" in command:
#            os.system("notepad")
#        elif "paint" in command:
#            os.system("mspaint")
#        elif "explorer" in command:
#            os.system("explorer")
#        elif "browser" in command or "chrome" in command or "firefox" in command:
#             webbrowser.open_new_tab("https://www.google.com")
#        else:
#             speak(f"Sorry, I can't open that: '{command}' . Please use a known app name like Notepad or Paint.", blocking=True)
#     except Exception as e:
#         speak(f"Failed to open '{command}'. Error: {e}", blocking=True)

# def type_text(text):
#     """Type the provided text into the current application."""
#     words = re.findall(r'\b\w+\b|\s+', text)
#     for word in words:
#       pyautogui.write(word)
#       time.sleep(0.03)

# def save_file():
#     """Handle saving a file with a user-specified name."""
#     speak("Please give the file a name.", blocking=True)
#     file_name = listen_command()
#     if file_name:
#        pyautogui.hotkey('ctrl', 's')
#        time.sleep(0.5)
#        pyautogui.write(file_name, interval=0)
#        pyautogui.press('enter')
#        speak(f"File saved as {file_name}.", blocking=True)
#     else:
#         speak("No file name given. Operation canceled.", blocking=True)

# def execute_command(command, typing_mode=False):
#     """Identify and execute commands."""
#     if typing_mode:
#         type_text(command)
#     elif command.startswith("open"):
#         open_application(command)
#     elif command.startswith("save the file"):
#         save_file()
#     else:
#         speak("Command not recognized.", blocking=True)

# def main():
#     """Main program loop."""
#     speak("Hello! I am online.", blocking=True)
#     typing_mode = False  # Initialize typing mode flag

#     while True:
#         command = listen_command()
#         if command:
#             if "exit typing mode" in command or "stop typing" in command:
#                 typing_mode = False
#                 speak("Exiting typing mode.", blocking=True)
#             elif "enter typing mode" in command or "start typing" in command:
#                 typing_mode = True
#                 speak("Entering typing mode. Start speaking.", blocking=True)
#             elif "exit" in command or "quit" in command or "stop" in command:
#                 speak("Goodbye!", blocking=True)
#                 break
#             else:
#                 execute_command(command, typing_mode)

# if __name__ == "__main__":
#     main()



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
