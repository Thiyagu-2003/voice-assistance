from pyautogui import press, keyDown, keyUp, screenshot
import pyttsx3
import os
import datetime
import pyautogui

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Set speaking speed
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Set female voice (optional)

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def press_and_release(key_combination):
    """Simulates pressing and releasing a key combination."""
    keys = key_combination.split('+')  # Split keys by '+'
    for key in keys:
        keyDown(key.strip())  # Press each key
    for key in reversed(keys):
        keyUp(key.strip())  # Release each key

def WindowsAuto(command):
    query = str(command).lower()

    if 'home screen' in query:                      #working
        speak("Minimizing all windows and showing the home screen sir.")
        press_and_release('win+m')

    elif 'minimize' in query or 'minimise' in query:                # working
        speak("Minimizing windows sir.")
        pyautogui.hotkey('win', 'down', 'down')

    elif 'maximize' in query or 'maximise' in query:            # working
        speak("Maximizing windows sir.")
        pyautogui.hotkey('win', 'up', 'up')

    elif 'close the window' in query or 'close the application' in query:   # working
        speak("Closing the window, sir.")
        pyautogui.hotkey('alt', 'f4')


    elif 'show start' in query:                     #working
        speak("Opening the start menu sir.")
        press('win')

    elif 'open setting' in query:                       #working
        speak("Opening the settings window sir.")
        press_and_release('win+i')

    elif 'open search' in query:                    #working
        speak("Opening the search bar sir.")
        press_and_release('win+s')

    elif 'restore windows' in query:                    #working
        speak("Restoring all minimized windows.")
        press_and_release('win+shift+m')

    elif 'start recording' in query:                    #working
        speak("Starting screen recording.")
        press_and_release('win+alt+r')

    elif 'stop recording' in query:                     #working
        speak("Stopping screen recording.")
        press_and_release('win+alt+r')

    elif 'shutdown' in query:                       # working
        speak("Are you sure you want to shut down the computer? Say yes to confirm or no to cancel.")
        confirmation = input("Type 'yes' to confirm or 'no' to cancel: ").strip().lower()
        if confirmation == 'yes':
            speak("Shutting down the computer. Goodbye, sir.")
            os.system('shutdown /s /t 1')
        else:
            speak("Shutdown cancelled.")

    elif 'restart' in query:                    # working
        speak("Are you sure you want to restart the computer? Say yes to confirm or no to cancel.")
        confirmation = input("Type 'yes' to confirm or 'no' to cancel: ").strip().lower()
        if confirmation == 'yes':
            speak("Restarting the computer. Please wait.")
            os.system('shutdown /r /t 1')
        else:
            speak("Restart cancelled.")

    elif 'log out' in query:            # working
        speak("Are you sure you want to log out? Say yes to confirm or no to cancel.")
        confirmation = input("Type 'yes' to confirm or 'no' to cancel: ").strip().lower()
        if confirmation == 'yes':
            speak("Logging out. See you soon, sir.")
            os.system('shutdown -l')
        else:
            speak("Logout cancelled.")

    elif 'system sleep' in query:               # not working
        speak("Putting the computer to sleep mode, sir.")
        os.system('rundll32.exe powrprof.dll,SetSuspendState Sleep')

    else:
        speak("Sorry, I didn't understand the command.")
