import os
import wolframalpha
from tkinter import *
import wikipedia
import tkinter.messagebox
import speech_recognition as sr
import time

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak something...")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio) #convert into text
            if text =="stop":
                break
            else:
                window = Tk()
                window.geometry("700x600")
                try:
                    app_id = "GAVV7X-VTVLJJTV3H"   #client id
                    client = wolframaplha.Client(app_id)
                    answer = next(res.results).text
                    
                    label1 = label(window, justify = LEFT, compund = CENTER, padx =12, text = answer, font= "times 15 bold")
                     label1.pack()
                    window.after(5000,lambda: window.destroy())
                    mainloop()
                except:
                    answer = wikipedia.summary()
                    label1 = label(window, justify = LEFT, compund = CENTER, padx =12, text = answer, font= "times 15 bold")
                    label1.pack()
                    window.after(5000000,lambda: window.destroy())
                    mainloop()
                    
                    
        #if module not understand our speech
        except:
            answer = "Sorry! I Can't here You"
            print(answer)
                