from tkinter import *


background_color = "#808080"
label_color = "#DCDCDC"
root = Tk()

root.minsize(600, 300)
root.title('парикмахерская')
root.configure(bg=background_color)

surname = StringVar()
surname_to_delete = StringVar()
surname_to_find = StringVar()
date = StringVar()
date_to_find = StringVar()
service = StringVar()
price = IntVar()


variables = [('Фамилия', surname), ('Дата', date), ('Услуга', service), ('Цена', price)]
variables2 = [('Поиск по фамилии', surname_to_find), ('Поиск по дате', date_to_find)]


def create_form(*attributes):
    label, var, row_count = attributes
    Label(text=label, bg=label_color).grid(row=row_count, column=0, sticky='w')
    Entry(textvariable=var).grid(row=row_count,column=1, padx=5, pady=5)

row_count = 0
for label, var in variables:
    create_form(label, var, row_count)
    row_count += 1

Button(text="Добавить клиента").grid(row=4,column=0, padx=5, pady=5, sticky="e")
Button(text="Добавить значение к клиенту").grid(row=4,column=1, padx=5, pady=5, sticky="e")

Label(text=variables[0][0], bg=label_color).grid(row=0, column=3, sticky='w')
Entry(textvariable=surname_to_delete).grid(row=0,column=4, padx=5, pady=5)
Button(text="Удалить клиента").grid(row=1,column=4, padx=5, pady=5, sticky="e")

row_count = 5
for label, var in variables2:
    create_form(label, var, row_count)
    row_count += 1

Button(text="Найти").grid(row=10,column=1, padx=5, pady=5, sticky="e")





root.mainloop()
