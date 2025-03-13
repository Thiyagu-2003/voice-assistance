
# import os
# import pyttsx3
# import speech_recognition as sr
# import pywhatkit as kit
# import webbrowser

# def speak(text):
#     """Convert text to speech."""
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.setProperty('volume', 1)
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     """Capture audio and return the recognized text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("I'm listening...")
#         print("Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             command = recognizer.recognize_google(audio)
#             print(f"You said: {command}")
#             return command.lower()
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand that.")
#             return None
#         except sr.WaitTimeoutError:
#             speak("I didn't hear anything.")
#             return None

# def is_whatsapp_installed():
#     """Check if WhatsApp is installed."""
#     paths = [
#         "C:\\Program Files\\WindowsApps",
#         "C:\\Program Files\\WhatsApp",
#         "C:\\Program Files (x86)\\WhatsApp",
#         "C:\Program Files\WindowsApps"

#     ]
#     for path in paths:
#         if os.path.exists(path):
#             return True
#     return False

# def open_whatsapp():
#     """Open WhatsApp app or browser."""
#     if is_whatsapp_installed():
#         speak("Opening WhatsApp.")
#         os.system("start whatsapp://")
#     else:
#         speak("WhatsApp is not installed on your system. Opening WhatsApp Web in the browser.")
#         #webbrowser.open("https://web.whatsapp.com")

# def make_call(contact_name, call_type="voice"):
#     """Make a WhatsApp call."""
#     speak(f"Making a {call_type} call to {contact_name}.")
#     # Use automation or ADB for advanced functionality.
#     # Here, we're simulating a message as a placeholder.
#     phone_number = contacts.get(contact_name)
#     if phone_number:
#         kit.sendwhatmsg_instantly(phone_no=f"+{phone_number}", message="Call initiated", wait_time=10)
#     else:
#         speak("I couldn't find that contact.")

# def main():
#     """Main program logic."""
#     speak("What do you want to do?")
#     command = listen()

#     if command:
#         if "open whatsapp" in command:
#             open_whatsapp()
#         elif "call" in command:
#             call_type = "video" if "video call" in command else "voice"
#             # Example contact mapping
#             global contacts
#             contacts = {
#                 "lokesh clg": "+your number",  # Replace with actual phone numbers
#                 #
#                 # "john": "0000000000"
#             }
#             for name in contacts.keys():
#                 if name in command:
#                     make_call(name, call_type)
#                     return
#             speak("I couldn't find that contact.")
#         else:
#             speak("I can only open WhatsApp or make calls for now.")

# if __name__ == "__main__":
#     main()


# import os
# import pyttsx3
# import speech_recognition as sr
# import pywhatkit as kit
# import webbrowser

# def speak(text):
#     """Convert text to speech."""
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.setProperty('volume', 1)
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     """Capture audio and return the recognized text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("I'm listening...")
#         print("Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             command = recognizer.recognize_google(audio)
#             print(f"You said: {command}")
#             return command.lower()
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand that.")
#             return None
#         except sr.WaitTimeoutError:
#             speak("I didn't hear anything.")
#             return None

# def is_whatsapp_installed():
#     """Check if WhatsApp is installed."""
#     paths = [
#         "C:\\Program Files\\WindowsApps",
#         "C:\\Program Files\\WhatsApp",
#         "C:\\Program Files (x86)\\WhatsApp"
#     ]
#     for path in paths:
#         if os.path.exists(path):
#             return True
#     return False

# def open_whatsapp():
#     """Open WhatsApp app or browser."""
#     if is_whatsapp_installed():
#         speak("Opening WhatsApp.")
#         os.system("start whatsapp://")
#     else:
#         speak("WhatsApp is not installed on your system. Opening WhatsApp Web in the browser.")
#         webbrowser.open("https://web.whatsapp.com")

