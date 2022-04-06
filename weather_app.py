import tkinter as tk
import requests
from PIL import Image, ImageTk

def get_weather(city):
    weather_key = "c6ede4f16a57ef8d278c2d059d0cd443"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"appid": weather_key, "q": city, "units":"metric"}
    response = requests.get(url, params=params)
    weather = response.json()

    label["text"] = format_response(weather)

    icon = weather['weather'][0]['icon']
    open_image(icon)

def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        pressure = weather["main"]["pressure"]

        final_str = "City: %s \nConditions: %s \nTemperature: %s°C \nPressure: %s hPa" % (name, desc, temp, pressure)
    except KeyError:
        final_str = "There was a problem\nretrieving that information" 
    return final_str

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.5)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor = "nw", image=img)
    weather_icon.image = img

root = tk.Tk()
root.title("Current Weather")
root.iconphoto(False, tk.PhotoImage(file="02d.png"))

canvas = tk.Canvas(root, height = 500, width = 600)
canvas.pack()

background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = "#3333ff", bd = 5)
frame.place(relx = 0.5, rely = 0.25, relwidth=0.75, relheight = 0.1, anchor="n")

entry = tk.Entry(frame, font = ("Courier", 25))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Check weather", font = ("Courier", 10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight = 1, relwidth = 0.25)

lower_frame = tk.Frame(root, bg="#3333ff", bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth = 0.75, relheight = 0.5, anchor = "n")


label = tk.Label(lower_frame, font = ("Courier", 15), anchor = "n", bd = 5)
label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg="#3333ff", bd=10)
upper_frame.place(relx=0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

title = tk.Label(upper_frame, text="Current Weather", font = ("Courier", 25, "bold"))
title.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=0.35, rely=0.5)

root.mainloop()
