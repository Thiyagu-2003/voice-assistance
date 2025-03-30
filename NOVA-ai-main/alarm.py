# import pyttsx3
# import sched
# import time
# from datetime import datetime

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Schedule manager
# scheduler = sched.scheduler(time.time, time.sleep)

# # Function to speak a message
# def speak_message(message):
#     engine.say(message)
#     engine.runAndWait()

# # Function to check if the time for an alarm has arrived
# def check_alarm_time(alarm_time):
#     # Current time in 12-hour format with AM/PM
#     current_time = datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM
#     if current_time == alarm_time:
#         speak_message("It's time for your scheduled alarm!")

# # Function to set an alarm at a specific time
# def set_alarm():
#     alarm_time = input("Enter the alarm time (12-hour format, e.g., 02:30 PM): ")
#     speak_message(f"Alarm set for {alarm_time}.")
#     while True:
#         check_alarm_time(alarm_time)
#         time.sleep(60)  # Check every minute

# # Function to add an event to the schedule
# def add_to_schedule():
#     event_time = input("Enter the event time (12-hour format, e.g., 04:00 PM): ")
#     event_name = input("Enter the event name: ")
#     speak_message(f"Scheduled {event_name} at {event_time}.")
#     event_time_obj = datetime.strptime(event_time, "%I:%M %p")  # 12-hour format with AM/PM
#     delay = (event_time_obj - datetime.now()).total_seconds()

#     if delay < 0:  # if time has passed today, schedule it for the next day
#         delay += 86400  # 24 hours in seconds

#     scheduler.enter(delay, 1, speak_message, argument=(f"Event '{event_name}' is happening now!",))
#     scheduler.run()

# # Main function to run the program
# if __name__ == "__main__":
#     while True:
#         # Ask the user what action they want to perform
#         action = input("Choose an action:\n1. Set an Alarm\n2. Add an Event to Schedule\n3. Exit\nEnter your choice: ")
        
#         if action == "1":
#             set_alarm()
#         elif action == "2":
#             add_to_schedule()
#         elif action == "3":
#             speak_message("Exiting the program.")
#             break
#         else:
#             speak_message("Invalid choice, please try again.")

import pyttsx3
import sched
import time
from datetime import datetime
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Schedule manager
scheduler = sched.scheduler(time.time, time.sleep)

# Function to speak a message
def speak_message(message):
    engine.say(message)
    engine.runAndWait()

# Function to check if the time for an alarm has arrived
def check_alarm_time(alarm_time):
    # Current time in 12-hour format with AM/PM
    current_time = datetime.now().strftime("%I:%M %p").lower()  # 12-hour format with AM/PM (lowercase for easier comparison)
    alarm_time = alarm_time.lower()  # make the alarm time lowercase to handle case insensitivity
    if current_time == alarm_time:
        speak_message("It's time for your scheduled alarm!")

# Function to set an alarm at a specific time
def set_alarm():
    alarm_time = input("Enter the alarm time (12-hour format, e.g., 08:30 PM): ")
    speak_message(f"Alarm set for {alarm_time}.")
    while True:
        check_alarm_time(alarm_time)
        time.sleep(60)  # Check every minute

# Function to add an event to the schedule
def add_to_schedule():
    event_time = input("Enter the event time (12-hour format, e.g., 04:00 PM): ")
    event_name = input("Enter the event name: ")
    speak_message(f"Scheduled {event_name} at {event_time}.")
    event_time_obj = datetime.strptime(event_time, "%I:%M %p")  # 12-hour format with AM/PM
    delay = (event_time_obj - datetime.now()).total_seconds()

    if delay < 0:  # if time has passed today, schedule it for the next day
        delay += 86400  # 24 hours in seconds

    scheduler.enter(delay, 1, speak_message, argument=(f"Event '{event_name}' is happening now!",))
    scheduler.run()

# Function to start the alarm and event schedule in parallel
def start_program():
    while True:
        # Ask the user what action they want to perform
        action = input("Choose an action:\n1. Set an Alarm\n2. Add an Event to Schedule\n3. Exit\nEnter your choice: ")
        
        if action == "1":
            alarm_thread = threading.Thread(target=set_alarm)
            alarm_thread.daemon = True  # Make sure it terminates when the program ends
            alarm_thread.start()
        elif action == "2":
            schedule_thread = threading.Thread(target=add_to_schedule)
            schedule_thread.daemon = True  # Make sure it terminates when the program ends
            schedule_thread.start()
        elif action == "3":
            speak_message("Exiting the program.")
            break
        else:
            speak_message("Invalid choice, please try again.")

if __name__ == "__main__":
    start_program()
