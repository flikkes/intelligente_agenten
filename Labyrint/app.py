from Agent import Agent
from Labyrinth import Labyrinth
import time
import tkinter
import sys
import os
from tkinter import *

sizeX = int(sys.argv[1])
sizeY = int(sys.argv[2])
startX = int(sys.argv[3])
startY = int(sys.argv[4])
finishX = int(sys.argv[5])
finishY = int(sys.argv[6])

labyrinth = Labyrinth(sizeX, sizeY, startX, startY, finishX, finishY)

def close_completely():
    os._exit(0)

top = tkinter.Tk()
top.geometry("500x500")
top.protocol("WM_DELETE_WINDOW", close_completely)

canvas = Canvas(top, height=len(labyrinth.fields) *
                15, width=len(labyrinth.fields[0])*15)
canvas.pack()


def callback():
    time.sleep(1)
    for i in range(len(labyrinth.fields)):
        for j in range(len(labyrinth.fields[i])):
            val = labyrinth.fields[i][j]
            fill = "#ffffff"
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

initialAgent = Agent(labyrinth.startx, labyrinth.starty, labyrinth, callback)

top.mainloop()
