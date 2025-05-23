# import json
# import threading
# import time
# import queue
# from datetime import datetime
# import speech_recognition as sr
# import pyttsx3
# from plyer import notification
# import webbrowser

# # -----------------------------
# # Memory storage (name, preferences, last search)
# # -----------------------------
# MEMORY_FILE = 'memory.json'

# def load_memory():
#     try:
#         with open(MEMORY_FILE, 'r') as f:
#             return json.load(f)
#     except:
#         return {"name": "", "preferences": {}, "last_search": ""}

# def save_memory(memory):
#     with open(MEMORY_FILE, 'w') as f:
#         json.dump(memory, f, indent=2)

# memory = load_memory()

# # -----------------------------
# # Task system with reminders
# # -----------------------------
# TASK_FILE = "tasks.json"

# def load_tasks():
#     try:
#         with open(TASK_FILE, 'r') as f:
#             return json.load(f)
#     except:
#         return []

# def save_tasks(tasks):
#     with open(TASK_FILE, 'w') as f:
#         json.dump(tasks, f, indent=2)

# # -----------------------------
# # Notification function
# # -----------------------------
# def show_notification(title, message):
#     notification.notify(
#         title=title,
#         message=message,
#         timeout=10
#     )

# # -----------------------------
# # Voice Assistant Engine
# # -----------------------------
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# # Queue for safe multi-threaded speaking
# speak_queue = queue.Queue()

# def speak(text):
#     print("Jarvis:", text)
#     speak_queue.put(text)

# def speaker_loop():
#     while True:
#         text = speak_queue.get()
#         engine.say(text)
#         engine.runAndWait()

# # -----------------------------
# # Speech Recognition
# # -----------------------------
# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#         try:
#             command = r.recognize_google(audio)
#             print("You:", command)
#             return command.lower()
#         except:
#             speak("Sorry, I didn't catch that.")
#             return ""

# # -----------------------------
# # Background Task Checker
# # -----------------------------
# def task_checker():
#     while True:
#         now = datetime.now().strftime("%Y-%m-%d %H:%M")
#         tasks = load_tasks()
#         for task in tasks:
#             if task['time'] == now and not task.get("done"):
#                 reminder_message = f"Reminder: {task['task']}"
#                 speak(reminder_message)
#                 show_notification("Task Reminder", task['task'])
#                 task["done"] = True
#         save_tasks(tasks)
#         time.sleep(60)

# # -----------------------------
# # Command Handler
# # -----------------------------
# def respond(command):
#     global memory

#     if "my name is" in command:
#         memory['name'] = command.split("my name is")[-1].strip()
#         save_memory(memory)
#         speak(f"Got it! I’ll remember your name is {memory['name']}.")

#     elif "what is my name" in command:
#         if memory['name']:
#             speak(f"Your name is {memory['name']}.")
#         else:
#             speak("I don't know your name yet.")

#     elif "remember that" in command:
#         key = command.split("remember that")[-1].strip()
#         memory['last_search'] = key
#         save_memory(memory)
#         speak(f"I’ll remember that: {key}.")

#     elif "what did i ask you to remember" in command:
#         if memory['last_search']:
#             speak(f"You asked me to remember: {memory['last_search']}.")
#         else:
#             speak("You haven't asked me to remember anything yet.")

#     elif "remind me to" in command:
#         try:
#             # Expected format: "remind me to drink water at 15:30"
#             task_text = command.split("remind me to")[1].split(" at ")[0].strip()
#             task_time = command.split(" at ")[1].strip()

#             now = datetime.now()
#             full_time = datetime.strptime(f"{now.date()} {task_time}", "%Y-%m-%d %H:%M")

#             task = {
#                 "task": task_text,
#                 "time": full_time.strftime("%Y-%m-%d %H:%M"),
#                 "done": False
#             }

#             tasks = load_tasks()
#             tasks.append(task)
#             save_tasks(tasks)

#             speak(f"Reminder set for {task_text} at {task_time}")
#         except Exception as e:
#             print("Error:", e)
#             speak("Please say: remind me to [task] at [HH:MM]")

#     elif "time" in command:
#         now = datetime.now().strftime("%H:%M")
#         speak(f"The time is {now}")

#     elif "open youtube" in command:
#         webbrowser.open("https://youtube.com")
#         speak("Opening YouTube")

#     elif "exit" in command or "stop" in command:
#         speak("Goodbye!")
#         exit()

#     else:
#         speak("Sorry, I don't know how to do that yet.")

# # -----------------------------
# # Main loop
# # -----------------------------
# def main():
#     threading.Thread(target=speaker_loop, daemon=True).start()
#     threading.Thread(target=task_checker, daemon=True).start()

