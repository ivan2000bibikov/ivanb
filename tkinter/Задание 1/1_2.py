import tkinter as tk

Money = 0

window = tk.Tk()
window.title('My Window')
window.geometry('250x150')
 
l = tk.Label(window, bg='white', width=20, text='Цена')
l.pack()

def print_selection():
	global Money
	Money = 0
	if(var1.get() == 1):
		Money += 8000
	if(var2.get() == 1):
		Money += 1800
	if(var3.get() == 1):
		Money += 1000
	if(var4.get() == 1):
		Money += 5000
	if(var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0):
		Money = 0

def res():
	global Money
	l.config(text=Money)
 
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
btn = tk.IntVar()

c1 = tk.Checkbutton(window, text='Монитор',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='Плата расширения',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='Клавиатура',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='SSD-накопитель',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()
btn = tk.Button(window, text="Результат", command=res)
btn.pack()
 
window.mainloop()
