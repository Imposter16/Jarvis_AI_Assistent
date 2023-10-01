import pyttsx3
import datetime

# text to speech
# Speech to text
import speech_recognition as sr
import wikipedia
import smtplib  # liberary for generating e-mail
import webbrowser as wb
import os  # for shutdown and all
import pyautogui  # this is used to take SS
import psutil  # for battery% and Task man.
import pyjokes  # library for Jokes


engine = pyttsx3.init()
# engine.say("Hello Saurabh, This is JARVIS How may i help u")
# engine.runAndWait()


# ----------- Another method using function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("    Hello Saurabh, This is JARVIS")


# date time function
def time():
    speak("The current time is ")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


# time()


# Date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")

    speak(date)
    speak(month)
    speak(year)


# date()


# Greet fn
def wishme():
    speak("    How may i help you sir!")
    # speak("The current date is ")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")

    time()


# wishme()


# ----------Speech Recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)

        speak("please say it again sir! ")
        return "None"
    return query


# takeCommand()

# ------ for sending mail


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("saurabhverma.stdnt@srmu.ac.in", "Saurabh@1234")
    server.sendmail("saurabhverma.stdnt@srmu.ac.in", to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\AI Assistant JARVIS\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("Your battery is at ")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


# --------using main function----------

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "saurabhkumarverma025@gmail.com"
                sendEmail(to, content)
                speak("E-mail has been send")
            except Exception as e:
                print(e)
                speak("Unable to send E-mail")

        # ---- To search on Google Chrome
        elif "search in chrome" in query:
            speak("What you want to search?")
            chromepath = "C:\Program Files\Google\Chrome\Application"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "restart" in query:
            speak("Restarting soon....")
            os.system("restarting  /r /t 1")

        elif "logout" in query:
            speak("Loging out soon....")
            os.system("shutdown /r /t -1")

        elif "shutdown" in query:
            speak("shuting down soon....")
            os.system("shutdown /s /t 1")

        elif "play song" in query:
            songs_dir = "D:\\"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said me to remember that is " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("SS Captured")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "offline" in query:
            quit()
