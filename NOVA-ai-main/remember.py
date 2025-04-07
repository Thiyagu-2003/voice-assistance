import json
import threading
import time
import queue
from datetime import datetime
import speech_recognition as sr
import pyttsx3
from plyer import notification
import webbrowser

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
# Notification function
# -----------------------------
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

# -----------------------------
# Voice Assistant Engine
# -----------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Queue for safe multi-threaded speaking
speak_queue = queue.Queue()

def speak(text):
    print("Jarvis:", text)
    speak_queue.put(text)

def speaker_loop():
    while True:
        text = speak_queue.get()
        engine.say(text)
        engine.runAndWait()

# -----------------------------
# Speech Recognition
# -----------------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You:", command)
            return command.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

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
# Command Handler
# -----------------------------
def respond(command):
    global memory

    if "my name is" in command:
        memory['name'] = command.split("my name is")[-1].strip()
        save_memory(memory)
        speak(f"Got it! I’ll remember your name is {memory['name']}.")

    elif "what is my name" in command:
        if memory['name']:
            speak(f"Your name is {memory['name']}.")
        else:
            speak("I don't know your name yet.")

    elif "remember that" in command:
        key = command.split("remember that")[-1].strip()
        memory['last_search'] = key
        save_memory(memory)
        speak(f"I’ll remember that: {key}.")

    elif "what did i ask you to remember" in command:
        if memory['last_search']:
            speak(f"You asked me to remember: {memory['last_search']}.")
        else:
            speak("You haven't asked me to remember anything yet.")

    elif "remind me to" in command:
        try:
            # Expected format: "remind me to drink water at 15:30"
            task_text = command.split("remind me to")[1].split(" at ")[0].strip()
            task_time = command.split(" at ")[1].strip()

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

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I don't know how to do that yet.")

# -----------------------------
# Main loop
# -----------------------------
def main():
    threading.Thread(target=speaker_loop, daemon=True).start()
    threading.Thread(target=task_checker, daemon=True).start()

    speak("Hello! How can I help you today?")
    while True:
        cmd = listen()
        if cmd:
            respond(cmd)

if __name__ == '__main__':
    main()




# import winsound
# from win10toast import ToastNotifier

# def show_notification(title, message):
#     winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)  # Plays a system sound
#     toaster = ToastNotifier()
#     toaster.show_toast(title, message, duration=10)


# from win10toast import ToastNotifier

# toaster = ToastNotifier()
# toaster.show_toast(
#     "Test Notification",
#     "This is a test with sound!",
#     duration=10,
#     threaded=True,  # Non-blocking
#     icon_path=None
# )


# from win10toast import ToastNotifier
# import os

# # Initialize the notifier
# toaster = ToastNotifier()

# # Set up relative path to the icon
# base_dir = os.path.dirname(__file__)
# icon_path = os.path.join(base_dir, "Material", "Nova Logo.ico")

# # Notification details
# app_name = "Nova Voice Assistant"
# message = "Your daily summary is ready. Tap to view."

# # Show the toast notification
# toaster.show_toast(
#     app_name,         # Title of the toast / app name
#     message,          # Message body
#     duration=10,      # Duration in seconds
#     threaded=True,    # Run in background
#     icon_path=icon_path  # Relative path to the icon
# )
