import pyautogui
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice (female in this case, adjust as needed)
engine.setProperty("rate", 178)  # Set speaking rate

def speak(audio):
    """Speak the provided text."""
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

def scroll_up():
    """Scroll up by pressing the Up arrow key five times."""
    try:
        pyautogui.press('up', presses=5)
    except Exception as e:
        print(f"Error in scroll_up function: {e}")

def scroll_down():
    """Scroll down by pressing the Down arrow key five times."""
    try:
        pyautogui.press('down', presses=5)
    except Exception as e:
        print(f"Error in scroll_down function: {e}")

def scroll_to_top():
    """Scroll to the top of the page."""
    try:
        pyautogui.hotkey('home')
    except Exception as e:
        print(f"Error in scroll_to_top function: {e}")

def scroll_to_bottom():
    """Scroll to the bottom of the page."""
    try:
        pyautogui.hotkey('end')
    except Exception as e:
        print(f"Error in scroll_to_bottom function: {e}")

def perform_scroll_action(command):
    """Perform scroll actions based on the provided voice command."""
    command = command.lower()  # Make input case-insensitive
    try:
        if "scroll up" in command or "mela poo" in command:
            scroll_up()
        elif "scroll down" in command or "kela va" in command:
            scroll_down()
        elif "scroll to top" in command or "top ku poo" in command:
            scroll_to_top()
        elif "scroll to bottom" in command or "bottom ku va" in command:
            scroll_to_bottom()
        else:
            speak("Command not recognized. Please try again.")
    except Exception as e:
        print(f"Error in perform_scroll_action function: {e}")

def take_voice_command():
    """Listen to the user's voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command.")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language='en-in')
            return command
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Please speak clearly.")
        except Exception as e:
            print(f"Error in take_voice_command function: {e}")
    return ""

def open_new_tab():
    pyautogui.hotkey('ctrl', 't')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def open_browser_menu():
    pyautogui.hotkey('alt', 'f')

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def open_bookmarks():
    pyautogui.hotkey('ctrl', 'b')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def open_dev_tools():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def toggle_full_screen():
    pyautogui.hotkey('f11')

def open_private_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')

def perform_browser_action(text):
    if "add new tab" in text or "new tab" in text:
        open_new_tab()
    elif "close tab" in text or "closetab" in text:
        close_tab()
    elif "go to browser menu" in text or "browser menu " in text:
        open_browser_menu()
    elif "zoom in" in text or "zoomin" in text:
        zoom_in()
    elif "zoom out" in text or "zoomout" in text:
        zoom_out()
    elif "refresh page" in text or "refresh the page" in text:
        refresh_page()
    elif "switch to next tab" in text or "next tab" in text:
        switch_to_next_tab()
    elif "switch to previous tab" in text or "previous tab" in text:
        switch_to_previous_tab()
    elif "open history" in text or "go to history" in text:
        open_history()
    elif "bookmarks" in text or "go to bookmarks" in text:
        open_bookmarks()
    elif "go back" in text or "goback" in text:
        go_back()
    elif "go forward" in text or "goforward" in text:
        go_forward()
    elif "open dev tools" in text or "go to dev tools " in text:
        open_dev_tools()
    elif "toggle full screen" in text or "togglefullscreen" in text:
        toggle_full_screen()
    elif "open private window" in text or " go to private window" in text:
        open_private_window()
    else:
        pass

# Main program loop
if __name__ == "__main__":
    speak("Voice control activated. Please say a command.")
    while True:
        command = take_voice_command()
        if command:
            if "exit" in command or "quit" in command:
                speak("Exiting. Goodbye!")
                break
            if any(word in command for word in ["scroll up", "scroll down", "scroll to top", "scroll to bottom"]):
                perform_scroll_action(command)
            else:
                perform_browser_action(command)

