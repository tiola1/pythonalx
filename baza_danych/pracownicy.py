
#"baza danych" pracowników
import datetime
import json
#miejsce przechowujące dane na temat rekordów pracowników
dane_pracowników =list()

try:

    with open("pracownicy.dat", "wt")as fd:
        dane_pracowników=json.load(fd)
except:
    print("Odczyt plików nie udał się")


def wprowadz_dane():
    print("="*40)
    print("Wprowadz dane pracownika")

    imie = None

    while(True):
        imie = input("Podaj imie:").upper().strip()
        if len(imie)<=2:
            print(("Podaj imie")
        else:
            break

    nazwisko = None
    while True:
        nazwisko = input("Podaj nazwisko: ").upper().strip()
        if len(nazwisko)>=3:
            break
        print("Podaj nazwisko")

    rok_urodzenia= None
    while True:
        try:
            rok_urodzenia= int(input("Podaj rok urodzenia: "))
            if rok_urodzenia <1930:
                print("Idź na emeryturę")
                continue
            rok_biezacy =datetime.datetime.now().year
            if rok_biezacy - rok_urodzenia>=15:
                break

            print("Za młodys na pracę")
        except Exception as exc:
            print("Podaj rok urodzenia", exc)

    pensja = None
    while True:
        try:
            pensja = float(input("Podaj wartość wynagrodzenia: "))
            if (pensja>0):
                break
            print("podaj kwotę wynagrodzenia")
        except Exceptions as exc:
            print("Podaj kwotę" exc)


    return {"imie"  :imie, "nazwisko" : nazwisko, "rok_urodzenia" : rok_urodzenia, "pensja" : pensja}


    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    rok_urodzenia = input("Podaj rok urodzenia: ")
    pensja = input("Podaj wartość wynagrodzenia: ")

    pass


#pokaz zawartosc zmiennej "dane pracowników"
def pokaz_rekordy():
    print("========lista pracowników=========")
    for rekordin dane_pracowników:
        print((f"{rekord.get('imie')}"))


####pętla główna

while (True):
    operacja = input("Podaj operację[d/w/q]: ").strip().upper()
    if operacja=="Q":
        print("Koniec aplikacji")
        break

    if operacja =="W":
        # a tu będę wypisywał dane użytkowników
        pass
        pokaz_rekordy()

    if operacja == "D":
        #a tu będę prosił o dane pracownika
        rekord = wprowadz_dane()
        dane_pracowników.append(rekord)
        with open("pracownicy.dat", "wt")as fd:
            json.dump(dane_pracowników, fd)


