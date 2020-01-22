#coden for direct play of any music on youtube search anything on youtube and also for date time and email too

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from selenium import webdriver
import smtplib
import time 
import urllib.request
import urllib.parse
import re

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

    except Exception:
        # print(e) 
        speak("say that again please")   
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
            # webbrowser.open("http://www.youtube.com/")
            print("hi")
            #browser.get('https://www.youtube.com/') 
            speak("what do you want to search on youtube")
            r = sr.Recognizer()
            with sr.Microphone() as source:                                                                                             
                audio = r.listen(source)

            # get the text from audio
            msg = r.recognize_google(audio)

            # song name from user
            song = urllib.parse.urlencode({"search_query" : msg})
            print(song)
            

            # fetch the ?v=query_string
            result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
            print(result)
           

            # make the url of the first result song
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
            print(search_results)

            # make the final url of song selects the very first result from youtube result
            url = "http://www.youtube.com/watch?v="+search_results[0]

            # play the song using webBrowser module which opens the browser 
            # webbrowser.open(url, new = 1)
            webbrowser.open_new(url)

            
            #query1 = takeCommand().lower()
            #search=browser.find_element_by_id('search')
            #search.send_keys(query1) 
            #sbutton=browser.find_element_by_id('search-icon-legacy')
            # browser.find_elements_by_xpath()
            #sbutton.click()
            #video=browser.find_elements_by_partial_link_text('')
            #print(video)
            #speak('which number you want to listen')
            #print(video.__len__())
            #query2 = takeCommand().lower()
            #video[19].click()
            #if(query2=='1'):
             #   video[0].click()
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

        elif 'email to mohinesh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to ="mohinrshsharma9999@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
            
        elif 'make me happy' in query:
             speak(" sarthak aayu, you are so beautiful")
    

        elif 'play some music' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:                                                                       
                speak("which song you wanna listen:")                                                                                   
                audio = r.listen(source)

            # get the text from audio
            msg = r.recognize_google(audio)

            # song name from user
            song = urllib.parse.urlencode({"search_query" : msg})
            print(song)
            

            # fetch the ?v=query_string
            result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
            print(result)
           

            # make the url of the first result song
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
            print(search_results)

            # make the final url of song selects the very first result from youtube result
            url = "http://www.youtube.com/watch?v="+search_results[0]

            # play the song using webBrowser module which opens the browser 
            # webbrowser.open(url, new = 1)
            webbrowser.open_new(url)


        elif 'close' in query.lower():
            exit()

