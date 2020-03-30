import tkinter
from Agent import crawlCategories, crawlTeasers
from tkinter import *
from tkinter import messagebox

top = tkinter.Tk()
top.geometry("600x1200")




categories = crawlCategories()
for category in categories:
    catBtn = Button(top, text=category['name'], command=lambda name = category['url']:crawlCallback(name))
    catBtn.pack()

results = Listbox(top, width=400, height=300)
results.pack()

def crawlCallback(url):
    print(url)
    results.delete(0, results.size())
    teasers = crawlTeasers(url)
    print(teasers)
    for teaser in teasers:
        results.insert(END, teaser['title'])
        results.insert(END, teaser['text'])

top.mainloop()