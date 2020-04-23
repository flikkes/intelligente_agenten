from Agent import Agent
from Labyrinth import Labyrinth
import time
import tkinter
from tkinter import *

labyrinth = Labyrinth()

top = tkinter.Tk()
top.geometry("500x500")

canvas = Canvas(top, height=len(labyrinth.fields)*15, width=len(labyrinth.fields[0])*15)
canvas.pack()

def callback():
    time.sleep(1)
    for i in range(len(labyrinth.fields)):
        for j in range(len(labyrinth.fields[i])):
            val = labyrinth.fields[i][j]
            fill="#ffffff"
            if val == 1:
                fill = "#34ebc9"
            if val == 2:
                fill = "#edea39"
            if val == 3:
                fill = "#d92f23"
            if val == 4:
                fill = "#5334eb"
            canvas.create_rectangle(j*15, i*15, j*15+8, i*15+8, fill=fill)
    top.update()

callback()

initialAgent = Agent(10, 0, labyrinth, callback)

top.mainloop()