# CLASSA
class czlowiek:
# ATRZBUTZ KLASS
    imie = ""
    nazwisko = ""
# FUNKCJA / METODA
    def przedstawsie(self):
        print(self.imie," ",self.nazwisko)

    def zmienimie(self):
        self.imie = input ("Podaj imie: ")

# OBIEKT
znajomy = czlowiek()
znajomy2 = czlowiek()
znajomy.imie = "Kondziu"
znajomy.nazwisko = "Jakie"
znajomy2.imie = "Piotr"
znajomy2.nazwisko = "Jakie"
# URUCHOMIENIE POROGRAMU
znajomy.przedstawsie()
znajomy2.przedstawsie()