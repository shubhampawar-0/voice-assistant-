import speech_recognition as sr
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser 
import os
import smtplib

listener = sr.Recognizer()

try:
    with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        url ="https://www.google.com.tr/search?q={}".format(instruct)
        webbrowser.open_new_tab(url)
        
        print(instruct)
except:
    pass
