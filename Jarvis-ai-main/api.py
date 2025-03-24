import speech_recognition as sr
import requests
import pyttsx3
from gtts import gTTS
import os
import webbrowser
import time
import json

# Initialize global variables
recognizer = sr.Recognizer()
engine = pyttsx3.init()
is_active = True

# Set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 175)  # Speed of speech

def speak(text):
    """Convert text to speech using pyttsx3 (works offline)"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
    
def speak_gtts(text):
    """Convert text to speech using gTTS (better quality but needs internet)"""
    print(f"Assistant: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # For Windows
    
def listen():
    """Listen for user voice input and convert to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=5)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
        
def process_command(command):
    """Process the voice command and call appropriate API function"""
    global is_active
    
    if "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye!")
        is_active = False
        return
        
    elif "pincode" in command or "pin code" in command or "postal code" in command:
        # Extract pincode from command
        words = command.split()
        for i, word in enumerate(words):
            if word.isdigit() and len(word) == 6:  # Indian pincodes are 6 digits 600054
                search_pincode(word)
                return
        speak("Please provide a valid 6-digit pincode.")
        
    elif "book" in command or "search book" in command:
        # Extract book name after "book" or "search book"
        if "book" in command:
            book_name = command.split("book", 1)[1].strip()
        else:
            book_name = command.split("search book", 1)[1].strip()
            
        if book_name:
            search_book(book_name)
        else:
            speak("What book would you like to search for?")
            
    elif "food" in command or "recipe" in command or "meal" in command:
        get_random_recipe()
        
    elif "lyrics" in command:
        if "by" in command:
            # Try to extract song and artist
            parts = command.split("lyrics", 1)[1].strip()
            if "by" in parts:
                song, artist = parts.split("by", 1)
                get_lyrics(artist.strip(), song.strip())
            else:
                speak("Please specify both song and artist. For example: get lyrics hello by adele")
        else:
            speak("Please specify both song and artist. For example: get lyrics hello by adele")
            
    elif "quote" in command or "inspiration" in command:
        get_quote()
        
    elif "fact" in command or "did you know" in command:
        get_fun_fact()
        
    elif "meaning" in command or "define" in command or "dictionary" in command:
        # Extract word to define
        words_to_check = ["meaning", "define", "dictionary"]
        for word in words_to_check:
            if word in command:
                word_to_define = command.split(word, 1)[1].strip()
                if word_to_define:
                    get_word_definition(word_to_define)
                    return
        speak("What word would you like me to define?")
        
    elif "barcode" in command or "bar code" in command:
        # Extract data for barcode
        if "for" in command:
            barcode_data = command.split("for", 1)[1].strip()
            if barcode_data:
                generate_barcode(barcode_data)
            else:
                speak("Please provide data for the barcode.")
        else:
            speak("Please specify what data to encode in the barcode.")
            
    elif "convert" in command and ("currency" in command or "dollar" in command or "usd" in command or "inr" in command):
        convert_currency()
        
    # Separated anime functionality into distinct command sections
    elif "anime character" in command:
        # Extract character name
        char_name = command.split("character", 1)[1].strip()
        if char_name:
            call_anime_character_api(char_name)
        else:
            speak("Which anime character would you like information about?")
    elif "anime quote" in command:
        call_anime_quote_api()
    elif "anime" in command:
        speak("Would you like an anime quote or character information? Please say 'anime quote' or 'anime character' followed by the name.")
            
    else:
        speak("I'm not sure how to help with that. You can ask me about pincodes, books, food recipes, lyrics, quotes, facts, word definitions, barcodes, currency conversion, or anime information.")

# API Functions
def search_pincode(pincode):
    """Search for pincode information"""
    try:
        url = f"https://api.postalpincode.in/pincode/{pincode}"
        response = requests.get(url).json()
        
        if response[0]["Status"] == "Success":
            area = response[0]['PostOffice'][0]['Name']
            district = response[0]['PostOffice'][0]['District']
            state = response[0]['PostOffice'][0]['State']
            speak(f"Pincode {pincode} belongs to {area} in {district} district, {state}.")
        else:
            speak("No information found for that pincode.")
    except Exception as e:
        speak("Sorry, I couldn't retrieve pincode information.")
        print(f"Error: {e}")

def search_book(book_name):
    """Search for book information"""
    try:
        url = f"https://www.googleapis.com/books/v1/volumes?q={book_name}"
        response = requests.get(url).json()
        
        if 'items' in response and len(response['items']) > 0:
            title = response['items'][0]['volumeInfo']['title']
            authors = ", ".join(response['items'][0]['volumeInfo'].get('authors', ['Unknown author']))
            description = response['items'][0]['volumeInfo'].get('description', 'No description available')
            
            # Truncate description if too long
            if len(description) > 200:
                description = description[:200] + "..."
                
            speak(f"I found {title} by {authors}. {description}")
        else:
            speak(f"Sorry, I couldn't find any books matching {book_name}.")
    except Exception as e:
        speak("Sorry, I couldn't retrieve book information.")
        print(f"Error: {e}")

