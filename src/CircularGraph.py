from tkinter import*

import math

import time

root = Tk()

root.geometry("900x600")

root.title("Josephus problem")

c = Canvas(root,width=600,height=600)

c.pack()

root.withdraw()

def create_circle(x,y,r,canvasName):
    
    x0 = x-r
    y0 = y-r
    x1 = x+r
    y1 = y+r

    return canvasName.create_oval(x0,y0,x1,y1,fill='orange',width=1.5)

#x0=300 y0=300 R=250

def drawNodes(arr):

    n=len(arr)

    nodeRadius = int(1571/(2*n))

    x=550

    y=300

    nodeAngel = (math.pi)*2/n

    for i in range(1,n+1):

        if(nodeRadius>46):nodeRadius=46

        if(n==1):

            x=300

            y=300

        create_circle(x,y,nodeRadius,c)

        c.create_text(x,y,text=arr[i-1],font=('Helvetica',nodeRadius,'bold'))

        x=300+250*(math.cos(i*nodeAngel))

        y=300+250*(math.sin(i*nodeAngel))

def display(mainArr):

    root.deiconify()

    for i in mainArr:

        drawNodes(i)

        time.sleep(2)

        c.update()

        c.delete('all')

    drawNodes(mainArr[-1])

    root.mainloop()
