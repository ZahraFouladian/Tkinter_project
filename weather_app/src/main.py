import requests
import json
from datetime import datetime
from tkinter import *
import os
import sys
##############################################################
hour = datetime.now().hour
URL = "https://api.open-meteo.com/v1/forecast?latitude=36.6485&longitude=51.4962&current=temperature_2m&hourly=temperature_2m&timezone=auto&forecast_days=1"
response = requests.get(url=URL)
data = response.json()
temp = data["hourly"]["temperature_2m"]
###########################################################
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)        

############################################################
window = Tk()
window.title("weather app")
window.geometry("250x200")
window.resizable(width = False, height = False)
def weather():
    l1.config(text=f"The temperature of this hour is {temp[hour]}", fg='white')
img = PhotoImage(file=resource_path("src/images/img.PNG")) 
w = "#212eeb"  
Label(window,image=img,bg=w).pack() 

btn = Button(window, text="click", command=weather,bg='#9ba1c9')
btn.pack()

l1 = Label(text="",bg=w)
l1.pack()

window.config(bg=w)
window.mainloop()