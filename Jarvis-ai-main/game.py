import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 178)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def games():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")



# ///////////////////////////// ALL GAMES FROM CHAT GPT BELOW ////////////////////////////////////


# import random
# import pyttsx3
# import speech_recognition as sr

# # Initialize pyttsx3 engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 175)
# engine.setProperty('voice', engine.getProperty('voices')[0].id)

# def speak(text):
#     """Speak the given text."""
#     engine.say(text)
#     engine.runAndWait()

# def listen_command():
#     """Listen for a voice command from the user."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening for command...")
#         speak("Listening for command.")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
    
#     try:
#         command = recognizer.recognize_google(audio).lower()
#         print(f"You said: {command}")
#         return command
#     except sr.UnknownValueError:
#         speak("Sorry, I couldn't understand that.")
#         return ""
#     except sr.RequestError:
#         speak("Sorry, there was an issue with the speech recognition service.")
#         return ""

# # Your game functions here: rock_paper_scissors, spelling_bee, etc.
# # Add all the game functions, for example:

# # 1. Rock, Paper, Scissors Game
# def rock_paper_scissors():
#     choices = ["rock", "paper", "scissors"]
#     speak("Choose rock, paper, or scissors.")
    
#     user_choice = listen_command()
#     if user_choice not in choices:
#         speak("Invalid choice. Try again.")
#         return
    
#     computer_choice = random.choice(choices)
#     speak(f"Computer chooses: {computer_choice}")
    
#     if user_choice == computer_choice:
#         speak("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "scissors" and computer_choice == "paper") or \
#          (user_choice == "paper" and computer_choice == "rock"):
#         speak("You win!")
#     else:
#         speak("Computer wins!")

# # 2. Spelling Bee Game
# def spelling_bee():
#     words = ["apple", "banana", "grape", "orange", "watermelon"]
#     word = random.choice(words)
#     speak("Spell the word: " + word)
    
#     user_input = listen_command()
#     if user_input == word:
#         speak("Correct!")
#     else:
#         speak(f"Wrong! The correct spelling is {word}.")

# # 3. Animal Sounds Quiz
# def animal_sounds_quiz():
#     animal_sounds = {
#         "dog": "bark",
#         "cat": "meow",
#         "cow": "moo",
#         "sheep": "baa",
#         "duck": "quack"
#     }
    
#     animal, sound = random.choice(list(animal_sounds.items()))
#     speak(f"What sound does a {animal} make?")
    
#     user_input = listen_command()
#     if user_input == sound:
#         speak("Correct!")
#     else:
#         speak(f"Wrong! The correct sound is {sound}.")

# # 4. Math Challenge Game
# def math_challenge():
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     operation = random.choice(["+", "-"])
    
#     if operation == "+":
#         correct_answer = num1 + num2
#     else:
#         correct_answer = num1 - num2
    
#     speak(f"What is {num1} {operation} {num2}?")
    
#     user_answer = listen_command()
#     if user_answer.isdigit() and int(user_answer) == correct_answer:
#         speak("Correct!")
#     else:
#         speak(f"Wrong! The correct answer is {correct_answer}.")

# # 5. Guess the Song Game
# def guess_the_song():
#     songs = {
#         "Imagine": "Imagine there's no heaven, it's easy if you try...",
#         "Hey Jude": "Hey Jude, don't make it bad...",
#         "Bohemian Rhapsody": "Is this the real life? Is this just fantasy?"
#     }
    
#     song, lyrics = random.choice(list(songs.items()))
#     speak(f"Guess the song from these lyrics: {lyrics}")
    
#     user_guess = listen_command().title()
#     if user_guess == song:
#         speak("Correct!")
#     else:
#         speak(f"Wrong! The correct song was {song}.")

# # 6. Coin Toss Game
# def coin_toss():
#     speak("Heads or Tails?")
#     user_choice = listen_command()
#     if user_choice not in ["heads", "tails"]:
#         speak("Invalid choice.")
#         return
    
#     toss_result = random.choice(["heads", "tails"])
#     speak(f"The coin landed on {toss_result}.")
    
#     if user_choice == toss_result:
#         speak("You win!")
#     else:
#         speak("You lose!")

# # 7. Number Guessing Game
# def number_guess():
#     number = random.randint(1, 100)
#     speak("I have chosen a number between 1 and 100. Try to guess it!")
    
#     attempts = 0
#     while True:
#         user_input = listen_command()
#         if user_input.isdigit():
#             guess = int(user_input)
#             attempts += 1
            
#             if guess < number:
#                 speak("Too low!")
#             elif guess > number:
#                 speak("Too high!")
#             else:
#                 speak(f"Correct! It took you {attempts} attempts.")
#                 break
#         else:
#             speak("Please say a valid number.")

# def main():
#     speak("Welcome to the Voice Games!")
    
#     while True:
#         speak("Choose a game:")
#         speak("Say 'Rock Paper Scissors', 'Spelling Bee', 'Animal Sounds', 'Math Challenge', 'Guess the Song', 'Coin Toss', 'Number Guessing', or 'Exit'.")
        
#         command = listen_command()
        
#         if "rock paper scissors" in command:
#             rock_paper_scissors()
#         elif "spelling bee" in command:
#             spelling_bee()
#         elif "animal sounds" in command:
#             animal_sounds_quiz()
#         elif "math challenge" in command:
#             math_challenge()
#         elif "guess the song" in command:
#             guess_the_song()
#         elif "coin toss" in command:
#             coin_toss()
#         elif "number guessing" in command:
#             number_guess()
#         elif "exit" in command:
#             speak("Goodbye!")
#             break
#         else:
#             speak("Sorry, I didn't understand the command. Please try again.")

# if __name__ == "__main__":
#     main()