from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('800x600+800+300')  # размеры
root.title('Текстовый редактор')  # Заголовок

s = ttk.Style()
s.configure('my.TButton', padding=6)


def choose(event):
    print(select.current(), select.get())


select = ttk.Combobox(root, values=['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь'])
select.place(relx=0.5, rely=0.5, anchor=CENTER)
select.current(0)

select.bind("<<ComboboxSelected>>", choose)
root.mainloop()