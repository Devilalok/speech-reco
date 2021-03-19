import pyttsx3  # pip install pyttsx3
import pyaudio
import speech_recognition as sr  # pip install speechRecognition
import time
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random
import smtplib
import sys
from math import *

engine = pyttsx3.init('sapi5')

""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


def speak(audio):  # use to convertt text into speech
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # wish me function to wish according time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am sanam mam. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #threshold frequency set to  1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as wrong:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):  #function used to send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password') #user sender email and passward place of email and passward
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def music_player():  #function to play music
    music_dir = "E:\\music" #location od music folder (full directory)
    songs = os.listdir(music_dir)
    random_choice = random.randint(0, len(music_dir)) #use random function to play any song  in the directory.
    # print(songs, "\n")
    os.startfile(os.path.join(music_dir, songs[random_choice]))


def calculator(): #simple calculator to do operation on two numbers.
    class arthemetic_operations:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def add(self): #Add two function
            return (self.x + self.y)

        def sub(self):  #Substraction
            return (self.x - self.y)

        def product(self):  #multiply
            return (self.x * self.y)

        def divide(self):   #divide
            return (self.x / self.y)

        def power(self):    #power
            return pow(self.x, self.y)

        def log(self):  #log value
            return log(self.x)

        def fac(self):  #factorial
            return factorial(self.x)

    speak("Please read instructions carefully")
    print("This calculator only use two number operations. ")
    print("Note: log, factorial, and fabonicci series only take one argument. so another argument give as 0 ")
    print("Note 2: you can enter numbers by keyboard\n")

    while True:

        number1 = int(input("Enter the number1: "))
        number2 = int(input("Enter the number2: "))

        res = arthemetic_operations(number1, number2)
        print("\n")

        speak("Choice the option in follwoing:")
        print("Press 1 for Addition")
        print("Press 2 for substration")
        print("Press 3 for multiply")
        print("Press 4 for divide")
        print("Press 5 for power")
        print("Press 6 for log")
        print("Press 7 for factorial")
        print("Press 0 to quit\n")

        user_choice = int(input("Enter what you want to do: "))
        if user_choice == 1:
            print("The answer is: ", res.add(), "\n")
            speak(f"The answer is: {res.add()}")

        elif user_choice == 2:
            print("The answer is: ", res.sub(), "\n")
            speak(f"The answer is: {res.sub()}")

        elif user_choice == 3:
            print("The answer is: ", res.product(), "\n")
            speak(f"The answer is: {res.product()}")

        elif user_choice == 4:
            print(res.divide(), "\n")
            speak(f"The answer is: {res.divide()}")

        elif user_choice == 5:
            print("The answer is: ", res.power(), "\n")
            speak(f"The answer is: {res.power()}")

        elif user_choice == 6:
            print("The answer is: ", res.log(), "\n")
            speak(f"The answer is: {res.log()}")

        elif user_choice == 7:
            print("The answer is: ", res.fac(), "\n")
            speak(f"The answer is: {res.fac()}")

        elif user_choice == 0:
            break


if __name__ == "__main__":

    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_player()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam, the time is {strTime}")

        elif 'open calculator' in query:
            calculator()

            # elif 'open code' in query:
        #     codePath = 'C:\\Users\\alokk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        #     os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "reciver email"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak("Sorry  mam. I am not able to send this email")


        elif 'quit' in query:  #To quit the program
            speak("Thanks for using us mam")
            sys.exit()
