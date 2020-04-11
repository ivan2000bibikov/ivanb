from tkinter import *
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
main_menu = Menu()
file_menu = Menu()
file1_menu = Menu()
file2_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_command(label="Open module")
file_menu.add_separator()
file1_menu.add_command(label="Copy")
file1_menu.add_command(label="Find")
file1_menu.add_command(label="Past")
file2_menu.add_command(label="Options")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=file1_menu)
main_menu.add_cascade(label="View", menu=file2_menu)
root.config(menu=main_menu)
root.mainloop()
