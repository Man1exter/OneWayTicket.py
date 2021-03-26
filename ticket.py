class Czlowiek:
    def __init__(self,imie,nazwisko,wiek,nrtel,kwota,bilet):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.nrtel = nrtel
        self.kwota = kwota
        self.bilet = bilet


def bukowanie():
 ile = int(input("Ile osob chce kupic bilet? "))

 if ile == str:
    print("!Wprowadzono bledne dane!")
 else:
    x = 0 # do iterowania w petli..
    while x < ile:
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        wiek = int(input("Podaj wiek: "))
        nrtel = int(input("Podaj numer telefonu: "))
        kwota = int(input("Podaj pelna kwote biletu: "))
        bilet = input("Bilet[ulgowy][normalny][szkolny]: ")
        x += 1



