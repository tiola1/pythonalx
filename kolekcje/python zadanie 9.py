"""
oferujemy następujące produkty
marchew: 2.35, ziemniaki: 2.20, cebula: 1.8, ogórki: 4.0

co chcesz kupić? marchew
ile chcesz kupić [marchew]? 3

Za [marchew] płacisz 7.05 PLN

2. Dodajemy obsługę magazynu
2.1 po zakupie ilość towaru się zmniejsza
2.2 jeśli ktoś chce kupić więcej niż w magazynie to nie może
"""
def wyprintuj(slownik, jednostka):
    for k,v in slowni
print("Wtamy w naszym zieleniaku ! oferujemy następujące produkty")
lista = {"marchew":2.35,
         "ziemniaki":2.20,
         "cebula":1.80,
         "ogórki": 4.40,
         }

magazyn = {"marchew": 15,
           "ziemniaki": 50,
           "cebula": 25,
           "ogórki": 10,
           }
for towar in lista:
    print(f" -{towar}: {lista[towar]}")

#print(lista)
while True:
    tryb = input("wybierz tryb: [z-zakupowy] [m-magazynowy]")
    if tryb== "k":
        break
    elif tryb == "z":
        while True: # zrobic fukncję z tego co się powtarza
            co_kupuje = input("Co chcesz kupić?[wpisz k by zakonczyc]?")
            if co_kupuje == "k":
                break
            if co_kupuje in lista:
                ile = input(f"ile chcesz kupić[{co_kupuje}]")
                ile = float(ile)
                if ile <= magazyn[co_kupuje]:
                    należność = ile * lista [co_kupuje]
                    magazyn[co_kupuje] = magazyn[co_kupuje] - ile
                    #magazyn{co_kupuje} -= 1
                    print(f"Za[{co_kupuje})placisz : {należność: 2f} PLN")
                else:
                    print("Ma za mało towaru")
            else:
                print("nie ma takiego produktu!")
    elif tryb == "m":
        while True:
            produkt_do_dodania = input("co chcesz dodać")
            ile_do_dodania = int(input("Ile chcesz dodać"?)

            if not produkt_do_dodania in lista:
                cena_nowego_pr = float(input("jaka będzie cena?")
                towary[produkt_do_dodania] = cena_nowego_pr

            magazyn[produkt_do_dodania]=magazyn.get(produkt_do_dodania, 0) + ile_do_dodania