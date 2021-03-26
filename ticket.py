class Czlowiek:
    def __init__(self,imie,nazwisko,wiek,nrtel,kwota,bilet,mecz):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.nrtel = nrtel
        self.kwota = kwota
        self.bilet = bilet
        self.mecz = mecz


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
        mecz = input("Jaki mecz: ")
        x += 1

def mecze():
    ligowe = int(input("[1]ligowy czy [2]europejski => 1/2 "))

    if ligowe == 1:
     print("[1] => REAL MADRYT VS FC BARCELONA ")
     print("[2] => PSG VS O.LYON ")
     print("[3] => CHELASEA VS LIVERPOOL ")
     print("[4] => BORUSSIA VS MONACHIUM ")
     print("[5] => JUVENTUS VS NAPOLI ")
     print("[6] => A.MADRYT VS CELTA VIGO ")
    elif ligowe == 2:
     print("R.MADRYT VS JUVENTUS")
     print("FC BARCELONA VS MAN.CITY")
     print("PSG VS LIVERPOOL")
     print("SZAHTAR DONIECK VS CHELSEA")
     print("A.MADRYT VS KOPALINA")
     print("TO.HOTSPUR VS MAN.UTD")
     print("SEVILLA VS AS.MONACO")
     print("INTER MEDIOLAN VS SLASK WROCLAW")
    else:
        print("Wprowadzono zle dane, popraw")
        mecze()
