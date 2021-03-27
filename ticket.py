import linecache
import os
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
 plik = open("zabukowane.txt","a")

 if ile == str:
    print("!Wprowadzono bledne dane!")
 else:
    x = 0 # do iterowania w petli..
    while x < ile:
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        wiek = (input("Podaj wiek: "))
        nrtel = (input("Podaj numer telefonu: "))
        kwota = (input("Podaj pelna kwote biletu: "))
        bilet = input("Bilet[ulgowy][normalny][szkolny]: ")
        mecz = input("Jaki mecz: ")
        if plik.writable():
         plik.write(imie )
         plik.write(" ")
         plik.write( nazwisko )
         plik.write(" ")
         plik.write( wiek )
         plik.write(" ")
         plik.write( nrtel )
         plik.write(" ")
         plik.write( kwota )
         plik.write(" ")
         plik.write( bilet )
         plik.write(" ")
         plik.write( mecz )
         plik.write(" ")
         plik.write("\n")
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

# zapis / odczyt z / do pliku docelowego po dopisaniu 1funckji aktywnej..

def rfile():
    plik = open("zabukowane.txt","r")
    if plik.readable():
       tekst =  plik.read()
    print(tekst)

print("[1] => bukowanie + zapis do pliku <= ")
print("[2] => zobaczyc aktualne mecze <= ")
print("[3] => zobaczyc zapisane osoby <=  ")
print("[4] => pokazywanie konkretnego wiersza z pliku <=  ")
print("[5] => zmiana nazwy pliku <=  ")
print("[5] => zliczenie wierszy pliku <=  ")
zdarzenie = int(input("CO CHCESZ ZROBIC?"))

def pokazywanie():
    numer_wiersza = int(input("Podaj numer wiersza, ktory chcesz pobrac"))
    wiersz = linecache.getline("zabukowane.txt",numer_wiersza)
    print(wiersz)

def zmianaNazwy():
  nowy = input("podaj nowa nazwe pliku (NIE ZAPOMNIJ O .TXT) => ")
  os.rename("zabukowane.txt",nowy)

def wierszePliku():
 linie = len ( open ("zabukowane.txt","r").readlines())
 print(linie)


if zdarzenie == 1:
    bukowanie()
elif zdarzenie == 2:
    mecze()
elif zdarzenie == 3:
    rfile()
elif zdarzenie == 4:
   pokazywanie()
elif zdarzenie == 5:
    zmianaNazwy()
elif zdarzenie == 6:
    wierszePliku()


#Zamiana fragmentu tekstu w pliku
#zrodlo = open ( ’ nazwa_pliku ’). readlines ()
#cel = open ( ’ nazwa_pliku ’ , ’w ’)
#for s in zrodlo :
#cel . write ( s . replace (" co zamienic " , " na co "))
#cel . close ()
