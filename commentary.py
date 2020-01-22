<<<<<<< HEAD
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from selenium import webdriver
import smtplib
import time 
from pycricbuzz import Cricbuzz
def cricCommentry():
        c = Cricbuzz()
        matches = c.matches()
        # for match in matches:
        match=matches[0]
        # print( match)
        # if(match['mchstate'] != 'nextlive'):
        #         print (c.livescore(match['id']))
        #         print( c.commentary(match['id']))
        #         print( c.scorecard(match['id']))
        print('sun',c.commentary(match['id'])['commentary'][0]['comm'])
        a,b=c.commentary(match['id'])['commentary'][0]['comm'],''
        while(1):
                if(a!=b):
                        # speak(a)
                        d=c.scorecard(match['id'])['scorecard']
                        speak(a)
                        speak(d[0]['batteam']+'score is '+d[0]['runs']+'for'+d[0]['wickets']+'wickets')
                        b=a
                else:
                        a=c.commentary(match['id'])['commentary'][0]['comm']

browser = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe') 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    speak("Hello Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

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
            # webbrowser.open("youtube.com")
            print("hi")
            browser.get('https://www.youtube.com/') 
            speak("what do you want to search on youtube")
            query1 = takeCommand().lower()
            search=browser.find_element_by_id('search')
            search.send_keys(query1) 
            sbutton=browser.find_element_by_id('search-icon-legacy')
            # browser.find_elements_by_xpath()
            sbutton.click()
            video=browser.find_elements_by_partial_link_text('')
            print(video)
            speak('which number you want to listen')
            print(video.__len__())
            query2 = takeCommand().lower()
            video[19].click()
            if(query2=='1'):
                video[0].click()
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sarthakmittal1461@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")    
        elif 'commentary' in query.lower():
             try:
                cricCommentry()
             except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 

=======
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from selenium import webdriver
import smtplib
import time 
from pycricbuzz import Cricbuzz
def cricCommentry():
        c = Cricbuzz()
        matches = c.matches()
        # for match in matches:
        match=matches[0]
        # print( match)
        # if(match['mchstate'] != 'nextlive'):
        #         print (c.livescore(match['id']))
        #         print( c.commentary(match['id']))
        #         print( c.scorecard(match['id']))
        print('sun',c.commentary(match['id'])['commentary'][0]['comm'])
        a,b=c.commentary(match['id'])['commentary'][0]['comm'],''
        while(1):
                if(a!=b):
                        # speak(a)
                        d=c.scorecard(match['id'])['scorecard']
                        speak(a)
                        speak(d[0]['batteam']+'score is '+d[0]['runs']+'for'+d[0]['wickets']+'wickets')
                        b=a
                else:
                        a=c.commentary(match['id'])['commentary'][0]['comm']

browser = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe') 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    speak("Hello Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

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
            # webbrowser.open("youtube.com")
            print("hi")
            browser.get('https://www.youtube.com/') 
            speak("what do you want to search on youtube")
            query1 = takeCommand().lower()
            search=browser.find_element_by_id('search')
            search.send_keys(query1) 
            sbutton=browser.find_element_by_id('search-icon-legacy')
            # browser.find_elements_by_xpath()
            sbutton.click()
            video=browser.find_elements_by_partial_link_text('')
            print(video)
            speak('which number you want to listen')
            print(video.__len__())
            query2 = takeCommand().lower()
            video[19].click()
            if(query2=='1'):
                video[0].click()
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sarthakmittal1461@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")    
        elif 'commentary' in query.lower():
             try:
                cricCommentry()
             except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 

>>>>>>> 31bee857ab196b147925431a10b03464e7051e3b
                