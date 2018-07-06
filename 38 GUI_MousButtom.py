from tkinter import *
okno = Tk()

def lewybottom(event):
    print(event.x, event.y)
def prawybottom(event):
    print(event.x, event.y)
def srodkowybottom(event):
    print(event.x, event.y)

ramka = Frame (okno, width = 480, height = 320)

ramka.bind("<Button-1>",lewybottom)
ramka.bind("<Button-3>",prawybottom)
ramka.bind("<Button-2>",srodkowybottom)
ramka.pack()
okno.mainloop()