# To Do: not working

from tkinter import *

#import tkinter as tk

def say_hi():
    lbl_Message.configure(text="Hello " + tb_Name.get())

win = Tk()

lbl_Name = Label(win, text="Enter your name:")
lbl_Name.pack()

tb_Name = Entry(win, width=20)
tb_Name.pack()

btn_Hello = Button(win, text="Say Hello", command=say_hi)
btn_Hello.pack()

lbl_Message = Label(win, text="nothing to say")
lbl_Message.pack()

btn_Goodbye = Button(win, text="Goodbye", command=win.destroy)
btn_Goodbye.pack()

### NOT WORKING
ninja = 0
cb_Ninja = Checkbutton(win, text="I'm a Ninja", varible=ninja)
cb_Ninja.pack(side="top")

tb_Name.focus()

win.mainloop()

