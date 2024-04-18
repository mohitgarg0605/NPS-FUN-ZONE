from tkinter import *
from tkinter import messagebox
import mysql.connector as pymysql
import os
from tkinter.messagebox import *

def Ok():
    if e1.get() == '' or e2.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        con = pymysql.connect(host='localhost', user='root', password='123456', database='users')
        cur = con.cursor()
        cur.execute('select username from info where userid=%s and username=%s and password=%s', (e3.get(),e1.get(), e2.get()))
        row = cur.fetchone()
        if row == None:
            showerror('error', 'Invalid UserID, UserName or Password')


        else:
            showinfo('', 'Logged in Sucessfully!')
            con.close()
            f=open("tempud.txt","w")
            f.writelines(e1.get())
            f.writelines("\n")
            f.writelines('1')
            f.writelines("\n")
            f.writelines(e3.get())
            f.close()
            root.destroy()
            os.system('python home.py')
        
        

root = Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2

Label(root, text="UserID").place(x=10, y=10)
Label(root, text="UserName").place(x=10, y=40)
Label(root, text="Password").place(x=10, y=70)

e3 = Entry(root)
e3.place(x=140, y=10)


e1 = Entry(root)
e1.place(x=140, y=40)

e2 = Entry(root)
e2.place(x=140, y=70)
e2.config(show="*")


Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=100, y=115)

root.mainloop()