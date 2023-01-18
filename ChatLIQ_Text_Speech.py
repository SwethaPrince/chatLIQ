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
from tkinter import PhotoImage , Label
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
        bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJsWUVOWHhJRWpTTm9LUjF5bEdxNHpSQUl1a1IxcThMdGZYNnBlZXctRnUwIn0.eyJleHAiOjE2NzQwMzY0MTgsImlhdCI6MTY3NDAzMzQxOCwianRpIjoiODQzODFkOTQtMGY5ZS00MzIxLWJlYzgtMmQxMTM3MmQ3ZWNkIiwiaXNzIjoiaHR0cDovLzEwLjI0MC4xODYuMjM2OjgwODAvYXV0aC9yZWFsbXMvTG9hbklRX1dFQiIsInN1YiI6ImYxZTUzZmY0LWQ3YmQtNGVhNS05NWMyLTYxYjRhNWVhN2JlMCIsInR5cCI6IkJlYXJlciIsImF6cCI6IkxvYW5JUV9XRUIiLCJzZXNzaW9uX3N0YXRlIjoiYjYwYjgxMGQtYjY4Ni00ZDM1LThiNjItZjdjMWRiMDg4NmM4IiwiYWNyIjoiMSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJiNjBiODEwZC1iNjg2LTRkMzUtOGI2Mi1mN2MxZGIwODg2YzgiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6InRydXNlcjI2In0.SRIyC6q_HQU4KAsWVuD_4VY5zVM2nPzF-eGx4ZtMBS8UVPBJFvPfyGMszjTntkwza0ikzYWZIG88RIcr6gzZZQPIZCIVKDN9mq6k7HfOC03KSKJGUJqvT674pBPiaHGiTFQb7UhaucfF7afUCvJ0B80UcpymiBksSq7c_fPtTkRddSh8PyqDF2JHfOgIKs17br7uFAhYpCntIjMoZUpIygxVwBLGlRN4yxh6Z70iX0WG6_itjuCpE1yaODhEqUGoZxU3F3K9IoXrTLq3Sy3mOuFBG9edPQF_847UNp6vHWbFlyhQZokib1pN9-DIBokTb9wUyE8pxvoxpsxqg5vBxA.eyJleHAiOjE2NzQwMjk0NDQsImlhdCI6MTY3NDAyNjQ0NCwianRpIjoiMDcwNDg1ZDEtY2IwMy00MWEwLTg3YWEtMTE1YWFkM2I1YmRjIiwiaXNzIjoiaHR0cDovLzEwLjI0MC4xODYuMjM2OjgwODAvYXV0aC9yZWFsbXMvTG9hbklRX1dFQiIsInN1YiI6ImYxZTUzZmY0LWQ3YmQtNGVhNS05NWMyLTYxYjRhNWVhN2JlMCIsInR5cCI6IkJlYXJlciIsImF6cCI6IkxvYW5JUV9XRUIiLCJzZXNzaW9uX3N0YXRlIjoiNDYxMWIwYWQtMjk5My00ZTYwLThjMGUtNjBlYjZhMjRiZDMzIiwiYWNyIjoiMSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI0NjExYjBhZC0yOTkzLTRlNjAtOGMwZS02MGViNmEyNGJkMzMiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6InRydXNlcjI2In0.tFN8dgcKSxqQKKtIk5ATtMeOfvPN-ARVjTYShvFRaRMHocixBy_FroW5Jbv0HHHjzbRVErrK5limjELt0aePWyRMdO6mCymByoHzDEWq1IHn0hB20uYwV0W4x9dBxZU0qOlBLp3Bh5DOAf0v0JgIEpN_wjeB7M1gPL-ZjSrBnWviV0brNwNzW3v0Lw7qGXUVfyoO6oaXRP-mS7gKMyddLonKHKs3ZWqhJLDRvbJIpXg3n8mwTcehdz8d9V4mF3Q-LHu1pgGnGHVx1brG08Ze1rY8NlTPkLyusPSyzWMNGJrfzxMgaRsyubMx7LjFsCAhVLtUCsUVu5j88oK3P3jncg"
        
        # Set the headers
        headers = {
            'Content-Type': 'application/x-protobuf',
            'Authorization': 'Bearer ' + bearer_token
        }
        
        # Send the POST request
        response = requests.post("http://blrcswliqdt0010:8081/saveaction/submit/SME/SME", data=protobuf_data, headers=headers)
        # Print the response
        print(response.status_code)


