import os
import webbrowser
import pyttsx3
import psutil
import pyautogui
import time
import platform
import logging
import speech_recognition as sr

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Dictionary of websites
websites = {
    "youtube": "www.youtube.com",
    "facebook": "www.facebook.com",
    "github": "www.github.com",
    "youtube studio": "studio.youtube.com",
    "twitter": "www.twitter.com",
    "instagram": "www.instagram.com",
    "linkedin": "www.linkedin.com",
    "wikipedia": "www.wikipedia.org",
    "reddit": "www.reddit.com",
    "pinterest": "www.pinterest.com",
    "quora": "www.quora.com",
    "tumblr": "www.tumblr.com",
    "flickr": "www.flickr.com",
    "snapchat": "www.snapchat.com",
    "tiktok": "www.tiktok.com",
    "vimeo": "www.vimeo.com",
    "dropbox": "www.dropbox.com",
    "onedrive": "www.onedrive.com",
    "google drive": "drive.google.com",
    "icloud": "www.icloud.com",
    "amazon": "www.amazon.com",
    "ebay": "www.ebay.com",
    "alibaba": "www.alibaba.com",
    "netflix": "www.netflix.com",
    "hulu": "www.hulu.com",
    "disney plus": "www.disneyplus.com",
    "hbo max": "www.hbomax.com",
    "spotify": "www.spotify.com",
    "soundcloud": "www.soundcloud.com",
    "apple music": "www.apple.com/apple-music",
    "pandora": "www.pandora.com",
    "deezer": "www.deezer.com",
    "bandcamp": "www.bandcamp.com",
    "bbc": "www.bbc.com",
    "cnn": "www.cnn.com",
    "nytimes": "www.nytimes.com",
    "the guardian": "www.theguardian.com",
    "forbes": "www.forbes.com",
    "bloomberg": "www.bloomberg.com",
    "reuters": "www.reuters.com",
    "espn": "www.espn.com",
    "fox news": "www.foxnews.com",
    "nbc news": "www.nbcnews.com",
    "cbs news": "www.cbsnews.com",
    "abc news": "www.abcnews.go.com",
    "msnbc": "www.msnbc.com",
    "npr": "www.npr.org",
    "wsj": "www.wsj.com",
    "yahoo news": "news.yahoo.com",
    "buzzfeed": "www.buzzfeed.com",
    "huffpost": "www.huffpost.com",
    "canva": "www.canva.com",
    "chatgpt": "chat.openai.com",
    "slack": "www.slack.com",
    "trello": "www.trello.com",
    "asana": "www.asana.com",
    "zoom": "www.zoom.us",
    "skype": "www.skype.com",
    "microsoft teams": "www.microsoft.com/microsoft-teams",
    "google meet": "meet.google.com",
    "webex": "www.webex.com",
    "jira": "www.atlassian.com/software/jira",
    "notion": "www.notion.so",
    "airtable": "www.airtable.com",
    "monday": "www.monday.com",
    "clickup": "www.clickup.com",
    "dropbox paper": "www.dropbox.com/paper",
    "confluence": "www.atlassian.com/software/confluence",
    "figma": "www.figma.com",
    "adobe xd": "www.adobe.com/products/xd.html",
    "invision": "www.invisionapp.com",
    "microsoft word": "www.microsoft.com/microsoft-365/word",
    "google docs": "docs.google.com",
    "medium": "www.medium.com",
    "wordpress": "www.wordpress.com",
    "wix": "www.wix.com",
    "squarespace": "www.squarespace.com",
    "shopify": "www.shopify.com",
    "bigcommerce": "www.bigcommerce.com",
    "weebly": "www.weebly.com",
    "godaddy": "www.godaddy.com",
    "namecheap": "www.namecheap.com",
    "bluehost": "www.bluehost.com",
    "siteground": "www.siteground.com",
    "hostgator": "www.hostgator.com",
    "dreamhost": "www.dreamhost.com",
    "a2 hosting": "www.a2hosting.com",
    "inmotion hosting": "www.inmotionhosting.com",
    "digitalocean": "www.digitalocean.com",
    "linode": "www.linode.com",
    "aws": "aws.amazon.com",
    "azure": "azure.microsoft.com",
    "google cloud": "cloud.google.com",
    "heroku": "www.heroku.com",
    "gitlab": "www.gitlab.com",
    "bitbucket": "bitbucket.org",
    "codepen": "codepen.io",
    "jsfiddle": "jsfiddle.net",
    "repl.it": "repl.it",
    "stack overflow": "stackoverflow.com",
    "stackoverflow careers": "stackoverflow.com/jobs",
    "glassdoor": "www.glassdoor.com",
    "indeed": "www.indeed.com",
    "linkedin jobs": "www.linkedin.com/jobs",
    "monster": "www.monster.com",
    "simplyhired": "www.simplyhired.com",
    "angel.co": "angel.co",
    "github jobs": "jobs.github.com",
    "ziprecruiter": "www.ziprecruiter.com",
    "careerbuilder": "www.careerbuilder.com",
    "snagajob": "www.snagajob.com",
    "dice": "www.dice.com",
    "jobs": "www.jobs.com",
    "bamboohr": "www.bamboohr.com",
    "workday": "www.workday.com",
    "adp": "www.adp.com",
    "sap successfactors": "www.sap.com/products/hcm.html",
    "oracle hcm": "www.oracle.com/applications/human-capital-management",
    "zenefits": "www.zenefits.com",
    "paycor": "www.paycor.com",
    "paycom": "www.paycom.com",
    "gusto": "www.gusto.com",
    "square": "squareup.com",
    "stripe": "www.stripe.com",
    "paypal": "www.paypal.com",
    "venmo": "www.venmo.com",
    "cash app": "cash.app",
    "robinhood": "www.robinhood.com",
    "etrade": "www.etrade.com",
    "fidelity": "www.fidelity.com",
    "charles schwab": "www.schwab.com",
    "vanguard": "investor.vanguard.com",
    "td ameritrade": "www.tdameritrade.com",
    "coinbase": "www.coinbase.com",
    "binance": "www.binance.com",
    "kraken": "www.kraken.com",
    "blockchain": "www.blockchain.com",
    "gemini": "www.gemini.com",
    "bitfinex": "www.bitfinex.com",
    "bitstamp": "www.bitstamp.net",
    "bittrex": "www.bittrex.com",
    "okex": "www.okex.com",
    "poloniex": "www.poloniex.com",
    "coindesk": "www.coindesk.com",
    "cointelegraph": "www.cointelegraph.com",
    "decrypt": "www.decrypt.co",
    "cryptoslate": "www.cryptoslate.com",
    "cryptonews": "www.cryptonews.com",
    "coinmarketcap": "www.coinmarketcap.com",
    "coingecko": "www.coingecko.com",
    "messari": "www.messari.io",
    "icodrops": "www.icodrops.com",
    "tokenmarket": "www.tokenmarket.net",
    "coinpaprika": "www.coinpaprika.com",
    "cryptocompare": "www.cryptocompare.com",
    "coincheckup": "www.coincheckup.com",
    "cryptobriefing": "www.cryptobriefing.com",
    "blockonomi": "www.blockonomi.com",
    "coininsider": "www.coininsider.com",
    "newsbtc": "www.newsbtc.com",
    "bitcoin.com": "www.bitcoin.com",
    "ethereum.org": "www.ethereum.org",
    "litecoin.com": "www.litecoin.com",
    "ripple.com": "www.ripple.com",
    "cardano.org": "www.cardano.org",
    "stellarlumens.com": "www.stellarlumens.com",
    "tezos.com": "www.tezos.com",
    "eos.io": "www.eos.io",
    "neo.org": "www.neo.org",
    "iota.org": "www.iota.org",
    "monero.org": "www.monero.org",
    "zcash.org": "www.zcash.org",
    "dash.org": "www.dash.org",
    "dogecoin.com": "www.dogecoin.com",
    "gpt": "www.chatgpt.com/",
    "gmail": "mail.google.com",
    "whatsapp": "web.whatsapp.com",
    "discord": "discord.com"
}

