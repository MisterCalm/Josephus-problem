from tkinter import *

import math

import time

root = Tk()

root.geometry("1400x700+0+0")

root.title("Josephus problem")


c = Canvas(root, width=1400, height=700 , bg='#007FFF')

c.pack()

root.withdraw()


def create_circle(x, y, r, canvasName):

    x0 = x - r

    y0 = y - r

    x1 = x + r

    y1 = y + r

    return canvasName.create_oval(x0, y0, x1, y1, fill='#9F79EE', width=1.5)


# x0=600 y0=350 R=320

def drawNodes(arr):

    n = len(arr)

    nodeRadius = int(1900/ (2 * n))

    x = 1000

    y = 350

    nodeAngel = math.pi * 2 / n

    for i in range(1, n + 1):

        if nodeRadius > 27:

            nodeRadius = 26

        if n == 1:

            x = 680

            y = 350

            nodeRadius = 150

        create_circle(x, y, nodeRadius, c)

        c.create_text(x, y, text=arr[i - 1], font=('Helvetica',int(nodeRadius/2), 'bold'))

        x = 680 + 320 * (math.cos(i * nodeAngel))

        y = 350 + 320 * (math.sin(i * nodeAngel))


def display(mainArr):

    root.deiconify()

    for i in mainArr:

        drawNodes(i)

        c.update()

        c.delete('all')

        time.sleep(2)

    drawNodes(mainArr[-1])

    root.mainloop()