def searchBorrowerCall():
        # Read the protobuf file
        with open("common.bin", "rb") as f:
            protobuf_data = f.read()
        
        # Define the bearer token
        bearer_token ="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJsWUVOWHhJRWpTTm9LUjF5bEdxNHpSQUl1a1IxcThMdGZYNnBlZXctRnUwIn0.eyJleHAiOjE2NzQwNjM0MjEsImlhdCI6MTY3NDA1OTgyMSwianRpIjoiNTU0ZGYxMzItOTAwMy00YWEyLThjZjAtZmRmMWM0MTNhM2UzIiwiaXNzIjoiaHR0cDovLzEwLjI0MC4xODAuMTkwOjgwOTAvYXV0aC9yZWFsbXMvTE9BTklRX1dFQiIsInN1YiI6ImQwZTY0Yjc1LTgzZDktNDMyOS1hYzM0LTQyNDkyY2RlODM3ZiIsInR5cCI6IkJlYXJlciIsImF6cCI6IkxPQU5JUV9XRUIiLCJzZXNzaW9uX3N0YXRlIjoiYTVjNDFlMzMtNGRmMy00ZmY3LTgxYzctMmQzOTU2YzI0ZmI5IiwiYWNyIjoiMSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJhNWM0MWUzMy00ZGYzLTRmZjctODFjNy0yZDM5NTZjMjRmYjkiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJ0cnVzZXIgMjYiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0cnVzZXIyNiIsImdpdmVuX25hbWUiOiJ0cnVzZXIiLCJmYW1pbHlfbmFtZSI6IjI2In0.RY5fepi0WXnADmduQmXVfpT8DnXBJI0Z3oU_lU3_WpcIB_WVi-xO-aa-FFoVFmC3mbVGVpFJPYQ0jBtmWFULZn5BKxayz-ndyvYDzhIq-Dpn1_lFjJREvLxk9DNNSoZ2iwUfSh2afysWjNFL9Sxh5LCdHYKSEBi8CIt8Wq4xfTARynZ8ApS0M7-zVvadbmAwyuMZeGXPyuzhDpr5gKYXEJ6Kud1kV0m1esJoACEvY9kPdnMMiQSHZrykCF9gn4yhCMq7p8Nhjm_G6GYc-2PRpJVEgUTpN_IBCTpQ-UYHfHe8QbZau850pieiDnhc55QpEdtOmy3JhZlf_l2YoXdQrA"
        # Set the headers
        headers = {
            'Content-Type': 'application/x-protobuf',
            'Authorization': 'Bearer ' + bearer_token
        }
        
        # Send the POST request
        response = requests.post("http://blrcswliqdt0010:8081/search/query/tenantID/SME/searchborrower", data=protobuf_data, headers=headers)
        # Print the response
        print(response.status_code)
       # Check if the request was successful
        if response.status_code == 200:
            # Get the content of the response
            content = response.content
        
            # Save the content to a file
            with open("response.bin", "wb") as file:
                file.write(content)
                print("response saved in response.bin")
             # Send the POST request
                 
            with open("response.bin", "rb") as f:
                protobuf_data = f.read()
             
                headers = {
                    'Content-Type': 'application/x-protobuf'
                    }
                response_json = requests.post("http://blrcswliqdt0010:9091/dev/protobuf-utility/protobuftojson", data=protobuf_data, headers=headers)  
                data_json = response_json.json()
                json_str = json.dumps(data_json)
                #print(json.dumps(data_json, indent=4))
                json_data = json.loads(json_str)
                #print(json_data["response"]["result"]["liqBusinessObjects"]["liqBusinessObject"][0]["group"][0]["item"][0:15])
                #print("transactionType:", json_data["transactionType"]["0"])

                desired_json = json_data["response"]["result"]["liqBusinessObjects"]["liqBusinessObject"][0]["group"][0]["item"][0:15]
                json_str1 = json.dumps(desired_json)
                print(json_str1)
                return (json_str1)
        else:
            # Handle error
            print("Request failed with status code:", response.status_code)





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
        r"search",
      [ "getting you search details"] 
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
root.geometry("1400x460")
bg_image = PhotoImage(file="Capture.png")
# Create a Label widget to hold the background image
bg_label = Label(root, image=bg_image)
# Place the Label widget on the right side of the main window
bg_label.place(relx=1.0, rely=0, anchor='ne')
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


user_input = tk.Entry(user_input_frame, width=400,font=("Roboto", 10))
user_input.pack()


# Create a button to send the user input
send_button = tk.Button(user_input_frame, text="Submit", command=lambda: send_message())
send_button.pack()
   
# Create a button to activate speech input
#listen_button = tk.Button(user_input_frame, text="Say Something", command=lambda: listen())
#listen_button.pack()

gif = PhotoImage(file="rsz_voice_search.png")
listen_button = tk.Button(user_input_frame, image=gif, command=lambda:  listen())
listen_button.image = gif
listen_button.pack()



def default_message():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        text = "Good Morning.I am your assistant chatLIQ. How can I help you ?"
    elif 12 <= hour < 18:
        text = "Good Afternoon.I am your assistant chatLIQ. How can I help you ?"
    else:
        text = "Good Evening.I am your assistant chatLIQ. How can I help you ?"
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
