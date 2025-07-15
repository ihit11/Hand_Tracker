import tkinter
from tkinter import Label, PhotoImage
import threading

root = tkinter.Tk()
root.title("Espio Hand Track")
root.geometry("1920x1080")

Mlabel = Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="black")
Mlabel.place(x=1800,y=50, anchor="center")
Glabel = Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="black")
Glabel.place(x=1800,y=80, anchor="center")
G1label = Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="black")
G1label.place(x=1800,y=110, anchor="center")
G2label = Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="black")
G2label.place(x=1800,y=140, anchor="center")
G3label = Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="black")
G3label.place(x=1800,y=170, anchor="center")
G4label = Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="black")
G4label.place(x=1800,y=200, anchor="center")

#Example objects to move
EgObjImg = PhotoImage(file="/home/ihit2011/EspioProjects/Godot.png")
EgObj = Label(root, image=EgObjImg)
EgObj.place(x=960,y=540, anchor="center")


#Mlabel.pack()
root.configure(bg="black")
root.attributes("-fullscreen", True)

def gloop():
    root.mainloop()

gloopthr = threading.Thread(target=gloop, daemon=True)
