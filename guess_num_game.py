import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def game(chances):
    number = random.randint(1, 100)
    while chances < 10:
        chances_left = 9 - chances
        guess = int(input(": "))
        if guess == number:
            speak("Congratulation YOU WON!!!")
            break

        elif guess < number:
            speak("Choose a larger number: ")
            print("Chances left : ", chances_left)

        else:
            speak("Choose a smaller number:")
            print("Chances left : ", chances_left)

        chances += 1

    if not chances < 10:
        speak("Sorry Sir, But YOU Lost!!!")
        print("The number is", number)
