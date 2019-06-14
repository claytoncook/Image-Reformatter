from tkinter import *
from tkinter import filedialog
import os

app = Tk()
direct = StringVar()

def selectDirectory():
    app.filename = filedialog.askdirectory()
    print(os.listdir(app.filename))
    direct.set("Directory: " + str(app.filename))

def displayFiles():
    print(os.path.exists("Output"))

def init():
    if os.path.exists("Output") != True :
        print("Creating Ouput Directory...")
        os.mkdir("Output")
    else:
        print("Ouput Directory Already Exists!")

def build():
    init()
    Button(app, text="Select Directory", command=selectDirectory).pack(side=LEFT)
    direct.set("Directory: ")
    Label(app, textvariable=direct).pack(side=LEFT)
    app.mainloop()

build()