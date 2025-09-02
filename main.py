import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
import wikipedia # type: ignore
import pywhatkit # pyright: ignore[reportMissingImports]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content =" "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio)
            print(f"listning...")
        except Exception as e:
            print("something went wrong please say again.")

    return content

def mainprocess():
    while True:
        request = command().lower()
        if "jarvis" in request:
            speak("yes how can i help you")
        elif "play music" in request:
            speak("playing music")   
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://youtu.be/BFGpnsSRHjg?t=1")
            elif song == 2:
                webbrowser.open("https://youtu.be/pCG5jVC8ECE?t=1")
            elif song == 3:
                webbrowser.open("https://youtu.be/QVtaRnA-TWE?t=3")
        elif "show time" in request:
            nowtime = datetime.datetime.now().strftime("%H:%M")
            speak (f"The current time is {nowtime}")
        elif "show date" in request:
            nowtime = datetime.datetime.now().strftime("%d:%m")
            speak (f"The current date is {nowtime}")    
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open google" in request:
            webbrowser.open("www.google.com")  
        elif "open facebook" in request:
            webbrowser.open("www.facbook.com")
        elif "open instagram" in request:
            webbrowser.open("www.instagram.com")    
        elif "search wikipedia" in request:
            request = request.replace("jarvis","")
            request = request.replace("search wikipedia", "")
            print(request)
            result = wikipedia.summary(request, sentences=2)  
            print(result)            
            speak(result)
        elif "search google" in request:
            request = request.replace("jarvis","")
            request = request.replace("search google", "")
            webbrowser.open(f"https://www.google.com/search?q={request}")
        elif "send whatsapp" in request:
            # Send a WhatsApp Message to a Contact at 1:30 PM
            pywhatkit.sendwhatmsg("+923053469691", "hn lopy", 16,35,10)

mainprocess()

