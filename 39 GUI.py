import tkinter, sys

def koniec():
    sys.exit()
def zmiana():
    l.config(text = "Wciśnij zakończ")
main = tkinter.Tk()
# TEXT
l = tkinter.Label(main, text = "wciśnij przycisk poniżej")
# PRZCISKI
b = tkinter.Button(main, text ="Zakończ", command = koniec )
b2 = tkinter.Button(main, text = " Przycisk", command = zmiana)
l.pack()
b.pack()
b2.pack()
main.mainloop()
