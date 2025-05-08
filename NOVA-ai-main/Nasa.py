import requests                     # all working fine
from PIL import Image
import os
import pyttsx3

# NASA API Key
Api_key = " NASA API Key" # Replace with your actual API key
# Note: You can get a free API key from NASA's website if you don't have one.

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 172)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latest_space_news():
    speak('Connecting to NASA API to fetch the latest space news...')

    try:
        # NASA API endpoint for the latest news
        Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)

        # Make API request
        r = requests.get(Url)
        if r.status_code != 200:
            speak("Unable to fetch data from NASA. Please try again later.")
            return

        Data = r.json()

        # Extract relevant data
        Info = Data.get('explanation', "No information available.")
        Title = Data.get('title', "No title available.")
        Image_Url = Data.get('url', None)

        if not Image_Url:
            speak("No image available for the latest news.")
            return

        # Fetch the image
        Image_r = requests.get(Image_Url)
        if Image_r.status_code != 200:
            speak("Unable to fetch the image. Please try again later.")
            return

        # Save the image
        FileName = "latest_space_news.jpg"
        Save_Path = os.path.join(os.getcwd(), "NasaImages")
        os.makedirs(Save_Path, exist_ok=True)  # Ensure the directory exists
        FilePath = os.path.join(Save_Path, FileName)

        with open(FilePath, 'wb') as f:
            f.write(Image_r.content)

        # Open the image
        img = Image.open(FilePath)
        img.show()

        # Speak the results
        speak(f"Title: {Title}")
        speak(f"According to NASA: {Info}")

    except Exception as e:
        speak("An error occurred while fetching the latest space news.")
        print(f"Error: {e}")

