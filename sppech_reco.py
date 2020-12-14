import pyttsx3  # pip install pyttsx3
import turtle
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
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as wrong:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def music_player():
    music_dir = "E:\\music"
    songs = os.listdir(music_dir)
    random_choice = random.randint(0, len(music_dir))
    # print(songs, "\n")
    os.startfile(os.path.join(music_dir, songs[random_choice]))


def calculator():
    class arthemetic_operations:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def add(self):
            return (self.x + self.y)

        def sub(self):
            return (self.x - self.y)

        def product(self):
            return (self.x * self.y)

        def divide(self):
            return (self.x / self.y)

        def power(self):
            return pow(self.x, self.y)

        def log(self):
            return log(self.x)

        def fac(self):
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

        elif 'game' in query:

            # snake_gamee
            delay = 0.1

            # scores
            score = 0
            high_score = 0

            # set up screen
            wn = turtle.Screen()
            wn.title("Snake Game")
            wn.bgcolor('yellow')
            wn.setup(width=600, height=600)
            wn.tracer(0)

            # snake head
            head = turtle.Turtle()
            head.speed(0)
            head.shape("square")
            head.color("black")
            head.penup()
            head.goto(0, 0)
            head.direction = "stop"

            # snake food
            food = turtle.Turtle()
            food.speed(0)
            food.shape("square")
            food.color("red")
            food.penup()
            food.goto(0, 100)

            segments = []

            # scoreboards
            sc = turtle.Turtle()
            sc.speed(0)
            sc.shape("square")
            sc.color("black")
            sc.penup()
            sc.hideturtle()
            sc.goto(0, 260)
            sc.write("score: 0  High score: 0", align="center", font=("ds-digital", 24, "normal"))


            # Functions
            def go_up():
                if head.direction != "down":
                    head.direction = "up"


            def go_down():
                if head.direction != "up":
                    head.direction = "down"


            def go_left():
                if head.direction != "right":
                    head.direction = "left"


            def go_right():
                if head.direction != "left":
                    head.direction = "right"


            def move():
                if head.direction == "up":
                    y = head.ycor()
                    head.sety(y + 20)
                if head.direction == "down":
                    y = head.ycor()
                    head.sety(y - 20)
                if head.direction == "left":
                    x = head.xcor()
                    head.setx(x - 20)
                if head.direction == "right":
                    x = head.xcor()
                    head.setx(x + 20)


            # keyboard bindings
            wn.listen()
            wn.onkeypress(go_up, "w")
            wn.onkeypress(go_down, "s")
            wn.onkeypress(go_left, "a")
            wn.onkeypress(go_right, "d")

            # MainLoop
            while True:
                wn.update()

                # check collision with border area
                if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"

                    # hide the segments of body
                    for segment in segments:
                        segment.goto(1000, 1000)  # out of range
                    # clear the segments
                    segments.clear()

                    # reset score
                    score = 0

                    # reset delay
                    delay = 0.1

                    sc.clear()
                    sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                             font=("ds-digital", 24, "normal"))

                # check collision with food
                if head.distance(food) < 20:
                    # move the food to random place
                    x = random.randint(-290, 290)
                    y = random.randint(-290, 290)
                    food.goto(x, y)

                    # add a new segment to the head
                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color("black")
                    new_segment.penup()
                    segments.append(new_segment)

                    # shorten the delay
                    delay -= 0.001
                    # increase the score
                    score += 10

                    if score > high_score:
                        high_score = score
                    sc.clear()
                    sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                             font=("ds-digital", 24, "normal"))

                    # move the segments in reverse order
                for index in range(len(segments) - 1, 0, -1):
                    x = segments[index - 1].xcor()
                    y = segments[index - 1].ycor()
                    segments[index].goto(x, y)
                # move segment 0 to head
                if len(segments) > 0:
                    x = head.xcor()
                    y = head.ycor()
                    segments[0].goto(x, y)

                move()

                # check for collision with body
                for segment in segments:
                    if segment.distance(head) < 20:
                        time.sleep(1)
                        head.goto(0, 0)
                        head.direction = "stop"

                        # hide segments
                        for segment in segments:
                            segment.goto(1000, 1000)
                        segments.clear()
                        score = 0
                        delay = 0.1

                        # update the score
                        sc.clear()
                        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                                 font=("ds-digital", 24, "normal"))
                time.sleep(delay)
            wn.mainloop()


        elif 'quit' in query:
            speak("Thanks for using us mam")
            sys.exit()

