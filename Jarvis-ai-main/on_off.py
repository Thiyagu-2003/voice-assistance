import os
import pyttsx3
import speech_recognition as sr
import platform
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
        speak("I am listening for your command sir.")
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

def control_wifi(command):
    """Turn Wi-Fi on or off."""
    if platform.system() == "Windows":
        if "on" in command:
            os.system("netsh interface set interface Wi-Fi enabled")
            speak("Wi-Fi turned on.")
        elif "off" in command:
            os.system("netsh interface set interface Wi-Fi disabled")
            speak("Wi-Fi turned off.")
    else:
        speak("Wi-Fi control is not supported on this OS.")

def control_bluetooth(command):
    """Turn Bluetooth on or off."""
    if platform.system() == "Windows":
        if "on" in command:
            os.system("Start Bluetooth")
            speak("Bluetooth turned on.")
        elif "off" in command:
            os.system("Stop Bluetooth")
            speak("Bluetooth turned off.")
    else:
        speak("Bluetooth control is not supported on this OS.")


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
            elif "check brightness level" in command:
                speak(f"Current brightness is {current_brightness}%.")
            elif "set brightness to" in command:
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

    elif "check current volume level" in command:                # Check current volume level
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







import winreg

def control_night_light(command):
    """Turn Night Light mode on or off."""
    if platform.system() == "Windows":
        try:
            # Open the registry key
            key_path = r"Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\Cache\DefaultAccount"
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, key_path, 0, winreg.KEY_WRITE)

            # Set the Night Light state
            if "on" in command:
                data = b'\x02\x00\x00\x00'  # Binary data to enable Night Light
                winreg.SetValueEx(key, "$$windows.data.bluelightreduction.bluelightreductionstate", 0, winreg.REG_BINARY, data)
                speak("Night Light mode turned on.")
            elif "off" in command:
                data = b'\x01\x00\x00\x00'  # Binary data to disable Night Light
                winreg.SetValueEx(key, "$$windows.data.bluelightreduction.bluelightreductionstate", 0, winreg.REG_BINARY, data)
                speak("Night Light mode turned off.")

            winreg.CloseKey(key)
        except Exception as e:
            speak(f"Failed to change Night Light mode: {e}")
    else:
        speak("Night Light mode control is not supported on this OS.")


def process_command(command):
    """Process the command to control features."""
    if "wifi" in command:
        control_wifi(command)
    elif "bluetooth" in command:
        control_bluetooth(command)
    elif "brightness" in command:
        adjust_brightness(command)
    elif "volume" in command:
        adjust_volume(command)
    elif "night light" in command:
        control_night_light(command)
    else:
        speak("Sorry, I didn't understand the command.")
