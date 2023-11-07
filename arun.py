from tkinter import*
import sqlite3
conn=sqlite3.connect('ash.db')
window=Tk()
window.title("sql")
window.geometry("1000x1000")
conn.execute('''create table
if not exists data(fName varchar(20),
              lName varchar(20));''')
def getdata():
    data1=entry_1.get()
    print(data1)
    data2=entry_2.get()
    print(data2)
    conn.execute('''insert into data
(fName,lName)values(?,?)''',(data1,data2))
    conn.commit()

label_1 =Label(window,text="FullName", width=20,font=("bold",10))
label_1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_1=Entry(window)
entry_1.grid(row=1, column=1, padx=10, pady=10, sticky="w")

label_2=Label(window,text="lastname", width=20,font=("bold",10))

label_2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_2=Entry(window)
entry_2.grid(row=2, column=1, padx=10, pady=10, sticky="w")

b=Button(window, text='Submit' , width=20,bg="black",fg='white',command=getdata)
b.grid(row=7, column=1, columnspan=4, padx=10,pady=10, sticky="w")


window.mainloop()