# Dictionary of system applications
system_apps = {
    "notepad": "notepad",
    "paint": "mspaint",
    "explorer": "explorer",
    "settings": "start ms-settings:",
    "chrome": "start chrome",
    "word": "start winword",
    "excel": "start excel",
    "powerpoint": "start powerpnt",
    "calculator": "calc",
    "terminal": "cmd",
    "control panel": "control",
    "task manager": "taskmgr"
}

def speak(text):
    """Speak the given text."""
    logging.info(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Capture voice command from the user."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your command...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            logging.info(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting. Please try again later.")
            return ""
        except Exception as e:
            speak("An error occurred while capturing your command.")
            logging.error(f"Error in listen_command: {e}")
            return ""

def open_website(website_name):
    """Open a website from the predefined list."""
    # Convert the website name to lowercase and remove extra spaces
    website_name = website_name.lower().strip()
    
    # Check if the website name is in the dictionary
    if website_name in websites:
        # Open the website
        url = websites[website_name]
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        webbrowser.open(url)
        speak(f"Opening {website_name}...")
        logging.info(f"Opening website: {website_name} - {url}")
        return True
    else:
        speak(f"Website '{website_name}' not found in the list.")
        logging.info(f"Website not found: {website_name}")
        return False

def open_system_app(app_name):
    """Open a system application from the predefined list."""
    app_name = app_name.lower().strip()
    if app_name in system_apps:
        command = system_apps[app_name]
        speak(f"Opening {app_name}...")
        try:
            os.system(command)
            logging.info(f"Opening system app: {app_name} with command: {command}")
            return True
        except Exception as e:
            speak(f"Failed to open {app_name}.")
            logging.error(f"Error opening {app_name}: {e}")
            return False
    else:
        speak(f"Application '{app_name}' not found in the list.")
        logging.info(f"Application not found: {app_name}")
        return False

