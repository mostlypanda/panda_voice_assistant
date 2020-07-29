import pyttsx3                          #pip install pyttsx3
import speech_recognition as sr         #pip install speechRecognition
import datetime                         #pip install datetime
import wikipedia                        #pip install wikipedia
import webbrowser                       #pip install webbrowser
import os                               #pip install os
from selenium import webdriver          #pip install selenium
import smtplib
import time 
from pycricbuzz import Cricbuzz         #pip install pycricbuzz
def cricCommentry():
        c = Cricbuzz()
        matches = c.matches()
        # for match in matches:
        match=matches[0]        #take most recent match
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

                        
browser = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe') #path to chrome driver

#voice methods defines

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

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        if 'commentary' in query.lower():
             try:
                cricCommentry()
             except Exception as e:
                print(e)
                speak("Sorry my friend I am not able to do live commentory")

