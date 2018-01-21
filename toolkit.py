from tkinter   import *
#from Tkinter import *
import sqlite3
a=sqlite3.Connection('infodb')
cur=a.cursor()
cur.execute('create table if not exists gym(id number,name varchar(20),sex varchar(8),height number,weight number)')
root=Tk()
Label(root,text="Enter gym id").grid(column=0,row=0)
v0=Entry(root)
v0.grid(row=1,column=0)

Label(root,text="Enter Name").grid(column=0,row=2)
v1=Entry(root)
v1.grid(row=3,column=0)

Label(root,text="Select Sex : ").grid(row=4,column=0)
v5=IntVar()
v6=IntVar()
v7=IntVar()
r1=Radiobutton(root,text='Male',variable=v5,value=1).grid(row=6,column=0)
r2=Radiobutton(root,text='Female',variable=v6,value=2).grid(row=7,column=0)
r2=Radiobutton(root,text='Other',variable=v7,value=3).grid(row=8,column=0)

Label(root,text="Enter Height").grid(column=9,row=0)
v3=Entry(root)
v3.grid(row=9,column=0)

Label(root,text="Enter Weight").grid(column=0,row=10)
v4=Entry(root)
v4.grid(row=0,column=11)
p=[]

def fun():
    b=[v0.get(),v1.get(),v5.get(),v6.get(),v7.get(),v3.get(),v4.get()]
    i=0
    p.append(v0.get())
    cur.executemany("insert into infodb values(?,?,?,?,?,?,?)",b)
    a.commit()

def fun2():
    cur.execute('select * from stu')
    t=cur.fetchall()
    print (t)

 def fun3():
 	cur.execute('''update infodb set name=? where id=?''',(v9.get(),v10.get()))
 	a.commit()

Button(root,text='insert',command=fun).grid(row=24,column=0)
Button(root,text='showall',command=fun2).grid(row=24,column=2)

root.mainloop()