def close_application(app_name):
    """Close the specified application."""
    app_name = app_name.lower().strip()
    speak(f"Attempting to close {app_name}.")
    try:
        found = False
        for proc in psutil.process_iter(attrs=['name']):
            proc_name = proc.info['name'].lower()
            if app_name in proc_name:
                proc.kill()
                found = True
                
        if found:
            speak(f"{app_name} has been closed.")
            logging.info(f"{app_name} process terminated.")
            return True
        else:
            speak(f"No running process found for {app_name}.")
            logging.info(f"No process found for: {app_name}")
            return False
    except Exception as e:
        speak("Unable to close the application.")
        logging.error(f"Error closing {app_name}: {e}")
        return False
    
def close_website(website_name=None):
    """Close a website browser tab.
    
    If website_name is None, closes the current tab.
    Otherwise, attempts to find and close tabs for the specified website.
    """
    if website_name:
        speak(f"Attempting to close {website_name} tab.")
        # For now, just close the current tab as it's difficult to
        # identify which tab contains a specific website
        pyautogui.hotkey('ctrl', 'w')
        logging.info(f"Attempted to close tab for: {website_name}")
    else:
        speak("Closing current website tab.")
        pyautogui.hotkey('ctrl', 'w')
        logging.info("Closed current browser tab")
    
    return True

def type_in_app():
    """Handle typing in the currently open application."""
    speak("I am ready to type. Please start speaking.")
    while True:
        command = listen_command()
        if not command:
            continue
        if "stop typing" in command:
            speak("Exiting typing mode.")
            break
        else:
            pyautogui.write(command)
            logging.info(f"Typed: {command}")

def save_file():
    """Handle saving a file with a user-specified name."""
    speak("Please specify a name for the file.")
    file_name = listen_command()
    if file_name:
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.write(file_name)
        pyautogui.press('enter')
        speak(f"File has been saved as {file_name}.")
        logging.info(f"File saved as: {file_name}")
    else:
        speak("File name not provided. Unable to save the file.")
        logging.info("File save canceled - no name provided")

