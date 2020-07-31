import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import random
from guess_num_game import game

music_no = random.randint(0, 17)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. How can I help you.")


def intro_game():
    speak("Let me introduce with the rules of the game.")
    speak("You have to guess a number in 10 chances.")
    speak("If you succesfully guesed the number you will win. else, game will be over and you lose.")

def the_game(chances):
    speak("Guess the number between 0 and 100")
    game(chances) 

def takeCommand():
    # It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recogonising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:

        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query.

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'  
            songs =os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[music_no]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play a game' in query:
            speak("Sir, would you like to play a number guessing game ??")
            
            query = takeCommand().lower()
            if 'yes' in query:
                speak("ok")
                intro_game()
                the_game(0)
                
            elif 'no' in query:
                speak("Ok sir, we will play it later")

        elif 'continue the game' in query:
            the_game(0)

        elif 'thank you' in query:
            speak("Its my duty sir.")

        elif 'quit' in query:
            speak("Thank you for using me. Hope you have a good day.")
            exit()