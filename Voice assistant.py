import subprocess
#import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime

import webbrowser
import os
#import winshell
#import pyjokes
#import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from ecapture import ecapture as ec
#from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import cv2
from random import randrange

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello Rudra")
    speak("How can i help you, boss")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"My Boss said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, there was a problem with the speech service.")
        speak("Sorry, there was a problem with the speech service.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        speak(f"An unexpected error occurred: {e}")
    
    return "None"




def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', port_number)
    server.ehlo()
    server.starttls()

    server.login('your_mail_id', 'your_password')
    server.sendmail('your_mail_id', to, content)
    server.close()


if __name__ == "__main__":
    WishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow, boss.Happy coding")
            webbrowser.open("stackoverflow.com") 

        elif 'spotify' in query:
            webbrowser.open("spotify.com")

        elif 'youtube music' in query:
            webbrowser.open("youtube music.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{ strTime}")
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Boss")
 
        elif 'fine' in query or "good" in query:
            speak("You are always dashing, Boss")
            
        elif "what's your name" in query or "What is your name" in query:
            speak("My Boss call me")
            speak("AK")
            print("My BOss call me, AK")
            
        elif 'who is your boss' in query:
            speak("Rudra is my Boss, He created me for the very secret purpose")
            
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Rudra.")
            
        elif "who are you" in query:
            speak("I am your Personalized virtual assistant,boss")
            
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])                             

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister Rudra")
        
        elif "i love you" in query:
            speak("It's hard to understand, why you love me, i am just a vitual assistant ")            
        
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
                
        elif 'news' in query:
            speak("what type of news you want")
            
            def get_input():
                return input("Enter a news category: ")

            def print_news(data):
                speak("here are some top news from the times of india")
                print("*****TIMWS OF INDIA*****")
                for i, article in enumerate(data['articles'], start=1):
                    print(f"{i}. {article['title']}")
                    print(article['description'])

            def main():
                category = takeCommand()
                url = f"API_key"
                response = requests.get(url)
                data = json.loads(response.content)
                print_news(data)
                speak("Now you can read it")

            main()

        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("you want to locate")
            speak(location)
            speak("now you can see it in the google map")
            webbrowser.open(
                "https://www.google.com/maps/place/" + location.replace(" ", "+"))

        elif 'i want to write a note' in query:
            speak("What will be title of the note")
            title_name = takeCommand()
            speak("what should i write in it,BOSS")
            note = takeCommand()
            file = open('ak.text', 'w')
            speak("BOSS, do you want to incude date and time as well")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)

            else:
                file.write(note)

        elif 'can you tell me my note' in query:
            speak("here is your note sir")
            with open("ak.text", "r") as file:
                content = file.read()
                print(content)
                speak(content)

        elif 'weather' in query:
            API_KEY = "95c969512623bd4c60510b009122babe"
            speak("for which city you want to know about weather")
            location = takeCommand()
            url = f"API_key"
            response = requests.get(url)
            data = json.loads(response.text)

            current_temperature = data["main"]["temp"]
            current_pressure = data["main"]["pressure"]
            current_humidiy = data["main"]["pressure"]
            weather_description = data["weather"][0]["description"]

            print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) =" +
                  str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))
            speak(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) =" +
                  str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

        elif 'check for the faces' in query:
            trained_face_data = cv2.CascadeClassifier("xml version=1.0.txt")
            webcam = cv2.VideoCapture(0)
            while True:
                successful_frame_read, frame = webcam.read()
                grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
                for (x, y, w, h) in face_coordinates:
                    cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (randrange(256), randrange(256), randrange(256)), 1)
                cv2.imshow('AKR face detecter', frame)
                key = cv2.waitKey(1)

                if key == 81 or key == 113:
                    break
            webcam.release()

        elif 'send a mail' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "mail_id"
                sendMail(to, content)
                speak("mail has been sent")

            except Exception as e:
                print(e)
                speak("There is some issue, please check the mail id again")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'camera' in query or 'take a photo' in query:
            ec.capture(0, "AKR Camera", "img.jpg")


            
        elif "check for the vehicle" in query:
            
            video = cv2.VideoCapture("Video or live capture")
            car_tracker_file = "xml version=2.0.txt"
            pedestration_tracker_file = "xml version=3.0.txt"
            car_tracker = cv2.CascadeClassifier(car_tracker_file)
            pedestration_tracker = cv2.CascadeClassifier(pedestration_tracker_file)



            while True:
                    (read_successful,frame) = video.read()
                    if read_successful:
                                grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                    else:
                                break          
                    cars = car_tracker.detectMultiScale(grayscaled_frame)
                    pedestration = pedestration_tracker.detectMultiScale(grayscaled_frame)


                    for (x,y,w,h) in cars:
                                cv2.rectangle(frame,(x+1,y+2),(x+w, y+h),(255,0,0), 2)
                    cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0), 2)
                    for (x,y,w,h) in pedestration:
                                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,255), 2) 
          
                    cv2.imshow('Self Driving Car',frame)
          
                    key = cv2.waitKey(1)

                    if key==81 or key==113:
                                break

            video.release()                       
