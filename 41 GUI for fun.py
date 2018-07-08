import tkinter, sys, random
from tkinter import messagebox

def zmiana():
    global liczba
    liczba = random.rendint(1, s.get())

def koniec():
    sys.exit()

def sprawdz():
    x = int(e.get())
    if x > liczba:
        l.config(text = "Moja liczba jest mniejsza od twojej")
        messagebox.showinfo(title = "UWAGA", message = "Moja liczba jest mniejsza od twojej")
    if x < liczba:
        l.config(text = "Moja liczba jet większa od Twojej")
        messagebox.showinfo(title = "UWAGA", message = " Moja liczba jest większa od twojej")
    if x == liczba:
        l.config(text = "Brawo zgadłeś")
def nowagra():
    liczba = random.rendint(1, 100)
    x = 0
    y = 0
    l.config(text = "")
random.seed()
main = tkinter.Tk()

liczba = random.randint(1, 100)
x = 0
y = 0
#pole do wpisywania text
e = tkinter.Entry(main, justify = "center")
# TEXT
l = tkinter.Label(main, text = "Wprowadz swoja liczbe do loteri")
# PRZCISKI
b = tkinter.Button(main, text ="Zakończ", command = koniec, width = 20)
b2 = tkinter.Button(main, text = " Sprawdź Wynik!", command = sprawdz, width = 20)
b3 = tkinter.Button(main, text = "Nowa gra",command = nowagra, width = 20)
s = tkinter.Scale(main,  orient = "horizontal", to_= 100, from_=1, width = 15)
b4 = tkinter.Button(main, text = "Zmien zakres liczb", command = zmiana, heigh = 1)
l.pack()
e.pack()
s.pack()
b4.pack()
b2.pack()
b3.pack()
b.pack()
main.mainloop()
