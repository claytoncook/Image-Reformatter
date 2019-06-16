from tkinter import *
from tkinter import filedialog
import os

os.system("clear")

app = Tk()
direct = StringVar()
files = []
formats = ["jpeg","tiff","png","gif","jp2","pict","bmp","qtif","psd","sgi","tga"]
v = StringVar()
v.set("jpeg")

def selectDirectory():
    app.filename = filedialog.askdirectory()
    print(app.filename)
    files.append(os.listdir(str(app.filename)))
    direct.set("Directory: " + str(app.filename))
    os.chdir(str(app.filename))
    os.system("ls")

def reformat():
    print(v.get())
    for f in files[0]:
        data = f.split(".")
        print(f)
        os.system("sips -s format " + v.get() + " " + f + " --out " + data[0] + "." + v.get())
        os.remove(f)

def build():
    chooseDirectoryFrame = Frame(app)
    chooseDirectoryFrame.pack(side=TOP)
    Button(chooseDirectoryFrame, text="Select Directory", command=selectDirectory).pack(side=LEFT)
    direct.set("Directory: ")
    Label(chooseDirectoryFrame, textvariable=direct).pack(side=LEFT)

    imageFormatOptionsFrame = Frame(app)
    imageFormatOptionsFrame.pack()
    for text in formats:
        Radiobutton(imageFormatOptionsFrame, text=text, variable=v, value=text).pack(side=LEFT)

    submitFrame = Frame(app)
    submitFrame.pack(side=BOTTOM)
    Button(submitFrame, text="Reformat", command=reformat).pack(side=LEFT)

    app.title("Image Reformatter")
    app.mainloop()

build()