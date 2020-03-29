import tkinter
from Agent import crawlWeather
from tkinter import *
from tkinter import messagebox

top = tkinter.Tk()
top.geometry("350x450")

def searchCallBack():
    listBox.delete(0, listBox.size())
    weather = crawlWeather(city.get())
    for dailyForecast in weather:
        listBox.insert(END, dailyForecast["day"]+": "+dailyForecast["max"]+" / "+dailyForecast["min"])
        

btn = Button (top, text = "Go", command = searchCallBack)
btn.place(x=250, y=50)

city = Entry(top)
city.place(x=50, y=50)

listBox = Listbox(top)
listBox.place(x=50, y = 150)

top.mainloop()