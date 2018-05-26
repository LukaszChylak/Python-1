from tkinter import *
okno = Tk ()

def wypisz(event):
    print ("Witaj !!!")

przycisk = Button(okno,text = "Nacisnij mnie !")
przycisk.bind("<Button -1>", wypisz)
przycisk.pack()
przycisk.mainloop()