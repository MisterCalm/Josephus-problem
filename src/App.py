import tkinter as tk
from utility.Algorithm import Josephus
from utility.CircularGraph import *


def showResults():

    res = Josephus(int(e1.get()), int(e2.get()))

    master.destroy()

    display(res)


master = tk.Tk()

master.title("Josephus")

master.geometry("40x40+330+240")

master.minsize(width=800, height=220)

master.configure(bg="#99004C")

tk.Label(master, text="Please Enter Number Of Person In Josephus Problem : ", bg="#9933FF").place(relx=0.2, rely=0.1)

tk.Label(master, text="Please Enter The Number Of Times To Proceed : ", bg="#FF007F").place(relx=0.2, rely=0.2)

e1 = tk.Entry(master)

e2 = tk.Entry(master)

e1.place(relx=0.6, rely=0.1)

e2.place(relx=0.6, rely=0.2)

tk.Button(master, text='Show', command=showResults, height=2, width=40, bg="#00FF80").place(relx=0.5, rely=0.5, anchor="center")

tk.mainloop()