# def make_call(contact_name, call_type="voice"):
#     """Make a WhatsApp call."""
#     if is_whatsapp_installed():
#         speak(f"Making a {call_type} call to {contact_name}.")
#         # For direct calling in the installed app, use automation or specific WhatsApp API endpoints if available.
#         # Placeholder for call logic on installed app:
#         os.system(f"start whatsapp://send?phone={contacts.get(contact_name)}")
#     else:
#         speak("WhatsApp is not installed. Opening WhatsApp Web in the browser.")
#         webbrowser.open("https://web.whatsapp.com")

# def main():
#     """Main program logic."""
#     speak("What do you want to do?")
#     command = listen()

#     if command:
#         if "open whatsapp" in command:
#             open_whatsapp()
#         elif "call" in command:
#             call_type = "video" if "video call" in command else "voice"
#             # Example contact mapping
#             global contacts
#             contacts = {
#                 "lokesh clg": "+your number",  # Replace with actual phone numbers
#                 #"john": "0000000000"
#             }
#             for name in contacts.keys():
#                 if name in command:
#                     make_call(name, call_type)
#                     return
#             speak("I couldn't find that contact.")
#         else:
#             speak("I can only open WhatsApp or make calls for now.")

# if __name__ == "__main__":
#     main()




import os
import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import webbrowser
import psutil

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm listening...")
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return None

def is_whatsapp_installed():
    """Check if WhatsApp is installed."""
    paths = [
        "C:\\Program Files\\WindowsApps",
        "C:\\Program Files\\WhatsApp",
        "C:\\Program Files (x86)\\WhatsApp"
    ]
    for path in paths:
        if os.path.exists(path):
            return True
    return False

def open_whatsapp():
    """Open WhatsApp app or browser."""
    if is_whatsapp_installed():
        speak("Opening WhatsApp.")
        os.system("start whatsapp://")
    else:
        speak("WhatsApp is not installed on your system. Opening WhatsApp Web in the browser.")
        webbrowser.open("https://web.whatsapp.com")

def make_call(contact_name, call_type="voice"):
    """Make a WhatsApp call."""
    if is_whatsapp_installed():
        speak(f"Making a {call_type} call to {contact_name}.")
        os.system(f"start whatsapp://send?phone={contacts.get(contact_name)}")
    else:
        speak("WhatsApp is not installed. Opening WhatsApp Web in the browser.")
        webbrowser.open("https://web.whatsapp.com")

def send_message(contact_name, message):
    """Send a WhatsApp message."""
    if is_whatsapp_installed():
        speak(f"Sending message to {contact_name}.")
        os.system(f"start whatsapp://send?phone={contacts.get(contact_name)}&text={message}")
    else:
        speak("WhatsApp is not installed. Opening WhatsApp Web in the browser.")
        webbrowser.open("https://web.whatsapp.com")

def close_whatsapp():
    """Close WhatsApp application if running."""
    speak("Closing WhatsApp.")
    for process in psutil.process_iter():
        try:
            if "whatsapp" in process.name().lower():
                process.terminate()
                speak("WhatsApp has been closed.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    speak("WhatsApp is not running.")

def main():
    """Main program logic."""
    speak("What do you want to do?")
    command = listen()

    if command:
        if "open whatsapp" in command:
            open_whatsapp()
        elif "call" in command:
            call_type = "video" if "video call" in command else "voice"
            global contacts
            contacts = {
                "lokesh clg": "+your number",  # Replace with actual phone numbers
                #"john": "0000000000"
            }
            for name in contacts.keys():
                if name in command:
                    make_call(name, call_type)
                    return
            speak("I couldn't find that contact.")
        elif "send message" in command:
            #global contacts
            contacts = {
                "lokesh clg": "+your number",  # Replace with actual phone numbers
                #"john": "0000000000"
            }
            for name in contacts.keys():
                if name in command:
                    speak("What is the message?")
                    message = listen()
                    if message:
                        send_message(name, message)
                    return
            speak("I couldn't find that contact.")
        elif "close whatsapp" in command:
            close_whatsapp()
        else:
            speak("I can open WhatsApp, make calls, send messages, or close WhatsApp.")

if __name__ == "__main__":
    main()
