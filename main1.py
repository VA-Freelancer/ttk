from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('800x600+800+300')  # размеры
root.title('Текстовый редактор')  # Заголовок

s = ttk.Style()
s.configure('my.TButton', padding=6)

Button(root, text="Button 1", padx=40, pady=5).pack(pady=10)
ttk.Button(root, text="Button 2", width=21, style="my.TButton").pack()
ttk.Button(root, text="Button 2", width=21).pack()

Entry(root).pack(pady=10)
ttk.Entry(root).pack()
root.mainloop()
