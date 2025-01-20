import os
import pyttsx3
import speech_recognition as sr
import platform
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen to the user's voice command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening for your command, sir.")
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Network error. Please try again later.")
            return ""

def open_action_center():
    """Open the Action Center using Windows + A."""
    pyautogui.hotkey('win', 'a')
    time.sleep(1)  # Wait for the Action Center to open

def toggle_bluetooth():
    """Toggle Bluetooth from the Action Center."""
    open_action_center()
    pyautogui.click(x=1703, y=672)  # Replace with the coordinates of the Bluetooth icon
    time.sleep(1)
    pyautogui.hotkey('esc')  # Close the Action Center

def toggle_wifi():
    """Toggle Wi-Fi from the Action Center."""
    open_action_center()
    pyautogui.click(x=1595, y=668)  # Replace with the coordinates of the Wi-Fi icon
    time.sleep(1)
    pyautogui.hotkey('esc')  # Close the Action Center

def toggle_night_light():
    """Toggle Night Light from the Action Center."""
    open_action_center()
    pyautogui.click(x=1728, y=769)  # Replace with the coordinates of the Night Light icon
    time.sleep(1)
    pyautogui.hotkey('esc')  # Close the Action Center

def toggle_airplane_mode():
    """Toggle Airplane Mode from the Action Center."""
    open_action_center()
    pyautogui.click(x=1835, y=670)  # Replace with the coordinates of the Airplane Mode icon
    time.sleep(1)
    pyautogui.hotkey('esc')  # Close the Action Center

def adjust_volume(command):                                         # working
    """Adjust system volume."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    if "no sound" in command:                         # Mute the audio
        volume.SetMute(1, None)
        speak("System muted.")

    elif "no sound" in command or "volume mute" in command or "no volume" in command:                   # Mute the audio
        pyautogui.press("volumemute")
        speak("System muted.")

    elif "sound" in command:                          # Unmute the audio
        volume.SetMute(0, None)
        speak("System unmuted.")

    elif "maximum volume" in command:                # Set volume to 100%
        volume.SetMasterVolumeLevelScalar(1.0, None)
        speak("Volume set to maximum, 100%.")

    elif "check current volume level" in command or "current volume level" in command:                # Check current volume level
        current_volume = volume.GetMasterVolumeLevelScalar() * 100
        speak(f"The current volume is {int(current_volume)}%.")

    elif "set volume to" in command:                 # Set volume to a specific level
        try:
            # Extract the desired volume level from the command
            level = int(''.join(filter(str.isdigit, command)))
            if 0 <= level <= 100:
                volume.SetMasterVolumeLevelScalar(level / 100, None)
                speak(f"Volume set to {level}%.")
            else:
                speak("Please specify a volume level between 0 and 100.")
        except ValueError:
            speak("I couldn't understand the desired volume level.")

    else:
        current_volume = volume.GetMasterVolumeLevelScalar() * 100

        if "increase volume" in command or "increasevolume" in command:  # Increase volume
            new_volume = min(current_volume + 25, 100) / 100
            volume.SetMasterVolumeLevelScalar(new_volume, None)
            speak(f"Volume increased to {int(new_volume * 100)}%.")

        elif "decrease volume" in command or "decreasevolume" in command:  # Decrease volume
            new_volume = max(current_volume - 25, 0) / 100
            volume.SetMasterVolumeLevelScalar(new_volume, None)
            speak(f"Volume decreased to {int(new_volume * 100)}%.")



def adjust_brightness(command):                                 # working
    """Adjust screen brightness."""
    if platform.system() == "Windows":
        try:
            from screen_brightness_control import set_brightness, get_brightness
            current_brightness = get_brightness()[0]
            if "increase brightness" in command:
                new_brightness = min(current_brightness + 25, 100)
                set_brightness(new_brightness)
                speak(f"Brightness increased to {new_brightness}%.")
            elif "decrease brightness" in command:
                new_brightness = max(current_brightness - 25, 0)
                set_brightness(new_brightness)
                speak(f"Brightness decreased to {new_brightness}%.")
            elif "check brightness level" in command or "current brightness" in command or "brightness level" in command:
                speak(f"Current brightness is {current_brightness}%.")
            elif "set brightness to" in command or "change brightness to" in command or "adjust brightness to" in command or "set current brightness to" in command:
                try:
                    target_brightness = int(command.split("set brightness to")[-1].strip())
                    if 0 <= target_brightness <= 100:
                        set_brightness(target_brightness)
                        speak(f"Brightness set to {target_brightness}%.")
                    else:
                        speak("Please specify a brightness level between 0 and 100.")
                except ValueError:
                    speak("Invalid brightness value specified. Please try again.")
        except Exception as e:
            print(f"Error in adjust_brightness function: {e}")
            speak("There was an error adjusting the brightness.")
    else:
        speak("Brightness control is not supported on this OS.")



def process_command(command):
    """Process the command to control features."""
    if "bluetooth" in command:
        if "turn on" in command:
            toggle_bluetooth()
        elif "turn off" in command:
            toggle_bluetooth()  # Toggle logic can handle this internally

    elif "wifi" in command:
        if "turn on" in command:
            toggle_wifi()
        elif "turn off" in command:
            toggle_wifi()

    elif "night light" in command:
        if "turn on" in command:
            toggle_night_light()
        elif "turn off" in command:
            toggle_night_light()
    
    elif "airplane mode" in command:
        if "turn on" in command:
            toggle_airplane_mode()
        elif "turn off" in command:
            toggle_airplane_mode()

    elif "brightness" in command:
        adjust_brightness(command)

    elif "volume" in command:
        adjust_volume(command)

    else:
        speak("Sorry, I didn't understand the command.")


# Main function
if __name__ == "__main__":
    while True:
        command = listen_command()
        if command:
            process_command(command)
