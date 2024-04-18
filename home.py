from tkinter import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import mysql.connector as pymysql
from PIL import ImageTk, Image
from tkinter.messagebox import *

mixer.init()
mixer.music.load('resources/home.mp3')
mixer.music.set_volume(0.01)
mixer.music.play(-1)

window = Tk()
window.title('Home')
window.geometry("1920x1080")

img=Image.open("resources/bg2.jpg")
bg=ImageTk.PhotoImage(img)

lable=Label(image=bg)
lable.pack()

label = Label(window,
              text="NPS FUN ZONE",
              font=('Arial',55,'bold'),
              fg='Purple',
              bg='white',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20).place(x=680 , y=30)
window.config(background='white')


label = Label(window,
              text="CLICK ON THE NAME OF THE GAME YOU WANT TO PLAY",
              font=('Candara',17,'bold'),
              fg='purple',
              bg='white').place(x=700, y=280)

label = Label(window,
              text="DON'T FORGET YOU HAVE TO GO TO STUDY TOO",
              font=('Candara',17,'bold'),
              fg='purple',
              bg='white').place(x=730, y=780)

def openmario():
    g=open("tempud.txt","r")
    username=g.readline()
    score=g.readline()
    userid=g.readline()
    g.close()
    intscore=int(score)
    intscore+=5
    if intscore>50:
        showerror('error', 'Enough for this session. Comeback later')
        closewindow()
    else:
        h=open('tempud.txt','w')
        h.writelines(username)
        h.writelines(str(intscore))
        h.writelines('\n')
        h.writelines(str(userid))
        h.close()
        os.system('python mario.py')

def openkbc():
    g=open("tempud.txt","r")
    username=g.readline()
    score=g.readline()
    userid=g.readline()
    g.close()
    intscore=int(score)
    intscore+=5
    if intscore>50:
        showerror('error', 'Enough for this session. Comeback later')
        closewindow()
    else:
        h=open('tempud.txt','w')
        h.writelines(username)
        h.writelines(str(intscore))
        h.writelines('\n')
        h.writelines(str(userid))
        h.close()
        os.system('python kbc/kbc.py')

def opensnake():
    g=open("tempud.txt","r")
    username=g.readline()
    score=g.readline()
    userid=g.readline()
    g.close()
    intscore=int(score)
    intscore+=5
    if intscore>50:
        showerror('error', 'Enough for this session. Comeback later')
        closewindow()
    else:
        h=open('tempud.txt','w')
        h.writelines(username)
        h.writelines(str(intscore))
        h.writelines('\n')
        h.writelines(str(userid))
        h.close()
        os.system('python snake.py')

def opencar():
    g=open("tempud.txt","r")
    username=g.readline()
    score=g.readline()
    userid=g.readline()
    g.close()
    intscore=int(score)
    intscore+=5
    if intscore>50:
        showerror('error', 'Enough for this session. Comeback later')
        closewindow()
    else:
        h=open('tempud.txt','w')
        h.writelines(username)
        h.writelines(str(intscore))
        h.writelines('\n')
        h.writelines(str(userid))
        h.close()
        os.system('python racing.py')

def openegg():
    g=open("tempud.txt","r")
    username=g.readline()
    score=g.readline()
    userid=g.readline()
    g.close()
    intscore=int(score)
    intscore+=5
    if intscore>50:
        showerror('error', 'Enough for this session. Comeback later')
        closewindow()
    else:
        h=open('tempud.txt','w')
        h.writelines(username)
        h.writelines(str(intscore))
        h.writelines('\n')
        h.writelines(str(userid))
        h.close()
        os.system('python catchegg.py')

def openindquiz():
    g=open("tempud.txt","r")
    username=g.readline()
    score=g.readline()
    userid=g.readline()
    g.close()
    intscore=int(score)
    intscore+=5
    if intscore>50:
        showerror('error', 'Enough for this session. Comeback later')
        closewindow()
    else:
        h=open('tempud.txt','w')
        h.writelines(username)
        h.writelines(str(intscore))
        h.writelines('\n')
        h.writelines(str(userid))
        h.close()
        os.system('python indquiz.py')

def closewindow():
    g=open("tempud.txt","r")
    username=g.readline()
    score=g.readline()
    userid=g.readline()
    g.close()
    con = pymysql.connect(host='localhost', user='root', password='123456', database='users')
    cur = con.cursor()
    cur.execute('update info set score=score+%s where userid=%s',(score,userid))
    con.commit()
    con.close()
    window.destroy()

def disable_event():
   pass
       
button1 = Button(window,
                text="   Mario   ",
                command=openmario,
                font=("Comic Sans",25),
                bg="white",
                fg="purple",
                activeforeground="purple",
                activebackground="white",
                relief=RAISED,
                bd=10,
                state=ACTIVE,padx=20,
                pady=20).place(x=440, y=350)


button2 = Button(window,
                text="Millionaire",
                command=openkbc,
                font=("Comic Sans",25),
                bg="white",
                fg="purple",
                activeforeground="purple",
                activebackground="white",
                relief=RAISED,
                bd=10,
                state=ACTIVE,padx=20,
                pady=20).place(x=1265, y=350)


button3 = Button(window,
                text="   Snake    ",
                command=opensnake,
                font=("Comic Sans",25),
                bg="white",
                fg="purple",
                activeforeground="purple",
                activebackground="white",
                relief=RAISED,
                bd=10,
                state=ACTIVE,padx=20,
                pady=20).place(x=428, y=600)

button3 = Button(window,
                text="End Session",
                command=closewindow,
                font=("Comic Sans",25),
                bg="white",
                fg="purple",
                activeforeground="purple",
                activebackground="white",
                relief=RAISED,
                bd=10,
                state=ACTIVE,padx=20,
                pady=20).place(x=835, y=850)

button4 = Button(window,
                text="Road Rash",
                command=opencar,
                font=("Comic Sans",25),
                bg="white",
                fg="purple",
                activeforeground="purple",
                activebackground="white",
                relief=RAISED,
                bd=10,
                state=ACTIVE,padx=20,
                pady=20).place(x=853, y=350)

button5 = Button(window,
                text="India Quiz",
                command=openindquiz,
                font=("Comic Sans",25),
                bg="white",
                fg="purple",
                activeforeground="purple",
                activebackground="white",
                relief=RAISED,
                bd=10,
                state=ACTIVE,padx=20,
                pady=20).place(x=1260, y=600)

button5 = Button(window,
                text="Egg Catcher",
                command=openegg,
                font=("Comic Sans",25),
                bg="white",
                fg="purple",
                activeforeground="purple",
                activebackground="white",
                relief=RAISED,
                bd=10,
                state=ACTIVE,padx=20,
                pady=20).place(x=840, y=600)
window.protocol("WM_DELETE_WINDOW", disable_event)
window.mainloop()