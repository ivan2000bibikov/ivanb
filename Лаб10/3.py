from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import codecs
import sqlite3

db = sqlite3.connect('book.db')
sql = db.cursor()

sql.execute("SELECT name, avtor, god FROM books WHERE name = 'Граф Монте-Кристо'")

window = Tk()
window.title('Работа с БД')
window.geometry('430x90')

def d():
	global sqlz1
	sqlz1 = e1.get()
	sql.execute(sqlz1)
	db.commit()

def y():
	global sqlz2
	sqlz2 = e2.get()
	sql.execute(sqlz2)
	db.commit()

l1 = Label(window, text="Добавление данных в БД (используйте SQL-запрос)")
l1.place(x=4, y=0)
e1 = Entry(window, width = 50)
e1.place(x=4, y=20)
l2 = Label(window, text="Удаление данных из БД (используйте SQL-запрос)")
l2.place(x=4, y=40)
e2 = Entry(window, width = 50)
e2.place(x=4, y=60)
btn = Button(window, text="Добавить данные", command=d)
btn.place(x=312, y=16)
btn2 = Button(window, text="Удалить данные", command=y)
btn2.place(x=312, y=56)
 
window.mainloop()