def get_random_recipe():
    """Get a random recipe"""
    try:
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url).json()
        
        meal = response['meals'][0]['strMeal']
        category = response['meals'][0]['strCategory']
        area = response['meals'][0]['strArea']
        instructions = response['meals'][0]['strInstructions']
        
        # Truncate instructions if too long
        if len(instructions) > 200:
            instructions = instructions[:200] + "..."
            
        speak(f"Here's a random {area} {category} recipe: {meal}. {instructions}")
    except Exception as e:
        speak("Sorry, I couldn't retrieve a recipe.")
        print(f"Error: {e}")

def get_lyrics(artist, song):
    """Get lyrics for a song"""
    try:
        url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
        response = requests.get(url).json()
        
        if 'lyrics' in response:
            lyrics = response['lyrics']
            # Truncate lyrics to first few lines
            lyrics_preview = '\n'.join(lyrics.split('\n')[:6]) + "..."
            speak(f"Here are the lyrics for {song} by {artist}: {lyrics_preview}")
        else:
            speak(f"Sorry, I couldn't find lyrics for {song} by {artist}.")
    except Exception as e:
        speak("Sorry, I couldn't retrieve the lyrics.")
        print(f"Error: {e}")

def get_quote():
    """Get a random inspirational quote"""
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url).json()
        
        quote = response[0]['q']
        author = response[0]['a']
        speak(f"Here's your quote: {quote} - {author}")
    except Exception as e:
        speak("Sorry, I couldn't retrieve a quote.")
        print(f"Error: {e}")

def get_fun_fact():
    """Get a random fun fact"""
    try:
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url).json()
        
        fact = response['text']
        speak(f"Did you know? {fact}")
    except Exception as e:
        speak("Sorry, I couldn't retrieve a fun fact.")
        print(f"Error: {e}")

def get_word_definition(word):
    """Get the definition of a word"""
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url).json()
        
        if isinstance(response, list) and len(response) > 0:
            meaning = response[0]["meanings"][0]["definitions"][0]["definition"]
            part_of_speech = response[0]["meanings"][0]["partOfSpeech"]
            speak(f"The word '{word}' is a {part_of_speech}. It means: {meaning}")
        else:
            speak(f"Sorry, I couldn't find a definition for '{word}'.")
    except Exception as e:
        speak(f"Sorry, I couldn't find a definition for '{word}'.")
        print(f"Error: {e}")

def generate_barcode(data):
    """Generate a barcode for given data"""
    try:
        url = f"https://www.barcodes4.me/barcode/c128b/{data}.png"
        speak(f"Opening barcode for {data} in your browser.")
        webbrowser.open(url)
    except Exception as e:
        speak("Sorry, I couldn't generate the barcode.")
        print(f"Error: {e}")

def convert_currency():
    """Convert USD to INR"""
    try:
        url = "https://api.exchangerate.host/convert?from=USD&to=INR"
        response = requests.get(url).json()
        
        rate = response["result"]
        speak(f"The current exchange rate is 1 US Dollar equals {rate:.2f} Indian Rupees.")
    except Exception as e:
        speak("Sorry, I couldn't retrieve currency information.")
        print(f"Error: {e}")

# Separated anime functions
def call_anime_character_api(character_name):
    """Dedicated function to call the anime character API"""
    try:
        print(f"Searching for anime character: {character_name}")
        url = f"https://api.jikan.moe/v4/characters?q={character_name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['data']:
                character = data['data'][0]
                name = character['name']
                about = character['about']
                
                # Truncate description if too long
                if len(about) > 200:
                    about = about[:200] + "..."
                    
                speak(f"Here's information about {name}: {about}")
            else:
                speak(f"Sorry, I couldn't find information about {character_name}.")
        else:
            speak("Sorry, the anime API is not responding right now.")
    except Exception as e:
        speak("Sorry, I couldn't retrieve anime character information.")
        print(f"Error: {e}")

def call_anime_quote_api():
    """Dedicated function to call the anime quote API"""
    try:
        print("Fetching an anime quote")
        url = "https://animechan.xyz/api/random"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            quote = data['quote']
            character = data['character']
            anime = data['anime']
            
            speak(f"Here's an anime quote: {quote} - said by {character} from {anime}")
        else:
            speak("Sorry, the anime quotes API is not responding right now.")
    except Exception as e:
        speak("Sorry, I couldn't retrieve an anime quote.")
        print(f"Error: {e}")

def run():
    """Main function to run the voice assistant"""
    speak("Hello! I'm your voice assistant. How can I help you today?")
    
    global is_active
    while is_active:
        command = listen()
        if command:
            process_command(command)
        time.sleep(0.5)  # Small pause between commands

if __name__ == "__main__":
    print("Starting Voice Assistant...")
    print("Required packages: speech_recognition, pyttsx3, gtts, requests")
    print("Make sure you have a microphone connected and working.")
    print("Say 'exit', 'quit', or 'stop' to end the program.")
    print("\nAvailable commands:")
    print("- Pincode information: 'Find pincode 600099'")
    print("- Book search: 'Search book atomic habits'")
    print("- Random recipe: 'Get me a food recipe'")
    print("- Lyrics: 'Get lyrics hello by adele'")
    print("- Quotes: 'Give me an inspirational quote'")
    print("- Fun facts: 'Tell me a fun fact'")
    print("- Dictionary: 'What's the meaning of entrepreneur'")
    print("- Barcode: 'Generate barcode for mydata'")
    print("- Currency: 'Convert currency USD to INR'")
    print("- Anime character: 'Tell me about anime character Naruto'")
    print("- Anime quote: 'Get an anime quote'")
    
    run()