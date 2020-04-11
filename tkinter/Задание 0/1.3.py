from tkinter import *
languages = [("C++", 1), ("SQL:", 2), ("C#", 3), ("Java", 4),("Python", 5)]
def select():
    l = language.get()
    if l == 1:
    	sel.config(text="Выбран C++")
    elif l == 2:
    	sel.config(text="Выбран SQL")
    elif l == 3:
    	sel.config(text="Выбран C#")
    elif l == 4:
    	sel.config(text="Выбран Java")
    elif l == 5:
        sel.config(text="Выбран Python")

root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)
language = IntVar()
row = 2
for txt, val in languages:
	Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, command=select)\
    	.grid(row=row, sticky=W)
	row += 1
sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)

root.mainloop()
