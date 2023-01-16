import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
import time
import datetime
from PIL import Image, ImageTk
#from PIL import Image
#import tkinter.messagebox
import time
import datetime
import pyttsx3
from win32com.client import Dispatch
#import win32com.client as wincl
#from pygame import mixer
import speech_recognition as sr
from threading import Thread
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import random
from playsound import playsound
import warnings
warnings.filterwarnings("ignore")


# Define the pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot", "I'm a chatbot, you can call me whatever you like"]
    ],
    [
        r"how are you?",
        ["I'm doing good", "I'm fine, thank you"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ],
]





# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Create the main window
root = tk.Tk()
root.title("Chatbot-LoanIQ")
pad=3
root.geometry("600x480")
root.configure(background='white')

global Canvas
global img1


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create a PhotoImage object
img1= ImageTk.PhotoImage(file='Capture.png')
canvas = tk.Canvas(root, width = 500, height = 796)
canvas.place(x=10,y=10)
canvas.create_image(0,0, anchor='nw', image=img1)
   
# Create a frame for the chat history
chat_history_frame = tk.Frame(root)
chat_history_frame.pack()

# Create a text widget to display the chat history
chat_history = tk.Text(chat_history_frame)
chat_history.pack()

# Create a frame for the user input
user_input_frame = tk.Frame(root)
user_input_frame.pack()


user_input = tk.Entry(user_input_frame, width=500,font=("Roboto", 10))
user_input.pack()

# Create a button to send the user input
send_button = tk.Button(user_input_frame, text="Submit", command=lambda: send_message())
send_button.pack()
    
# Create a button to activate speech input
listen_button = tk.Button(user_input_frame, text="Say Something", command=lambda: listen())
listen_button.pack()

def default_message():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        text = "Good Morning.I am your assistant chatLIQ.How can I Serve you?"
    elif 12 <= hour < 18:
        text = "Good Afternoon.I am your assistant chatLIQ.How can I Serve you?"
    else:
        text = "Good Evening.I am your assistant chatLIQ.How can I Serve you?"
    chat_history.insert(tk.END, "chatLIQ: " + text + "\n")


root.after(1000, default_message)


def send_message():
    # Get the user's message
    message = user_input.get()
    # Insert the user's message into the chat history
    chat_history.insert(tk.END, "You: " + message + "\n")
    # Get the chatbot's response
    response = chatbot.respond(message)
    # Insert the chatbot's response into the chat history
    chat_history.insert(tk.END, "chatLIQ: " + response + "\n")
    # Clear the user's input
    user_input.delete(0, tk.END)
    
def listen():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text)
        print("You said: {}".format(text))
        speak(text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand you.")
        return None
    except sr.RequestError as e:
        print("Error occured: {}".format(e))
        return None
    
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

root.mainloop()