def send_message():
    """Handle typing and sending a message in social media apps."""
    speak("I am ready to type your message. Please start speaking.")
    message_content = ""
    while True:
        command = listen_command()
        if not command:
            continue
        if "send message" in command or "stop typing" in command:
            speak("Sending your message.")
            pyautogui.press('enter')
            logging.info(f"Message sent: {message_content}")
            break
        else:
            pyautogui.write(command)
            message_content += command + " "
            logging.info(f"Added to message: {command}")
    
def process_command(command):
    """Process the user's voice command."""
    if not command:
        return True
        
    command = command.lower().strip()
    
    # Website open commands
    if "open" in command and any(site in command for site in websites.keys()):
        for site in websites.keys():
            if site in command:
                return open_website(site)
    
    # Website close commands
    elif "close" in command and any(site in command for site in websites.keys()):
        for site in websites.keys():
            if site in command:
                speak(f"Closing {site}...")
                pyautogui.hotkey('ctrl', 'w')
                logging.info(f"Closing website tab for: {site}")
                return True
                
    # Application commands
    elif "open" in command and any(app in command for app in system_apps.keys()):
        for app in system_apps.keys():
            if app in command:
                return open_system_app(app)
    
    # Generic open commands
    elif command.startswith("open "):
        item = command.replace("open ", "").strip()
        # Try as website first
        if open_website(item):
            return True
        # Then try as app
        if open_system_app(item):
            return True
        speak(f"I don't know how to open {item}.")
        return True
        
    # Close current tab command
    elif command == "close tab" or command == "close current website":
        speak("Closing current website tab.")
        pyautogui.hotkey('ctrl', 'w')
        logging.info("Closed current browser tab")
        return True
        
    # Generic close commands
    elif command.startswith("close "):
        app_name = command.replace("close ", "").strip()
        return close_application(app_name)
    
    # Type command
    elif command == "start typing" or command == "type":
        type_in_app()
        return True
        
    # Save command
    elif command == "save file" or command == "save":
        save_file()
        return True
        
    # Message command
    elif command == "compose message" or command == "new message":
        send_message()
        return True
    
    # Help command
    elif command == "help" or command == "what can you do":
        display_help()
        return True
    
    # Exit command
    elif command == "exit" or command == "quit" or command == "stop" or command == "shutdown":
        speak("Exiting the voice assistant. Goodbye!")
        return False
    
    else:
        speak("I don't understand that command. Say 'help' for available commands.")
        return True

def display_help():
    """Display and speak available commands."""
    help_text = """
    Available voice commands:
    - 'Open [website name]': Opens a website
    - 'Close [website name]': Closes a specific website tab
    - 'Close tab' or 'Close current website': Closes the current browser tab
    - 'Open [app name]': Opens a system application
    - 'Close [app name]': Closes a running application
    - 'Start typing': Enters typing mode for the current application
    - 'Save file': Initiates the save file procedure
    - 'Compose message': Enters message composition mode
    - 'Help' or 'What can you do': Displays this help message
    - 'Exit', 'Quit', or 'Stop': Exits the application
    """
    print(help_text)
    speak("Here are some commands you can use:")
    speak("Say open followed by a website name to open it")
    speak("Say close followed by a website name to close that website")
    speak("Say close tab to close the current browser tab")
    speak("Say open followed by an application name to open it")
    speak("Say close followed by an application name to close it")
    speak("Say start typing to enter text in the current application")
    speak("Say save file to save your work")
    speak("Say compose message to write and send a message")
    speak("Say exit or quit to close this voice assistant")
    logging.info("Help displayed")

def main():
    """Main function to run the voice assistant."""
    speak("Voice Assistant activated. Say 'help' or 'what can you do' to learn available commands.")
    print("="*50)
    print("Voice Assistant - Listening for commands")
    print("Say 'help' for available commands")
    print("="*50)
    
    running = True
    while running:
        command = listen_command()
        running = process_command(command)

if __name__ == "__main__":
    main()