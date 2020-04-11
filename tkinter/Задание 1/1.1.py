from tkinter import *
from tkinter import messagebox
 
def display_full_name():
	messagebox.showinfo("окно сообщения", name.get() + '\n'
                            + surname.get() + '\n'
                            + nayname.get() + '\n'
                            + rainame.get() + '\n'
                            + unyname.get() + '\n'
                            + hetname.get() + '\n'
                            + okoname.get())
 
root = Tk()
root.title("Информация учащегося в колледже Агу")
 
name = StringVar()
surname = StringVar()
nayname = StringVar()
rainame = StringVar()
unyname = StringVar()
hetname = StringVar()
okoname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
nayname_label = Label(text="Введите год рождения:")
rainame_label = Label(text="Введите дату поступления :")
unyname_label = Label(text="Введите направление :")
hetname_label = Label(text="Введите специальность :")
okoname_label = Label(text="Введите дату окончания :")

name_label.grid(row=0, column=0, sticky="w")           
surname_label.grid(row=1, column=0, sticky="w")
nayname_label.grid(row=2, column=0, sticky="w")
rainame_label.grid(row=3, column=0, sticky="w")
unyname_label.grid(row=4, column=0, sticky="w")
hetname_label.grid(row=5, column=0, sticky="w")
okoname_label.grid(row=6, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
nayname_entry = Entry(textvariable=nayname)
rainame_entry = Entry(textvariable=rainame)
unyname_entry = Entry(textvariable=unyname)
hetname_entry = Entry(textvariable=hetname)
okoname_entry = Entry(textvariable=okoname)

name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
nayname_entry.grid(row=2,column=1, padx=5, pady=5)
rainame_entry.grid(row=3,column=1, padx=5, pady=5)
unyname_entry.grid(row=4,column=1, padx=5, pady=5)
hetname_entry.grid(row=5,column=1, padx=5, pady=5)
okoname_entry.grid(row=6,column=1, padx=5, pady=5)

message_button = Button(text="показать", command=display_full_name)
message_button.grid(row=7,column=1, padx=10, pady=3, sticky="e")
 
root.mainloop()

