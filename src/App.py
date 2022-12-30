import tkinter as tk

from src.Algorithm import Josephus
from src.CircularGraph import display


def showResults():
    print(Josephus(int(e1.get()), int(e2.get())))


master = tk.Tk()
master.title("Josephus")
master.minsize(width=800, height=250)
master.configure(bg="pink")
tk.Label(master, text="Please Enter Number Of Person In Josephus Problem : ").place(relx=0.2, rely=0.1)
tk.Label(master, text="Please Enter The Number Of Times To Proceed : ").place(relx=0.2, rely=0.2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.place(relx=0.6, rely=0.1)
e2.place(relx=0.6, rely=0.2)

tk.Button(master, text='Show', command=showResults, height=2, width=40).place(relx=0.5, rely=0.5, anchor="center")

tk.mainloop()
