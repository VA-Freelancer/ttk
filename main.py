from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('800x600+800+300')  # размеры
root.title('Текстовый редактор')  # Заголовок

s = ttk.Style()
print(s.theme_names())
print(s.theme_use())
s.theme_use('clam')
Button(root, text="Button 1", padx=40, pady=5).pack(pady=10)
ttk.Button(root, text="Button 2", width=21).pack()

Entry(root).pack(pady=10)
ttk.Entry(root).pack()
root.mainloop()
