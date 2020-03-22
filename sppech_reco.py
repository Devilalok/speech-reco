import speech_recognition as sr
import webbrowser as wb


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("[choose, google: youtube]")
    print("speak")
    audio = r3.listen(source)

if "youtube" in r3.recognize_google(audio):
    r2 = sr.Recognizer()
    url = "https://www.youtube.com/"

    with sr.Microphone() as source:
        print("search your query")
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("failed".format(e))

elif 'google' in r3.recognize_google(audio):
    r1 = sr.Recognizer()
    url = ""

    with sr.Microphone() as source:
        print("search your query")
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("failed".format(e))
