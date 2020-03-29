import tkinter
from Agent import crawlCategories, crawlTeasers
from tkinter import *
from tkinter import messagebox

top = tkinter.Tk()
top.geometry("600x1200")



search = Entry(top)
search.place(x=50, y=50)

listBox = Listbox(top)
listBox.place(x=50, y = 150)

results = Listbox(top)
results.place(x=50, y=800)

categories = crawlCategories()
for category in categories:
    listBox.insert(END, category['name']+': '+category['url'])

def searchCallBack():
    results.delete(0, listBox.size())
    teasers = crawlTeasers(search.get())
    for teaser in teasers:
        results.insert(END, teaser['title']+': '+teaser['text'])
        
btn = Button (top, text = "Go", command = searchCallBack)
btn.place(x=250, y=50)


top.mainloop()