#     speak("Hello! How can I help you today?")
#     while True:
#         cmd = listen()
#         if cmd:
#             respond(cmd)

# if __name__ == '__main__':
#     main()







import time
import ctypes
import threading
import winsound

# Constants for Windows message box types
MB_OK = 0x0
MB_ICONINFORMATION = 0x40
MB_ICONWARNING = 0x30
MB_ICONERROR = 0x10

# Sound constants
SOUND_DEFAULT = winsound.MB_OK
SOUND_WARNING = winsound.MB_ICONEXCLAMATION
SOUND_ERROR = winsound.MB_ICONHAND
SOUND_INFO = winsound.MB_ICONASTERISK

# App configuration
APP_NAME = "Voice Assistant NOVA"
ICON_PATH = r"D:\FINAL_YEAR_PROJECT\voice-assistance\NOVA-ai-main\Material\Nova Logo.ico"

class NotificationType:
    """Notification types with predefined styles"""
    INFO = {"icon": MB_ICONINFORMATION, "sound": SOUND_INFO, "buttons": MB_OK}
    WARNING = {"icon": MB_ICONWARNING, "sound": SOUND_WARNING, "buttons": MB_OK}
    ERROR = {"icon": MB_ICONERROR, "sound": SOUND_ERROR, "buttons": MB_OK}

class Notification:
    """Enhanced notification system for Voice Assistant NOVA"""
    
    @staticmethod
    def show(message, notification_type=NotificationType.INFO, play_sound=True):
        """
        Display a Windows message box notification with customized appearance and sound.
        
        Args:
            message (str): The notification content
            notification_type (dict): Predefined style (NotificationType.INFO, WARNING, ERROR)
            play_sound (bool): Whether to play a sound with the notification
            
        Returns:
            int: Response code from the message box (e.g., 1=OK)
        """
        # Combine style flags
        style = notification_type["icon"] | notification_type["buttons"]
        
        # Play appropriate sound if enabled
        if play_sound:
            winsound.MessageBeep(notification_type["sound"])
        
        # Load icon from path
        icon_handle = 0
        try:
            icon_handle = ctypes.windll.user32.LoadImageW(
                0, ICON_PATH, 1, 0, 0, 0x00000010 | 0x00000040
            )
        except Exception:
            pass  # If icon loading fails, continue without icon
        
        # Show the message box and return the result
        return ctypes.windll.user32.MessageBoxW(0, message, APP_NAME, style)
    
    @staticmethod
    def show_non_blocking(message, notification_type=NotificationType.INFO, play_sound=True, callback=None):
        """
        Display a notification in a separate thread so it doesn't block the main program.
        
        Args:
            message (str): The notification content
            notification_type (dict): Predefined style (NotificationType.INFO, WARNING, ERROR)
            play_sound (bool): Whether to play a sound with the notification
            callback (function): Function to call with the result when the notification is closed
            
        Returns:
            thread: The thread object displaying the notification
        """
        def show_and_callback():
            result = Notification.show(message, notification_type, play_sound)
            if callback:
                callback(result)
            return result
            
        thread = threading.Thread(target=show_and_callback)
        thread.daemon = True
        thread.start()
        return thread
    
    @staticmethod
    def schedule(message, delay_seconds=0, notification_type=NotificationType.INFO, play_sound=True, callback=None):
        """
        Schedule a notification to be shown after a specified delay.
        
        Args:
            message (str): The notification content
            delay_seconds (int): Time to wait before showing notification (in seconds)
            notification_type (dict): Predefined style (NotificationType.INFO, WARNING, ERROR)
            play_sound (bool): Whether to play a sound with the notification
            callback (function): Function to call with the result when the notification is closed
            
        Returns:
            thread: The thread object that will display the notification
        """
        def delayed_notification():
            if delay_seconds > 0:
                time.sleep(delay_seconds)
            result = Notification.show(message, notification_type, play_sound)
            if callback:
                callback(result)
            return result
        
        thread = threading.Thread(target=delayed_notification)
        thread.daemon = True
        thread.start()
        return thread

# Example usage
if __name__ == "__main__":
    # Define a callback function to handle user response
    def handle_response(result):
        if result == 1:  # OK
            print("User clicked OK")
    
    # Display a single information notification
    print("Showing NOVA notification...")
    Notification.show_non_blocking(
        "Welcome to Voice Assistant NOVA!", 
        NotificationType.INFO,
        callback=handle_response
    )
    
    # Keep the main thread running briefly to allow notification to appear
    print("Main program continues running...")
    time.sleep(5)
    print("Program finished.")