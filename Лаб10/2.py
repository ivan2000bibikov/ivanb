from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import codecs
import sqlite3

db = sqlite3.connect('book.db')
sql = db.cursor()
sql2 = db.cursor()
sql3 = db.cursor()
sql4 = db.cursor()
sql5 = db.cursor()

sql.execute("SELECT name, avtor, god FROM books WHERE name = 'Граф Монте-Кристо'")
sql2.execute("SELECT name, avtor, god FROM books WHERE name = 'Время жить и время умирать'")
sql3.execute("SELECT name, avtor, god FROM books WHERE name = 'Рождественская песнь'")
sql4.execute("SELECT name, avtor, god FROM books WHERE name = 'Три мушкетера'")
sql5.execute("SELECT name, avtor, god FROM books WHERE name = 'Евгений Онегин'")

window = tk.Tk()
window.title('Поиск книг')
window.geometry('340x208')

def print_selection():
	pass

def res():
	if(var1.get() == 1):
		messagebox.showinfo("Результат", sql.fetchone())
		messagebox.showinfo("Результат", sql4.fetchone())
	if(var2.get() == 1):
		messagebox.showinfo("Результат", sql2.fetchone())
	if(var3.get() == 1):
		messagebox.showinfo("Результат", sql3.fetchone())
	if(var4.get() == 1):
		messagebox.showinfo("Результат", sql5.fetchone())
	if(var5.get() == 1):
		messagebox.showinfo("Результат", sql5.fetchone())
	if(var6.get() == 1):
		messagebox.showinfo("Результат", sql2.fetchone())
		messagebox.showinfo("Результат", sql3.fetchone())
	if(var7.get() == 1):
		messagebox.showinfo("Результат", sql.fetchone())
		messagebox.showinfo("Результат", sql4.fetchone())

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
btn = tk.IntVar()

c1 = tk.Checkbutton(window, text='Дюма',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='Ремарк',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='Диккенс',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='Пушкин',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()
c5 = tk.Checkbutton(window, text='Год издания: 2015',variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.pack()
c6 = tk.Checkbutton(window, text='Год издания: 2018',variable=var6, onvalue=1, offvalue=0, command=print_selection)
c6.pack()
c7 = tk.Checkbutton(window, text='Год издания: 2019',variable=var7, onvalue=1, offvalue=0, command=print_selection)
c7.pack()
btn = tk.Button(window, text="Результат", command=res)
btn.pack()
 
window.mainloop()
