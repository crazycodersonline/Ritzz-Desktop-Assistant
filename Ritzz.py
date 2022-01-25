import pyttsx3
import os
import pyautogui
import datetime
import speech_recognition as sr
import wikipedia
from wikipedia.wikipedia import search
import webbrowser as wb
import cv2
# pyttsx3 is for Text to speech

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
newVoiceRate = 200  # Voice Speed
engine.setProperty('rate', newVoiceRate)


# Convert to audio
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def intro():
    intro = '''I am Rizz a desktop assistant with lots of functionalities,
i was created by Ritesh Sah in the year 2021 as a college project'''
    speak(intro)
# For date and Time
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("Current Date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    pyautogui.alert("Ritzz Activated")
    speak("Welcome back Sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Ritzz is now Activated., How can i help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening..")
        print("Listening...")
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("I didn't get you, Please Repeat...")

        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\screenshots\ss.png")

if __name__ == "__main__":

    wishme()

    while True:
        query = takecommand().lower()
        print(query)

        if "yourself" in query:
            intro()
        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "what can you do" in query:
            speak('''I can,  Search on Wikipedia with the command, 
            who is / what is / or simply saying wikipedia in searchterm, 
            i can play songs and take screenshot,  i can tell you the time and date,
            i can even shut down or restart or logout your computer ''')
        
        #os module
        elif "log out" in query:
            os.system("shutdown -l")
        elif "restart the laptop" in query:
            os.system("shutdown /r /t 1")
        elif "shutdown the laptop" in query:
            os.system("shutdown /s /t 1")
        
        #Volume controls
        elif "volume up" in query:
            pyautogui.press('volumeup')
        elif "volume down" in query:
            pyautogui.press('volumedown')
        elif "mute" in query:
            pyautogui.press('volumemute')
        
        elif "open camera" in query:
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
                cam.release()
                cv2.destroyAllWindows()

        #for Screenshot
        elif "screenshot" in query:
            screenshot()
            speak("screenshot captured and saved to screenshot folder")
        
        
        #searching on wikipedia 
        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)

        elif "what is" in query:
            speak("searching...")
            query = query.replace("what is", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "who is" in query:
            speak("searching...")
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        #Google Chrome Search
        #not  working need to fix raw string/chromepath 
        elif "search on google" in query:
            speak("what should i search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+ " .com")
        
        #Playing Songs
        elif "play song" in query:
            songs_dir = "D:\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        

        elif "offline" in query:
            speak("Good Bye Sir!, Have a Nice day")
            quit()
        
