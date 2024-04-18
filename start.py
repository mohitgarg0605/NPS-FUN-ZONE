from tkinter import *
import os
window = Tk()
window.geometry("1920x1080")
from PIL import ImageTk, Image

window.title('Welcome to NPS Fun Zone')

img=Image.open("resources/bg.jpg")
bgimg=img.resize((1920,1080))
bg=ImageTk.PhotoImage(bgimg)
def openlogin():
    os.system('python login.py')

def openregister():
    os.system('python register.py')

def openlb():
    os.system('python leaderboard.py')

lable=Label(image=bg)
lable.pack()

button1 = Button(window,
                text="     Login     ",
                command=openlogin,
                font=("Comic Sans",18),
                fg="black",
                bg="white",
                activeforeground="black",
                activebackground="white",relief=RAISED,bd=10,
                padx=7,
                pady=7,
                state=ACTIVE).place(x=770 , y=825)

button2 = Button(window,
                text="  Register  ",
                command=openregister,
                font=("Comic Sans",18),
                fg="black",
                bg="white",
                activeforeground="black",
                activebackground="white",relief=RAISED,bd=10,
                padx=7,
                pady=7,
                state=ACTIVE).place(x=980 , y=825)

button3 = Button(window,
                text="Leaderboard",
                command=openlb,
                font=("Comic Sans",18),
                bg="white",
                fg="black",
                activeforeground="black",
                activebackground="white",relief=RAISED,bd=10,
                padx=7,
                pady=7,
                state=ACTIVE).place(x=870, y=920)
window.mainloop()