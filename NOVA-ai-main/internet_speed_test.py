import speedtest
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def check_internet_speed():
    try:
        speak("checking internet speed please wait for a moment sir ")
        wifi = speedtest.Speedtest()
        wifi.get_best_server()  # Finds the optimal server
        upload_net = wifi.upload() / 1048576  # Convert bytes to MB
        download_net = wifi.download() / 1048576  # Convert bytes to MB
        
        upload_net = round(upload_net, 2)
        download_net = round(download_net, 2)
        
        print(f"Wifi Upload Speed is {upload_net} MB/s")
        print(f"Wifi Download Speed is {download_net} MB/s")
        
        speak(f"Wifi download speed is {download_net} MB per second")
        speak(f"Wifi upload speed is {upload_net} MB per second")
    except Exception as e:
        print(f"Error: {e}")
        speak("There was an error while checking the internet speed.")
