from pyttsx3 import Engine
import speech_recognition as sr
import pyttsx3
import pygame
from time import sleep
import datetime

listener = sr.Recognizer()
engine: Engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 171)
engine.setProperty('volume', 150)
engine.runAndWait()

def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}")
        return query

    except:
        return ""

    query = str(query)
    return query.lower()
def txt2hndwrtn(t,n):
    from PIL import Image, ImageDraw, ImageFont

    # Define the dimensions of an A4 page in pixels (300 DPI)
    A4_WIDTH = 2480
    A4_HEIGHT = 3508

    # Create a blank image in A4 size
    image = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), "white")
    draw = ImageDraw.Draw(image)

    # Specify a font and size for the handwritten style
    font = ImageFont.truetype("C:\\handwritten.ttf", size=70)  # Replace with the path to your desired font file

    import wikipedia

    # Get the title from the user
    user_title = t

    # Use the Wikipedia API to fetch the page content
    try:
        page = wikipedia.page(user_title)
        print("Title: ", page.title)

        # Get the number of lines from the user
        num_lines = int(n)

        # Display the desired number of lines
        lines = page.content.split('\n')[:num_lines]
        text =  page.title + "\n" +"\n"+"\n".join(lines)
    #     text=lines

    except wikipedia.exceptions.DisambiguationError as e:
        print("Please be more specific with your title.")
    except wikipedia.exceptions.PageError as e:
        print("The page does not exist. Please try another title.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print("An error occurred: ", e)


    # Position where the text will be drawn
    position = (50, 50)

    # Split the text into lines
    lines = text.split('\n')

    # Track the current line and width
    current_line = 0
    current_width = 0
    current_height = 50
    # ... (previous code remains unchanged)

    # Keep track of the current page
    current_page = 1
    # ... (previous code remains unchanged)

    # Draw the text on the image
    for line in lines:
        words = line.split()
        for word in words:
            word_bbox = draw.textbbox(position, word, font=font)
            word_width = word_bbox[2] - word_bbox[0]
            word_height = word_bbox[3] - word_bbox[1]
            if current_width + word_width > A4_WIDTH - 100:
                position = (50, position[1] + 100)
                current_width = 0
                current_line += 1
                if position[1] > A4_HEIGHT - 100:
                    image.save(f"C:\\handwritten\\handwritten_text_page_{current_page}.png")
                    current_page += 1
                    image = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), "white")
                    draw = ImageDraw.Draw(image)
                    position = (50, 50)
            draw.text(position, word, fill="black", font=font)
            word_width_with_space = word_width + 20  # Adjust the value to your preference for word spacing
            position = (position[0] + word_width_with_space, position[1])  # Add space between words
            current_width += word_width_with_space

        position = (50, position[1] + 100)
        current_line += 1
        current_width = 0

    # Save the final image
    image.save(f"C:\\handwritten\\handwritten_text_page_{current_page}.png")


    from fpdf import FPDF
    import os

    # Directory containing the handwritten images
    image_directory = "C:\\handwritten"

    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Iterate through each image in the directory
    for image_file in os.listdir(image_directory):
        if image_file.endswith(".png"):
            pdf.add_page()
            pdf.image(os.path.join(image_directory, image_file), x=0, y=0, w=210, h=297)

    # Save the PDF
    pdf.output("C:\\handwritten\\handwritten_text.pdf", "F")


    file_path = "C:\\handwritten\\handwritten_text.pdf"
    os.startfile(file_path)
def main():
    while True:
        command = take_command()
        if "hi" in command:
            talk("Hello")
        elif "assignments" in command:
            talk("Please mention your title.")
            t=take_command()
            txt2hndwrtn(t,50)
            break
        elif "sleep" in command:
            break