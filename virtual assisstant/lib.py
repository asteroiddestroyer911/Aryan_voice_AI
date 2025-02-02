import os
import speech_recognition as sr
import greeting as gr
import smtplib
import pyttsx3 as tts
import pywhatkit as kit
from datetime import *
from AppOpener import *
import wikipedia as wp
import calendar


listener = sr.Recognizer()

machine = tts.init()
voices = machine.getProperty('voices')


def talk(text):
    machine.setProperty('voice', voices[1].id)
    machine.say(text)
    machine.runAndWait()

def wake_word():
    try:
        with sr.Microphone() as origin:
            print("To start, say 'Hey Aryan'")
            speech = listener.listen(origin)
            word = listener.recognize_google(speech).lower()
            if "aryan" in word:
                return True
    except sr.UnknownValueError:
        print("Wake word not detected.")
    except sr.RequestError as e:
        print(f"Error with speech recognition: {e}")
    return False
 
def input_instruction():
    global instruction
    try:
        with sr.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech).lower()
            if "aryan" in instruction:
                instruction = instruction.replace('aryan', '').strip()
                print(f"Recognized command: {instruction}")
    except sr.UnknownValueError:
        instruction = ""
        talk("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        instruction = ""
        talk("It seems there's an issue with the network. Please try again.")
    return instruction if instruction else None  
