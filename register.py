from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter.messagebox import *

def register():
    if e1.get() == '' or e2.get() == '' or e3.get() == '' or e1.get() == '':
        showerror('Error', "All Fields Are Required", parent=root)
    
    elif e4.get().isdigit()==False:
        showerror('Error', "Only Numerical input allowed for UserID", parent=root)

    elif e2.get() != e3.get():
        showerror('Error', "Password Mismatch", parent=root)

    else:
        con = pymysql.connect(host='localhost', user='root', password='123456', database='users')
        cur = con.cursor()
        cur.execute('select * from info where userid=%s', e4.get())
        row = cur.fetchone()
        if row != None:
            showerror('Error', "UserID Already Exists", parent=root)
        else:

            cur.execute('insert into info (userid,username,password,score) values(%s,%s,%s,0)',(e4.get(),e1.get(),e2.get()))
            con.commit()
            con.close()
            showinfo('Success', "Registration Successful", parent=root)
            root.destroy()
            import login


        

root = Tk()
root.title("Register")
root.geometry("300x250")
global e1
global e2

Label(root, text="UserID (Numbers only)").place(x=10, y=10)

Label(root, text="UserName").place(x=10, y=40)
Label(root, text="Password").place(x=10, y=70)
Label(root, text="Confirm Password").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=40)

e2 = Entry(root)
e2.place(x=140, y=70)
e2.config(show="*")

e3 = Entry(root)
e3.place(x=140, y=100)
e3.config(show="*")

e4 = Entry(root)
e4.place(x=140, y=10)


Button(root, text="Register", command=register ,height = 3, width = 13).place(x=100, y=150)

root.mainloop()