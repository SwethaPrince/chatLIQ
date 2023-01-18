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
import json
import random
from playsound import playsound
import warnings
warnings.filterwarnings("ignore")



def aboutCall(): 
    response = requests.get("http://blrcswliqdt0010:11082/loaniqcoreservice/restapi/About")
    # Get the JSON data from the response
    data = response.json()
    print(json.dumps(data, indent=4))
    return json.dumps(data, indent=4)


def paymentCall():
        # Read the protobuf file
        with open("input.bin", "rb") as f:
            protobuf_data = f.read()
        
        # Define the bearer token
        bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5akVFdzNwcGp4U1Q4Tlc0M0Zqcll5TG84VlFVeWdkM0MycF9malRKVW9nIn0.eyJleHAiOjE2NzQwMjk0NDQsImlhdCI6MTY3NDAyNjQ0NCwianRpIjoiMDcwNDg1ZDEtY2IwMy00MWEwLTg3YWEtMTE1YWFkM2I1YmRjIiwiaXNzIjoiaHR0cDovLzEwLjI0MC4xODYuMjM2OjgwODAvYXV0aC9yZWFsbXMvTG9hbklRX1dFQiIsInN1YiI6ImYxZTUzZmY0LWQ3YmQtNGVhNS05NWMyLTYxYjRhNWVhN2JlMCIsInR5cCI6IkJlYXJlciIsImF6cCI6IkxvYW5JUV9XRUIiLCJzZXNzaW9uX3N0YXRlIjoiNDYxMWIwYWQtMjk5My00ZTYwLThjMGUtNjBlYjZhMjRiZDMzIiwiYWNyIjoiMSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI0NjExYjBhZC0yOTkzLTRlNjAtOGMwZS02MGViNmEyNGJkMzMiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6InRydXNlcjI2In0.tFN8dgcKSxqQKKtIk5ATtMeOfvPN-ARVjTYShvFRaRMHocixBy_FroW5Jbv0HHHjzbRVErrK5limjELt0aePWyRMdO6mCymByoHzDEWq1IHn0hB20uYwV0W4x9dBxZU0qOlBLp3Bh5DOAf0v0JgIEpN_wjeB7M1gPL-ZjSrBnWviV0brNwNzW3v0Lw7qGXUVfyoO6oaXRP-mS7gKMyddLonKHKs3ZWqhJLDRvbJIpXg3n8mwTcehdz8d9V4mF3Q-LHu1pgGnGHVx1brG08Ze1rY8NlTPkLyusPSyzWMNGJrfzxMgaRsyubMx7LjFsCAhVLtUCsUVu5j88oK3P3jncg"
        
        # Set the headers
        headers = {
            'Content-Type': 'application/x-protobuf',
            'Authorization': 'Bearer ' + bearer_token
        }
        
        # Send the POST request
        response = requests.post("http://blrcswliqmt0096:8081/saveaction/submit/SME/SME", data=protobuf_data, headers=headers)
        # Print the response
        print(response.status_code)










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
        r"about",
      [ paymentCall()  ] 
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
        response = chatbot.respond(text)
        print("You said response: {}".format(response))
        speak(response)
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
