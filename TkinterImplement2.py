import chatbot
import tkinter as tk
from transformers import pipeline
import webbrowser
import random
from functools import partial

#tried to add tkinter (again)


#import TKinterStuff

def getInput(entry):
    string = entry.get()
    responses.append(string)
    print(responses)

"""
create inital pop up
Ask how ur feeling
"""
# feeling = chatbot.isHappyOrSad("")
# feeling = 'happy'
# if feeling == 'happy':
#     webbrowser.open("https://youtu.be/hY7m5jjJ9mM?si=Awzgx8UdJSAJfHBm&t=13")
# elif feeling == 'sad':
#     #create pop up asking more info
"""
    create pop up w/ 4 options
        It's fine, I always feel a little sad -> More pop ups
        I don't really know -> More pop ups
        Something bad just happend -> To code in the future!
        I'm not sure I really wanna talk about it -> To code in the future!
    """
root = tk.Tk()
root.geometry("300x300")
root.title("Therapy Chatbot")
window = tk.Frame(root)
window.grid(padx=30,pady=30)

classifier = pipeline("sentiment-analysis")
responses = []

label = tk.Label(window, text="Thank you for opening up to me, it takes a lot of strength to do that. Please elaborate on how you're feeling.").grid(row=0)
entry= tk.Entry(window, width= 40)
entry.grid(row=1)
getInputCallable = partial(getInput, entry)
tk.Button(window, text= "Enter",width= 20, command= getInputCallable).grid(row=2)

if len(responses) == 1:
    if chatbot.isHappyOrSad(responses[-1]) == 'sad':
        label.configure(text = "Oh no! What's going on?")
    else:
        label.configure(text = "Congrats! Here's some cute cat videos to celebrate")
        webbrowser.open("https://youtu.be/hY7m5jjJ9mM?si=Awzgx8UdJSAJfHBm&t=13")

window.mainloop()