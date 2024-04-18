from tkinter import ttk
import tkinter as tk
import mysql.connector as pymysql
my_conn = pymysql.connect(host='localhost', user='root', password='123456', database='users')  
my_w = tk.Tk()
my_w.geometry("283x280") 
my_w.title("Leaderboard")  

trv = ttk.Treeview(my_w, selectmode ='browse')
trv.grid(row=1,column=1,padx=20,pady=20)


trv["columns"] = ("1", "2", "3")


trv['show'] = 'headings'


trv.column("1", width = 80, anchor ='c')
trv.column("2", width = 80, anchor ='c')
trv.column("3", width = 80, anchor ='c')

trv.heading("1", text ="UserID")
trv.heading("2", text ="UserName")
trv.heading("3", text ="Score")  
cur=my_conn.cursor()
cur.execute('select userid,username,score from info order by score desc')
c = cur.fetchmany(10)
for dt in c:
    trv.insert("",'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2]))
my_conn.close()
my_w.mainloop()