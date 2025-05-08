import pygetwindow as gw                # all working fine
import pyautogui
from time import sleep
import pyttsx3


# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Set speaking speed
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Set female voice (optional)

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()


def YouTubeAuto(command):
    # Focus the browser window (replace 'YouTube' with the correct browser title if needed)
    windows = gw.getWindowsWithTitle('YouTube')
    if windows:
        windows[0].activate()  # Activate the first YouTube window found
    else:
        print("YouTube is not open or not focused.")
        return  # Exit if YouTube is not open or found

    sleep(0.5)  # Allow time for the window to activate

    query = str(command).lower()
    
    # Pause or Resume the video
    if 'pause' in query or 'pass' in query:
        pyautogui.press('space')  # Space key to pause or resume the video
        print("Video Paused sir")
        speak("Video Paused sir")

    elif 'resume' in query or 'resume' in query or 'unpass' in query or 'unpause' in query or 'un pass' in query or 'un pause' in query:
        pyautogui.press('space')  # Space key to pause or resume the video
        print("Video Resumed sir")
        speak("Video Resumed sir")

    # Fullscreen the video
    elif 'full screen' in query or 'fullscreen' in query:
        pyautogui.press('f')  # 'f' key for fullscreen
        print(" playing Video in Fullscreened sir")
        speak(" playing Video in Fullscreened sir")

    # Film Screen (Theater Mode)
    elif 'film screen' in query or 'flimscreen' in query:
        pyautogui.press('t')  # 't' key for theater mode
        print("playing Video in flimscreen sir")
        speak("playing Video in flimscreen sir")

    # Skip Forward
    elif 'skip' in query:
        pyautogui.press('l')  # 'l' key to skip 10 seconds forward
        print("Video skipped forward 10seconds sir")
        speak("Video skipped forward 10seconds sir")

    # Skip Backward
    elif 'back' in query:
        pyautogui.press('j')  # 'j' key to skip 10 seconds backward
        print("Video skipped backward sir")
        speak("Video skipped backward sir")


    # Increase Volume
    elif 'increase youtube volume' in query or 'volume up' in query or 'volumeup' in query:                        # new
        for _ in range(5):  # increase volume by 10% (5 presses should roughly decrease it by 10%)
            pyautogui.press('volumeup')  # 'volumeup' key
        print(" increased Video volume sir")
        speak(" increased Video volume by 2 percent sir")




    # Decrease Volume by 10%                                           # new
    elif 'decrease youtube volume' in query or 'volume down' in query or 'volumedown' in query:
        for _ in range(5):  # Decrease volume by 10% (5 presses should roughly decrease it by 10%)
            pyautogui.press('volumedown')
        print("Decreased Video volume sir")
        speak("Decreased Video volume by 10 percent sir")



    # Max Volume                                                        # new
    elif 'max volume' in query:
        for _ in range(20):  # Increase volume multiple times to max
            pyautogui.press('volumeup')
        pyautogui.hotkey('volumeup')  # Direct command to set maximum volume
        print("Maxed Video volume sir")
        speak("Volume increased to its max level sir")



    # Mute
    elif 'mute' in query:
        pyautogui.press('volumemute')  # Mute the volume
        print("muted the video sir")
        speak("muted the video sir")

    # Unmute
    elif 'unmute' in query:
        pyautogui.press('volumemute')  # unmute the volume
        print("unmuted the video sir")
        speak("unmuted the video sir")

    # Next Video
    elif 'next' in query:
        pyautogui.hotkey('shift', 'n')  # 'shift + n' for next video
        print("playing next Video sir")
        speak("playing next Video sir")

    # Previous Video
    elif 'previous' in query:
        pyautogui.hotkey('shift', 'p')  # 'shift + p' for previous video
        print("playing previous Video sir")
        speak("playing previous Video sir")